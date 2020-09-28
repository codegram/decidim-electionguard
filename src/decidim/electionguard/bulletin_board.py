from electionguard.election import CiphertextElectionContext, ElectionDescription, InternalElectionDescription
from electionguard.elgamal import elgamal_combine_public_keys
from electionguard.group import ElementModP
from typing import Dict, Set
from .common import Context, ElectionStep, Wrapper
from .utils import InvalidElectionDescription, complete_election_description, serialize, deserialize_key


class BulletinBoardContext(Context):
    number_of_guardians: int
    public_keys: Dict[str, ElementModP] = {}
    election: ElectionDescription
    election_metadata: InternalElectionDescription
    election_context: CiphertextElectionContext


class ProcessCreateElection(ElectionStep):
    message_type = "create_election"

    number_of_guardians: int
    quorum: int
    election_description: dict

    def process_message(self, message_type: str, message: dict, context: Context):
        self.parse_create_election_message(message)
        context.number_of_guardians = self.number_of_guardians
        context.election = ElectionDescription.from_json_object(complete_election_description(self.election_description))
        if not context.election.is_valid():
            raise InvalidElectionDescription()

        self.next_step = ProcessTrusteeElectionKeys()

    def parse_create_election_message(self, message: dict):
        self.number_of_guardians = len(message['trustees'])
        self.quorum = message['scheme']['parameters']['quorum']
        self.election_description = message['description']


class ProcessTrusteeElectionKeys(ElectionStep):
    message_type = "trustee_election_keys"

    def process_message(self, message_type: str, message: dict, context: Context):
        guardian_id, guardian_public_key = self.parse_trustee_public_keys(message)
        context.public_keys[guardian_id] = guardian_public_key

        if len(context.public_keys) == context.number_of_guardians:
            self.next_step = ProcessTrusteeElectionPartialKeyBackups()

    def parse_trustee_public_keys(self, message: dict):
        return (message['owner_id'], deserialize_key(message['election_public_key']))


class ProcessTrusteeElectionPartialKeyBackups(ElectionStep):
    message_type = "trustee_election_partial_key_backup"

    partial_keys_received: Set[str] = set()

    def process_message(self, message_type: str, message: dict, context: Context):
        self.partial_keys_received.add(message['owner_id'])

        if len(self.partial_keys_received) == context.number_of_guardians:
            self.next_step = ProcessTrusteeVerification()


class ProcessTrusteeVerification(ElectionStep):
    message_type = "trustee_verification"

    verification_received: Set[str] = set()

    def process_message(self, message_type: str, message: dict, context: Context):
        self.verification_received.add(message['owner_id'])

        if len(self.verification_received) == context.number_of_guardians:
            return serialize(elgamal_combine_public_keys(context.public_keys.values()))


class BulletinBoard(Wrapper):
    def __init__(self) -> None:
        super().__init__(BulletinBoardContext(), ProcessCreateElection())
