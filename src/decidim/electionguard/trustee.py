from electionguard.key_ceremony import PublicKeySet, ElectionPartialKeyBackup
from electionguard.guardian import Guardian
from pickle import loads, dumps
from typing import Set
from .utils import serialize, deserialize
from .common import Context, ElectionStep, Wrapper


class TrusteeContext(Context):
    guardian: Guardian
    guardian_id: str
    guardian_ids: Set[str]

    def __init__(self, guardian_id: str) -> None:
        self.guardian_id = guardian_id


class ProcessCreateElection(ElectionStep):
    order: int
    guardian_ids: Set[str]
    quorum: int

    message_type = "create_election"

    def process_message(self, message_type: str, message: dict, context: Context):
        self.parse_create_election_message(context.guardian_id, message)
        context.guardian_ids = self.guardian_ids
        context.guardian = Guardian(context.guardian_id, self.order, len(self.guardian_ids), self.quorum)

        self.next_step = ProcessTrusteeElectionKeys()

        public_keys = context.guardian.share_public_keys()

        return serialize(public_keys)

    def parse_create_election_message(self, guardian_id: int, message: dict):
        guardian_ids = [trustee["name"] for trustee in message["trustees"]]
        self.guardian_ids = set(guardian_ids)
        self.order = guardian_ids.index(guardian_id)
        self.quorum = message["scheme"]["parameters"]["quorum"]


class ProcessTrusteeElectionKeys(ElectionStep):
    message_type = "trustee_election_keys"

    def process_message(self, message_type: str, message: dict, context: Context):
        if message['owner_id'] == context.guardian_id:
            return

        context.guardian.save_guardian_public_keys(deserialize(message, PublicKeySet))

        if context.guardian.all_public_keys_received():
            context.guardian.generate_election_partial_key_backups()
            self.next_step = ProcessTrusteesPartialElectionKey()

            return [
                serialize(context.guardian.share_election_partial_key_backup(guardian_id))
                for guardian_id in context.guardian_ids
                if context.guardian_id != guardian_id
            ]


class ProcessTrusteesPartialElectionKey(ElectionStep):
    message_type = "trustee_partial_election_key"

    def process_message(self, message_type: str, message: dict, context: Context):
        if message[0]['owner_id'] == context.guardian_id:
            return

        for partial_keys_backup in message:
            if partial_keys_backup['designated_id'] == context.guardian_id:
                context.guardian.save_election_partial_key_backup(deserialize(partial_keys_backup, ElectionPartialKeyBackup))

        if context.guardian.all_election_partial_key_backups_received():
            self.next_step = VerifyTrusteesStep()

            # TODO: check that verifications are OK

            return [
                serialize(context.guardian.verify_election_partial_key_backup(guardian_id))
                for guardian_id in context.guardian_ids
                if context.guardian_id != guardian_id
            ]


class VerifyTrusteesStep(ElectionStep):
    pending_verifications: Set[str] = None

    message_type = "verify_trustee"

    def process_message(self, message_type: str, message: dict, context: Context):
        if message[0]['verifier_id'] == context.guardian_id:
            return

        self.pending_verifications = self.pending_verifications or {context.guardian_id}
        self.pending_verifications.add(message[0]['verifier_id'])

        # TODO: everything should be ok
        if context.guardian_ids == self.pending_verifications:
            self.next_step = ProcessJointElectionKey()


class ProcessJointElectionKey(ElectionStep):
    message_type = 'joint_election_key'

    def process_message(self, message_type: str, message: dict, context: Context):
        # TODO: check joint key but don't use private variables
        # serialize(elgamal_combine_public_keys(context.guardian._guardian_election_public_keys.values()))
        pass


class Trustee(Wrapper):
    def __init__(self, guardian_id: str) -> None:
        super().__init__(TrusteeContext(guardian_id), ProcessCreateElection())

    def backup(self) -> dict:
        return dumps(self)

    def restore(backup: dict):
        return loads(backup)
