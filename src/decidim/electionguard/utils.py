from base64 import b64encode, b64decode
from electionguard.group import ElementModP, ElementModQ
import electionguard.serializable
from gmpy2 import mpz


# -- TEMPORARY MONKEYPATCH JSONS SERIALIZATION --
old_set_serializers = electionguard.serializable.set_serializers
old_set_deserializers = electionguard.serializable.set_deserializers
electionguard.serializable.KEYS_TO_REMOVE += ['nonce']  # Remove nonces when serializing to JSON


def set_serializers():
    old_set_serializers()
    electionguard.serializable.set_serializer(serialize_big_number, ElementModP)
    electionguard.serializable.set_serializer(serialize_big_number, ElementModQ)


def set_deserializers():
    old_set_serializers()
    electionguard.serializable.set_deserializer(deserialize_big_number, ElementModP)
    electionguard.serializable.set_deserializer(deserialize_big_number, ElementModQ)


electionguard.serializable.set_serializers = set_serializers
electionguard.serializable.set_deserializers = set_deserializers
# -----------------------------------------------


def serialize_big_number(obj: object, **_):
    number = int(obj.to_int())
    return b64encode(
        number.to_bytes(
            (number.bit_length() + 7) // 8,
            byteorder='little'
        )
    ).decode("utf-8")


def deserialize_big_number(obj, cls, **_):
    return cls(mpz(int.from_bytes(b64decode(obj), byteorder='little')))


def serialize(obj, include_private: bool = False):
    return electionguard.serializable.write_json_object(obj, not include_private)


def deserialize(obj, type):
    return electionguard.serializable.read_json_object(obj, type)


def deserialize_key(obj):
    return deserialize_big_number(obj, ElementModP)


class InvalidElectionDescription(Exception):
    """Exception raised when the election description is invalid."""
    pass


def complete_election_description(election_description: dict) -> dict:
    complete_description = {
        **election_description,
        "contact_information": {
            "address_line": [],
            "name": "Organization name",
            "email": [{"annotation": "contact", "value": "contact@example.org"}],
            "phone": []
        },
        "election_scope_id": "test-election",
        "type": "special",
        "geopolitical_units": [
            {
                "object_id": "a-place",
                "name": "A place",
                "type": "county",
                "contact_information": {
                    "address_line": [],
                    "name": "Organization name",
                    "email": [{"annotation": "contact", "value": "contact@example.org"}]
                },
                "phone": []
            }
        ],
        "parties": [],
        "ballot_styles": [
            {
                "object_id": "ballot-style",
                "geopolitical_unit_ids": ["a-place"]
            }
        ]
    }

    for contest in complete_description["contests"]:
        contest["electoral_district_id"] = "a-place"

    return complete_description
