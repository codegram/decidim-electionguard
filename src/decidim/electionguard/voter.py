from electionguard.election import (
    ElectionDescription,
    InternalElectionDescription,
    CiphertextElectionContext
)
from electionguard.election_builder import ElectionBuilder
from electionguard.utils import get_optional
from electionguard.encrypt import encrypt_ballot, selection_from
from electionguard.group import ElementModP, ElementModQ
from electionguard.ballot import (
    PlaintextBallot,
    PlaintextBallotContest,
    PlaintextBallotSelection,
)

from .utils import complete_election_description, serialize

class InvalidElectionDescription(Exception):
  """Exception raised when the election description is invalid."""
  pass

class VoterState:
  election: ElectionDescription
  election_builder: ElectionBuilder
  election_metadata: InternalElectionDescription
  election_context: CiphertextElectionContext

class VoterElectionStep:
  voter_state: VoterState

  def __init__(self, voter_state: VoterState) -> None:
    self.voter_state = voter_state
    self.next_step = None

  def skip_message(self, message_type: str):
    return False

  def process_message(self, message_type: str, message: dict):
    raise NotImplementedError()

class ProcessCreateElection(VoterElectionStep):
  number_of_guardians: int
  quorum: int
  election_description: dict

  def skip_message(self, message_type: str):
    return message_type != 'create_election'

  def process_message(self, message_type: str, message: dict):
    self.parse_create_election_message(message)
    self.voter_state.election = ElectionDescription.from_json_object(complete_election_description(self.election_description))
    if not self.voter_state.election.is_valid():
      raise InvalidElectionDescription()

    self.voter_state.election_builder = ElectionBuilder(self.number_of_guardians, self.quorum, self.voter_state.election)

    self.next_step = ProcessJointElectionKey

  def parse_create_election_message(self, message: dict):
    self.number_of_guardians = len(message['trustees'])
    self.quorum = message['scheme']['parameters']['quorum']
    self.election_description = message['description']

class ProcessJointElectionKey(VoterElectionStep):
  def skip_message(self, message_type: str):
    return message_type != 'joint_election_key'

  def process_message(self, message_type: str, message: dict):
    joint_key = ElementModP(message['joint_election_key'])

    self.voter_state.election_builder.set_public_key(get_optional(joint_key))
    self.voter_state.election_metadata, self.voter_state.election_context = get_optional(self.voter_state.election_builder.build())

class Voter:
  voter_state: VoterState
  step: VoterElectionStep
  ballot_id: str

  def __init__(self, ballot_id: str) -> None:
    self.voter_state = VoterState()
    self.step = ProcessCreateElection(self.voter_state)
    self.ballot_id = ballot_id

  def skip_message(self, message_type: str) -> bool:
    return self.step.skip_message(message_type)

  def process_message(self, message_type: str, message: dict) -> dict:
    result = self.step.process_message(message_type, message)

    if self.step.next_step:
      self.step = self.step.next_step(self.voter_state)

    return result

  def encrypt(self, ballot: dict) -> dict:
    ballot_style: str = self.voter_state.election.ballot_styles[0].object_id
    contests: List[PlaintextBallotContest] = []

    for contest in self.voter_state.election_metadata.get_contests_for(ballot_style):
      selections: List[PlaintextBallotSelection] = list()
      for selection in contest.ballot_selections:
        selections.append(selection_from(selection, False, selection.object_id in ballot[contest.object_id]))

      contests.append(PlaintextBallotContest(contest.object_id, selections))

    plaintext_ballot = PlaintextBallot(self.ballot_id, ballot_style, contests)

    return serialize(encrypt_ballot(
      plaintext_ballot,
      self.voter_state.election_metadata,
      self.voter_state.election_context,
      ElementModQ(0),
      None,
      True
    ))