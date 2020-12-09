import unittest
from decidim.electionguard.bulletin_board import BulletinBoard
from .utils import create_election_test_message, trustees_public_keys


class TestBulletinBoard(unittest.TestCase):
    def setUp(self):
        self.bulletin_board = BulletinBoard()

    def test_key_ceremony(self):
        election_message = create_election_test_message()
        self.bulletin_board.process_message('create_election', election_message)

        for public_keys in trustees_public_keys():
            self.bulletin_board.process_message('trustee_election_keys', public_keys)

        for trustee in election_message['trustees']:
            self.bulletin_board.process_message('trustee_partial_election_keys', {'guardian_id': trustee['name']})

        for trustee in election_message['trustees']:
            joint_key = self.bulletin_board.process_message('trustee_verification', {'guardian_id': trustee['name']})

        print(joint_key)

        # TODO: assert ballot keys
        # TODO: assert ballot constests keys
        # TODO: assert ballot selections keys
        # TODO: assert nonces removal
        # TODO: assert number of selections for each contest
        # TODO: assert decryption of the ballot


if __name__ == '__main__':
    unittest.main()
