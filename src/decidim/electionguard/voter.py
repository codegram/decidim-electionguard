from electionguard.ballot import PlaintextBallot, PlaintextBallotContest, PlaintextBallotSelection
from electionguard.election import CiphertextElectionContext, ElectionDescription, InternalElectionDescription
from electionguard.election_builder import ElectionBuilder
from electionguard.encrypt import encrypt_ballot, selection_from
from electionguard.group import ElementModQ
from electionguard.utils import get_optional
from typing import List
from .common import Context, ElectionStep, Wrapper
from .utils import InvalidElectionDescription, complete_election_description, serialize, deserialize_key


class VoterContext(Context):
    election: ElectionDescription
    election_builder: ElectionBuilder
    election_metadata: InternalElectionDescription
    election_context: CiphertextElectionContext


class ProcessCreateElection(ElectionStep):
    number_of_guardians: int
    quorum: int
    election_description: dict

    message_type = 'create_election'

    def process_message(self, message_type: str, message: dict, context: Context):
        self.parse_create_election_message(message)
        context.election = ElectionDescription.from_json_object(complete_election_description(self.election_description))
        if not context.election.is_valid():
            raise InvalidElectionDescription()

        context.election_builder = ElectionBuilder(self.number_of_guardians, self.quorum, context.election)
        self.next_step = ProcessJointElectionKey()

    def parse_create_election_message(self, message: dict):
        self.number_of_guardians = len(message['trustees'])
        self.quorum = message['scheme']['parameters']['quorum']
        self.election_description = message['description']


class ProcessJointElectionKey(ElectionStep):
    message_type = 'joint_election_key'

    def process_message(self, message_type: str, message: dict, context: Context):
        joint_key = deserialize_key(message['joint_election_key'])

        context.election_builder.set_public_key(get_optional(joint_key))
        context.election_metadata, context.election_context = get_optional(context.election_builder.build())


class Voter(Wrapper):
    ballot_id: str

    def __init__(self, ballot_id: str) -> None:
        super().__init__(VoterContext(), ProcessCreateElection())
        self.ballot_id = ballot_id

    def encrypt(self, ballot: dict) -> dict:
        ballot_style: str = self.context.election.ballot_styles[0].object_id
        contests: List[PlaintextBallotContest] = []

        for contest in self.context.election_metadata.get_contests_for(ballot_style):
            selections: List[PlaintextBallotSelection] = [
                selection_from(selection, False, selection.object_id in ballot[contest.object_id])
                for selection in contest.ballot_selections
            ]

            contests.append(PlaintextBallotContest(contest.object_id, selections))

        plaintext_ballot = PlaintextBallot(self.ballot_id, ballot_style, contests)

        return serialize(encrypt_ballot(
            plaintext_ballot,
            self.context.election_metadata,
            self.context.election_context,
            ElementModQ(0),
            None,
            True
        ))
