from electionguard.decryption import compute_decryption_share_for_selection
from electionguard.decryption_share import CiphertextDecryptionContest, CiphertextDecryptionSelection
from electionguard.election import CiphertextElectionContext, ElectionDescription, InternalElectionDescription
from electionguard.election_builder import ElectionBuilder
from electionguard.key_ceremony import PublicKeySet, ElectionPartialKeyBackup
from electionguard.guardian import Guardian
from electionguard.tally import CiphertextTallyContest
from electionguard.types import CONTEST_ID, SELECTION_ID
from electionguard.utils import get_optional
from pickle import loads, dumps
from typing import Dict, Set
from .common import Context, ElectionStep, Wrapper
from .utils import (
  InvalidElectionDescription,
  complete_election_description, pair_with_object_id,
  serialize, deserialize, deserialize_key
)


class TrusteeContext(Context):
    election: ElectionDescription
    election_builder: ElectionBuilder
    election_metadata: InternalElectionDescription
    election_context: CiphertextElectionContext
    guardian: Guardian
    guardian_id: str
    guardian_ids: Set[str]

    def __init__(self, guardian_id: str) -> None:
        self.guardian_id = guardian_id


class ProcessCreateElection(ElectionStep):
    order: int
    guardian_ids: Set[str]
    quorum: int
    election_description: dict

    message_type = 'create_election'

    def process_message(self, message_type: str, message: dict, context: Context):
        self.parse_create_election_message(context.guardian_id, message)

        context.election = ElectionDescription.from_json_object(complete_election_description(self.election_description))
        if not context.election.is_valid():
            raise InvalidElectionDescription()

        context.election_builder = ElectionBuilder(len(self.guardian_ids), self.quorum, context.election)

        context.guardian_ids = self.guardian_ids
        context.guardian = Guardian(context.guardian_id, self.order, len(self.guardian_ids), self.quorum)

        self.next_step = ProcessTrusteeElectionKeys()

        public_keys = context.guardian.share_public_keys()

        return serialize(public_keys)

    def parse_create_election_message(self, guardian_id: int, message: dict):
        guardian_ids = [trustee['name'] for trustee in message['trustees']]
        self.guardian_ids = set(guardian_ids)
        self.order = guardian_ids.index(guardian_id)
        self.quorum = message['scheme']['parameters']['quorum']
        self.election_description = message['description']


class ProcessTrusteeElectionKeys(ElectionStep):
    message_type = 'trustee_election_keys'

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
    message_type = 'trustee_partial_election_key'

    def process_message(self, message_type: str, message: dict, context: Context):
        if message[0]['owner_id'] == context.guardian_id:
            return

        for partial_keys_backup in message:
            if partial_keys_backup['designated_id'] == context.guardian_id:
                context.guardian.save_election_partial_key_backup(deserialize(partial_keys_backup, ElectionPartialKeyBackup))

        if context.guardian.all_election_partial_key_backups_received():
            self.next_step = ProcessTrusteeVerification()

            # TODO: check that verifications are OK

            return [
                serialize(context.guardian.verify_election_partial_key_backup(guardian_id))
                for guardian_id in context.guardian_ids
                if context.guardian_id != guardian_id
            ]


class ProcessTrusteeVerification(ElectionStep):
    pending_verifications: Set[str] = None

    message_type = 'trustee_verification'

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
        joint_key = deserialize_key(message['joint_election_key'])
        context.election_builder.set_public_key(get_optional(joint_key))
        context.election_metadata, context.election_context = get_optional(context.election_builder.build())
        # TODO: coefficient validation keys???
        # TODO: check joint key, without using private variables if possible
        #         serialize(elgamal_combine_public_keys(context.guardian._guardian_election_public_keys.values()))
        self.next_step = ProcessStartDecrypt()


class ProcessStartDecrypt(ElectionStep):
    message_type = 'start_decrypt'

    def process_message(self, message_type: str, message: dict, context: Context):
        contests: Dict[CONTEST_ID, CiphertextDecryptionContest] = {}

        tally_cast: Dict[CONTEST_ID, CiphertextTallyContest] = deserialize(message, Dict[CONTEST_ID, CiphertextTallyContest])

        for contest in tally_cast.values():
            selections: Dict[SELECTION_ID, CiphertextDecryptionSelection] = dict(
              pair_with_object_id(
                  compute_decryption_share_for_selection(context.guardian, selection, context.election_context)
              )
              for (_, selection) in contest.tally_selections.items()
            )

            contests[contest.object_id] = CiphertextDecryptionContest(
                contest.object_id, context.guardian_id, contest.description_hash, selections
            )

        return serialize({
            'guardian_id': context.guardian_id,
            'public_key': context.guardian.share_election_public_key().key,
            'contests': contests
        })


class Trustee(Wrapper):
    def __init__(self, guardian_id: str) -> None:
        super().__init__(TrusteeContext(guardian_id), ProcessCreateElection())

    def backup(self) -> dict:
        return dumps(self)

    def restore(backup: dict):
        return loads(backup)
