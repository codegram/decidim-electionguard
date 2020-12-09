import unittest
from electionguard.elgamal import elgamal_combine_public_keys
from decidim.electionguard.trustee import Trustee
from decidim.electionguard.utils import serialize, deserialize_key
from .utils import create_election_test_message


class TestTrustee(unittest.TestCase):
    def setUp(self):
        self.trustees = [Trustee('alicia'), Trustee('bob'), Trustee('clara')]

    def test_key_ceremony(self):
        trustees_public_keys = [
            trustee.process_message('create_election', create_election_test_message())
            for trustee in self.trustees
        ]

        print('\n---- PUBLIC KEYS ----')
        print(repr(trustees_public_keys))
        print('---- END PUBLIC KEYS ----\n')

        trustees_partial_public_keys = list(filter(None, [
            trustee.process_message('trustee_election_keys', public_keys)
            for public_keys in trustees_public_keys
            for trustee in self.trustees
        ]))

        print('\n---- PARTIAL PUBLIC KEYS ----')
        print(repr(trustees_partial_public_keys))
        print('---- END PARTIAL PUBLIC KEYS ----\n')

        trustees_verifications = list(filter(None, [
            trustee.process_message('trustee_partial_election_keys', partial_public_keys)
            for partial_public_keys in trustees_partial_public_keys
            for trustee in self.trustees
        ]))

        print('\n---- VERIFICATIONS ----')
        print(repr(trustees_verifications))
        print('---- END VERIFICATIONS ----\n')

        # Process verifications results
        for verification in trustees_verifications:
            for trustee in self.trustees:
                trustee.process_message('trustee_verification', verification)

        # Simulate the message from the Bulletin Board
        joint_election_key = serialize({
            'joint_election_key': elgamal_combine_public_keys(
                deserialize_key(public_keys['election_public_key'])
                for public_keys in trustees_public_keys
            )
        })

        for trustee in self.trustees:
            print(repr(trustee.process_message('joint_election_key', joint_election_key)))

        # TODO: assert ballot keys
        # TODO: assert ballot constests keys
        # TODO: assert ballot selections keys
        # TODO: assert nonces removal
        # TODO: assert number of selections for each contest
        # TODO: assert decryption of the ballot

    def test_restore(self):
        pass
        # TODO: backup and restore a trustee between each step

        # self.trustee = Trustee.restore(trustee_backup())
        # print(trustee_public_keys)


if __name__ == '__main__':
    unittest.main()
