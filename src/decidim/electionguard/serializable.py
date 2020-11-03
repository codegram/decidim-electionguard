from base64 import b64encode, b64decode
from electionguard.group import ElementModP, ElementModQ
import electionguard.serializable
from gmpy2 import mpz


old_set_serializers = electionguard.serializable.set_serializers
old_set_deserializers = electionguard.serializable.set_deserializers


def monkey_patch_serialization():
    electionguard.serializable.set_serializers = set_serializers
    electionguard.serializable.set_deserializers = set_deserializers
    electionguard.serializable.KEYS_TO_REMOVE += ['nonce']  # Remove nonces when serializing to JSON


def set_serializers():
    old_set_serializers()
    electionguard.serializable.set_serializer(serialize_big_number, ElementModP)
    electionguard.serializable.set_serializer(serialize_big_number, ElementModQ)


def set_deserializers():
    old_set_serializers()
    electionguard.serializable.set_deserializer(deserialize_big_number, ElementModP)
    electionguard.serializable.set_deserializer(deserialize_big_number, ElementModQ)


def serialize_big_number(obj: object, **_):
    number = int(obj.to_int())
    return b64encode(
        number.to_bytes(
            (number.bit_length() + 7) // 8,
            byteorder='big'
        )
    ).decode('utf-8')


def deserialize_big_number(obj, cls, **_):
    return cls(mpz(int.from_bytes(b64decode(obj), byteorder='big')))
