from collections import defaultdict
from electionguard.ballot import CiphertextBallot, from_ciphertext_ballot, BallotBoxState
from electionguard.ballot_validator import ballot_is_valid_for_election
from electionguard.decryption_share import CiphertextDecryptionSelection
from electionguard.decrypt_with_shares import decrypt_selection_with_decryption_shares
from electionguard.elgamal import elgamal_combine_public_keys
from electionguard.group import ElementModP
from electionguard.tally import CiphertextTally, tally_ballot, PlaintextTallyContest, PlaintextTallySelection
from electionguard.types import CONTEST_ID, GUARDIAN_ID, SELECTION_ID
from electionguard.utils import get_optional
from typing import Dict, Set
from .common import Context, ElectionStep, Wrapper
from .utils import (
  MissingJointKey, pair_with_object_id,
  serialize, deserialize, deserialize_key
)


class BulletinBoardContext(Context):
    public_keys: Dict[str, ElementModP]
    has_joint_key: bool
    tally: CiphertextTally
    shares: Dict[GUARDIAN_ID, Dict]

    def __init__(self):
        self.public_keys = {}
        self.has_joint_key = False
        self.shares = {}


class ProcessCreateElection(ElectionStep):
    message_type = 'create_election'

    def process_message(self, message_type: str, message: dict, context: Context):
        context.build_election(message)
        self.next_step = ProcessTrusteeElectionKeys()


class ProcessTrusteeElectionKeys(ElectionStep):
    message_type = 'trustee_election_keys'

    def process_message(self, message_type: str, message: dict, context: Context):
        guardian_id, guardian_public_key = self.parse_trustee_public_keys(message)
        context.public_keys[guardian_id] = guardian_public_key
        # TO-DO: verify keys?

        if len(context.public_keys) == context.number_of_guardians:
            self.next_step = ProcessTrusteeElectionPartialKey()

    def parse_trustee_public_keys(self, message: dict):
        return (message['owner_id'], deserialize_key(message['election_public_key']))


class ProcessTrusteeElectionPartialKey(ElectionStep):
    message_type = 'trustee_partial_election_key'

    partial_keys_received: Set[str] = set()

    def process_message(self, message_type: str, message: dict, context: Context):
        self.partial_keys_received.add(message['owner_id'])
        # TO-DO: verify partial keys?

        if len(self.partial_keys_received) == context.number_of_guardians:
            self.next_step = ProcessTrusteeVerification()


class ProcessTrusteeVerification(ElectionStep):
    message_type = 'trustee_verification'

    verification_received: Set[str] = set()

    def process_message(self, message_type: str, message: dict, context: Context):
        self.verification_received.add(message['owner_id'])
        # TO-DO: check verifications?

        if len(self.verification_received) == context.number_of_guardians:
            joint_key = elgamal_combine_public_keys(context.public_keys.values())
            context.election_builder.set_public_key(get_optional(joint_key))
            context.election_metadata, context.election_context = get_optional(context.election_builder.build())
            context.has_joint_key = True
            return {'joint_election_key': serialize(joint_key)}


class ProcessCastVote(ElectionStep):
    message_type = 'cast_vote'

    def process_message(self, message_type: str, message: dict, context: Context):
        ballot = deserialize(message, CiphertextBallot)
        return ballot_is_valid_for_election(ballot, context.election_metadata, context.election_context)


class ProcessTrusteePartialDecrypt(ElectionStep):
    message_type = 'trustee_partial_decrypt'

    def process_message(self, message_type: str, message: dict, context: Context):
        context.shares[message['guardian_id']] = message
        if len(context.shares) == context.number_of_guardians:
            tally_shares = self._prepare_shares_for_decryption(context.shares)

            results: Dict[CONTEST_ID, PlaintextTallyContest] = {}

            for contest in context.tally.cast.values():
                selections: Dict[SELECTION_ID, PlaintextTallySelection] = dict(
                    pair_with_object_id(decrypt_selection_with_decryption_shares(
                      selection,
                      tally_shares[selection.object_id],
                      context.election_context.crypto_extended_base_hash
                    ))
                    for selection in contest.tally_selections.values()
                )

                results[contest.object_id] = PlaintextTallyContest(
                    contest.object_id, selections
                )

            return serialize(results)

    def _prepare_shares_for_decryption(self, tally_shares):
        shares = defaultdict(dict)
        for guardian_id, share in tally_shares.items():
            for question_id, question in share['contests'].items():
                for selection_id, selection in question['selections'].items():
                    shares[selection_id][guardian_id] = (
                      deserialize_key(share['public_key']),
                      deserialize(selection, CiphertextDecryptionSelection)
                    )
        return shares


class BulletinBoard(Wrapper):
    def __init__(self) -> None:
        super().__init__(BulletinBoardContext(), ProcessCreateElection())

    def open_ballot_box(self):
        if not self.context.has_joint_key:
            raise MissingJointKey()

        self.step = ProcessCastVote()

    def close_ballot_box(self):
        self.context.tally = CiphertextTally('election-results', self.context.election_metadata, self.context.election_context)
        self.step = ProcessTrusteePartialDecrypt()

    def add_ballot(self, ballot: dict):
        ciphertext_ballot = deserialize(ballot, CiphertextBallot)
        # TODO: remove the dependency of multiprocessing
        tally_ballot(from_ciphertext_ballot(ciphertext_ballot, BallotBoxState.CAST), self.context.tally)

    def get_tally_cast(self):
        return serialize(self.context.tally.cast)
