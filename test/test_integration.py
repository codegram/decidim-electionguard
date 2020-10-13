from random import choice, sample
import unittest
from .utils import create_election_test_message
from decidim.electionguard.bulletin_board import BulletinBoard
from decidim.electionguard.trustee import Trustee
from decidim.electionguard.voter import Voter


NUMBER_OF_VOTERS = 10


class TestIntegration(unittest.TestCase):
    def test_complete(self):
        self.configure_election()
        self.key_ceremony()
        self.encrypt_ballots()
        self.cast_votes()
        self.decrypt_tally()
        self.publish_and_verify()

    def configure_election(self):
        self.election_message = create_election_test_message()
        self.bulletin_board = BulletinBoard()
        self.trustees = [Trustee('alicia'), Trustee('bob'), Trustee('clara')]
        self.voters = [
            Voter(f'the-voter-{i}')
            for i in range(1, NUMBER_OF_VOTERS)
        ]

    def key_ceremony(self):
        self.bulletin_board.process_message('create_election', self.election_message)

        trustees_public_keys = [
            trustee.process_message('create_election', self.election_message)
            for trustee in self.trustees
        ]

        for public_keys in trustees_public_keys:
            self.bulletin_board.process_message('trustee_election_keys', public_keys)

        print('\n---- PUBLIC KEYS ----')
        print(repr(trustees_public_keys))
        print('---- END PUBLIC KEYS ----\n')

        trustees_partial_public_keys = list(filter(None, [
            trustee.process_message('trustee_election_keys', public_keys)
            for public_keys in trustees_public_keys
            for trustee in self.trustees
            if trustee.context.guardian_id != public_keys['owner_id']
        ]))

        for partial_public_keys in trustees_partial_public_keys:
            self.bulletin_board.process_message('trustee_partial_election_key', partial_public_keys)

        print('\n---- PARTIAL PUBLIC KEYS ----')
        print(repr(trustees_partial_public_keys))
        print('---- END PARTIAL PUBLIC KEYS ----\n')

        trustees_verifications = list(filter(None, [
            trustee.process_message('trustee_partial_election_key', partial_public_keys)
            for partial_public_keys in trustees_partial_public_keys
            for trustee in self.trustees
            if trustee.context.guardian_id != partial_public_keys['guardian_id']
        ]))

        for trustee_verifications in trustees_verifications:
            self.joint_election_key = self.bulletin_board.process_message('trustee_verification', trustee_verifications)

        print('\n---- VERIFICATIONS ----')
        print(repr(trustees_verifications))
        print('---- END VERIFICATIONS ----\n')

        # Process verifications results
        for verification in trustees_verifications:
            for trustee in self.trustees:
                if trustee.context.guardian_id != verification['guardian_id']:
                    trustee.process_message('trustee_verification', verification)

        for trustee in self.trustees:
            trustee.process_message('joint_election_key', self.joint_election_key)

        print('\n---- JOINT ELECTION KEY ----')
        print(repr(self.joint_election_key))
        print('---- JOINT ELECTION KEY ----\n')

    def encrypt_ballots(self):
        possible_answers = [
            {
                'object_id': contest['object_id'],
                'number': range(contest['minimum_elected'], contest['number_elected']+1),
                'selections': [selection['object_id'] for selection in contest['ballot_selections']]
            }
            for contest in self.election_message['description']['contests']
        ]

        self.encrypted_ballots = []
        for voter in self.voters:
            voter.process_message('create_election', self.election_message)
            voter.process_message('joint_election_key', self.joint_election_key)

            ballot = dict(
                (contest['object_id'], sample(contest['selections'], choice(contest['number'])))
                for contest in possible_answers
            )

            print(ballot)

            self.encrypted_ballots.append(voter.encrypt(ballot))

    def cast_votes(self):
        print('\n---- BALLOT BOX OPEN ----')
        self.bulletin_board.open_ballot_box()

        self.accepted_ballots = list(filter(
            lambda ballot: self.bulletin_board.process_message('cast_vote', ballot),
            self.encrypted_ballots
        ))

        self.bulletin_board.close_ballot_box()
        print('---- BALLOT BOX CLOSED ----\n')

    def decrypt_tally(self):
        for ballot in self.accepted_ballots:
            self.bulletin_board.add_ballot(ballot)

        tally_cast = self.bulletin_board.get_tally_cast()

        print('\n---- TALLY CAST ----')
        print(repr(tally_cast))
        print('---- TALLY CAST ----\n')

        trustees_shares = [
            trustee.process_message('tally_cast', tally_cast)
            for trustee in self.trustees
        ]

        print('\n---- TRUSTEE SHARES ----')
        print(repr(trustees_shares))
        print('---- TRUSTEE SHARES ----\n')

        for share in trustees_shares:
            results = self.bulletin_board.process_message('trustee_share', share)

        print('\n---- RESULTS ----')
        print(repr(results))
        print('---- RESULTS ----\n')

        for question_id, question in results.items():
            print(f'Question {question_id}:')
            for selection_id, selection in question['selections'].items():
                print(f'Option {selection_id}: ' + str(selection['tally']))

    def publish_and_verify(self):
        # see publish.py
        pass


if __name__ == '__main__':
    unittest.main()
