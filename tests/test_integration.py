import unittest
from random import choice, sample
from decidim.electionguard.bulletin_board import BulletinBoard
from decidim.electionguard.trustee import Trustee
from decidim.electionguard.voter import Voter
from decidim.electionguard.utils import InvalidBallot
from .utils import create_election_test_message, open_ballot_box_message, close_ballot_box_message


NUMBER_OF_VOTERS = 10


class TestIntegration(unittest.TestCase):
    def test_complete(self):
        self.reset_state = False
        self.show_output = True
        self.configure_election()
        self.key_ceremony()
        self.encrypt_ballots()
        self.cast_votes()
        self.decrypt_tally()
        self.publish_and_verify()

    def test_without_state(self):
        self.reset_state = True
        self.show_output = False
        self.configure_election()
        self.key_ceremony()
        self.encrypt_ballots()
        self.cast_votes()
        self.decrypt_tally()
        self.publish_and_verify()

    def checkpoint(self, step, output=None):
        if self.show_output:
            if output:
                print('\n____ ' + step + ' ____')
                print(repr(output))
                print('‾‾‾‾ ' + step + ' ‾‾‾‾')
            else:
                print('\n---- ' + step + ' ----')

        if self.reset_state:
            self.bulletin_board = self.bulletin_board.backup()
            self.trustees = [trustee.backup() for trustee in self.trustees]
            self.bulletin_board = BulletinBoard.restore(self.bulletin_board)
            self.trustees = [Trustee.restore(trustee) for trustee in self.trustees]

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

        self.checkpoint("CREATE ELECTION")

        for public_keys in trustees_public_keys:
            self.bulletin_board.process_message('trustee_election_keys', public_keys)

        trustees_partial_public_keys = list(filter(None, [
            trustee.process_message('trustee_election_keys', public_keys)
            for public_keys in trustees_public_keys
            for trustee in self.trustees
        ]))

        self.checkpoint("PUBLIC KEYS", trustees_public_keys)

        for partial_public_keys in trustees_partial_public_keys:
            self.bulletin_board.process_message('trustee_partial_election_keys', partial_public_keys)

        trustees_verifications = list(filter(None, [
            trustee.process_message('trustee_partial_election_keys', partial_public_keys)
            for partial_public_keys in trustees_partial_public_keys
            for trustee in self.trustees
        ]))

        self.checkpoint("PARTIAL PUBLIC KEYS", trustees_partial_public_keys)

        for trustee_verifications in trustees_verifications:
            self.joint_election_key = self.bulletin_board.process_message('trustee_verification', trustee_verifications)

        for verification in trustees_verifications:
            for trustee in self.trustees:
                trustee.process_message('trustee_verification', verification)

        self.checkpoint("VERIFICATIONS", trustees_verifications)

        for trustee in self.trustees:
            trustee.process_message('joint_election_key', self.joint_election_key)

        self.checkpoint("JOINT ELECTION KEY", self.joint_election_key)

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
            voter.process_message('open_ballot_box', open_ballot_box_message())

            ballot = dict(
                (contest['object_id'], sample(contest['selections'], choice(contest['number'])))
                for contest in possible_answers
            )
            self.encrypted_ballots.append(voter.encrypt(ballot))

        voter = Voter('a-voter')
        voter.process_message('create_election', self.election_message)
        voter.process_message('joint_election_key', self.joint_election_key)
        voter.process_message('open_ballot_box', open_ballot_box_message())
        encrypted_ballot = voter.encrypt(ballot, True)
        self.encrypted_ballots.append(encrypted_ballot)

    def cast_votes(self):
        self.bulletin_board.process_message('open_ballot_box', open_ballot_box_message())
        self.checkpoint("OPEN BALLOT BOX")

        self.accepted_ballots = []

        for encrypted_ballot in self.encrypted_ballots:
            try:
                self.bulletin_board.process_message('cast_vote', encrypted_ballot)
                self.accepted_ballots.append(encrypted_ballot)
                self.checkpoint("BALLOT ACCEPTED " + encrypted_ballot["object_id"], encrypted_ballot)
            except InvalidBallot:
                self.checkpoint("BALLOT REJECTED " + encrypted_ballot["object_id"])

        self.bulletin_board.process_message('close_ballot_box', close_ballot_box_message())
        self.checkpoint("CLOSE BALLOT BOX")

    def decrypt_tally(self):
        for ballot in self.accepted_ballots:
            self.bulletin_board.add_ballot(ballot)

        tally_cast = self.bulletin_board.get_tally_cast()

        self.checkpoint("TALLY CAST", tally_cast)

        trustees_shares = [
            trustee.process_message('tally_cast', tally_cast)
            for trustee in self.trustees
        ]

        self.checkpoint("TRUSTEE SHARES", trustees_shares)

        for share in trustees_shares:
            results = self.bulletin_board.process_message('trustee_share', share)

        self.checkpoint("RESULTS", results)

        if self.show_output:
            for question_id, question in results.items():
                print(f'Question {question_id}:')
                for selection_id, selection in question['selections'].items():
                    print(f'Option {selection_id}: ' + str(selection['tally']))

    def publish_and_verify(self):
        # see publish.py
        pass


if __name__ == '__main__':
    unittest.main()
