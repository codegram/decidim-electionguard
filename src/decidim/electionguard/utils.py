from jsons import dumps, set_serializer
from base64 import b64encode
from datetime import datetime
from electionguard.group import ElementModP, ElementModQ
import electionguard.serializable

# -- TEMPORARY MONKEYPATCH JSONS SERIALIZATION --
old_set_serializers = electionguard.serializable.set_serializers
electionguard.serializable.KEYS_TO_REMOVE += ['nonce'] # Remove nonces when serializing to JSON

def set_serializers():
  old_set_serializers()
  electionguard.serializable.set_serializer(serialize_big_number, ElementModP)
  electionguard.serializable.set_serializer(serialize_big_number, ElementModQ)

electionguard.serializable.set_serializers = set_serializers

def serialize_big_number(obj: object, **_):
  number = int(obj.to_int())
  return b64encode(
    number.to_bytes(
      (number.bit_length() + 7) // 8,
      byteorder='little'
    )
  ).decode("utf-8")
# -----------------------------------------------

def serialize(obj):
  return electionguard.serializable.write_json(obj, True)

def complete_election_description(election_description: dict) -> dict:
  complete_description = {
    **election_description,
    "contact_information": {
      "address_line": [],
      "name": "Organization name",
      "email": [{ "annotation": "contact", "value": "contact@example.org" }],
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
          "email": [{ "annotation": "contact", "value": "contact@example.org" }]
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
