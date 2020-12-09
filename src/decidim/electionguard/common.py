from electionguard.election import CiphertextElectionContext, ElectionDescription, InternalElectionDescription
from electionguard.election_builder import ElectionBuilder
from .utils import complete_election_description, InvalidElectionDescription
try:
    import cPickle as pickle
except:  # noqa: E722
    import pickle


class Context:
    election: ElectionDescription
    election_builder: ElectionBuilder
    election_metadata: InternalElectionDescription
    election_context: CiphertextElectionContext
    number_of_guardians: int
    quorum: int

    def build_election(self, election_creation: dict):
        self.election = ElectionDescription.from_json_object(complete_election_description(election_creation['description']))

        if not self.election.is_valid():
            raise InvalidElectionDescription()

        self.number_of_guardians = len(election_creation['trustees'])
        self.quorum = election_creation['scheme']['parameters']['quorum']
        self.election_builder = ElectionBuilder(self.number_of_guardians, self.quorum, self.election)


class ElectionStep:
    message_type: str

    def __init__(self) -> None:
        self.next_step = None
        self.setup()

    def setup(self):
        pass

    def skip_message(self, message_type: str):
        return self.message_type != message_type

    def process_message(self, message_type: str, message: dict, context: Context):
        raise NotImplementedError()


class Wrapper:
    context: Context
    step: ElectionStep

    def __init__(self, context: Context, step: ElectionStep) -> None:
        self.context = context
        self.step = step

    def skip_message(self, message_type: str) -> bool:
        return self.step.skip_message(message_type)

    def process_message(self, message_type: str, message: dict) -> dict:
        if self.step.skip_message(message_type):
            return

        result = self.step.process_message(message_type, message, self.context)

        if self.step.next_step:
            self.step = self.step.next_step

        return result

    def backup(self) -> dict:
        return pickle.dumps(self)

    def restore(backup: dict):
        return pickle.loads(backup)
