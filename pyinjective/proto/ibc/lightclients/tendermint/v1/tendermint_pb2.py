# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/lightclients/tendermint/v1/tendermint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tendermint.types import validator_pb2 as tendermint_dot_types_dot_validator__pb2
from tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from cosmos.ics23.v1 import proofs_pb2 as cosmos_dot_ics23_dot_v1_dot_proofs__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from ibc.core.commitment.v1 import commitment_pb2 as ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/ibc/lightclients/tendermint/v1/tendermint.proto\x12\x1eibc.lightclients.tendermint.v1\x1a tendermint/types/validator.proto\x1a\x1ctendermint/types/types.proto\x1a\x1c\x63osmos/ics23/v1/proofs.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\'ibc/core/commitment/v1/commitment.proto\x1a\x14gogoproto/gogo.proto\"\xb2\x04\n\x0b\x43lientState\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\x12\x43\n\x0btrust_level\x18\x02 \x01(\x0b\x32(.ibc.lightclients.tendermint.v1.FractionB\x04\xc8\xde\x1f\x00\x12<\n\x0ftrusting_period\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12=\n\x10unbonding_period\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12<\n\x0fmax_clock_drift\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x37\n\rfrozen_height\x18\x06 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12\x37\n\rlatest_height\x18\x07 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12/\n\x0bproof_specs\x18\x08 \x03(\x0b\x32\x1a.cosmos.ics23.v1.ProofSpec\x12\x14\n\x0cupgrade_path\x18\t \x03(\t\x12%\n\x19\x61llow_update_after_expiry\x18\n \x01(\x08\x42\x02\x18\x01\x12+\n\x1f\x61llow_update_after_misbehaviour\x18\x0b \x01(\x08\x42\x02\x18\x01:\x04\x88\xa0\x1f\x00\"\xdb\x01\n\x0e\x43onsensusState\x12\x37\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x36\n\x04root\x18\x02 \x01(\x0b\x32\".ibc.core.commitment.v1.MerkleRootB\x04\xc8\xde\x1f\x00\x12R\n\x14next_validators_hash\x18\x03 \x01(\x0c\x42\x34\xfa\xde\x1f\x30github.com/cometbft/cometbft/libs/bytes.HexBytes:\x04\x88\xa0\x1f\x00\"\xb9\x01\n\x0cMisbehaviour\x12\x15\n\tclient_id\x18\x01 \x01(\tB\x02\x18\x01\x12\x45\n\x08header_1\x18\x02 \x01(\x0b\x32&.ibc.lightclients.tendermint.v1.HeaderB\x0b\xe2\xde\x1f\x07Header1\x12\x45\n\x08header_2\x18\x03 \x01(\x0b\x32&.ibc.lightclients.tendermint.v1.HeaderB\x0b\xe2\xde\x1f\x07Header2:\x04\x88\xa0\x1f\x00\"\xf2\x01\n\x06Header\x12;\n\rsigned_header\x18\x01 \x01(\x0b\x32\x1e.tendermint.types.SignedHeaderB\x04\xd0\xde\x1f\x01\x12\x35\n\rvalidator_set\x18\x02 \x01(\x0b\x32\x1e.tendermint.types.ValidatorSet\x12\x38\n\x0etrusted_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12:\n\x12trusted_validators\x18\x04 \x01(\x0b\x32\x1e.tendermint.types.ValidatorSet\"2\n\x08\x46raction\x12\x11\n\tnumerator\x18\x01 \x01(\x04\x12\x13\n\x0b\x64\x65nominator\x18\x02 \x01(\x04\x42LZJgithub.com/cosmos/ibc-go/v8/modules/light-clients/07-tendermint;tendermintb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.tendermint.v1.tendermint_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgithub.com/cosmos/ibc-go/v8/modules/light-clients/07-tendermint;tendermint'
  _CLIENTSTATE.fields_by_name['trust_level']._options = None
  _CLIENTSTATE.fields_by_name['trust_level']._serialized_options = b'\310\336\037\000'
  _CLIENTSTATE.fields_by_name['trusting_period']._options = None
  _CLIENTSTATE.fields_by_name['trusting_period']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _CLIENTSTATE.fields_by_name['unbonding_period']._options = None
  _CLIENTSTATE.fields_by_name['unbonding_period']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _CLIENTSTATE.fields_by_name['max_clock_drift']._options = None
  _CLIENTSTATE.fields_by_name['max_clock_drift']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _CLIENTSTATE.fields_by_name['frozen_height']._options = None
  _CLIENTSTATE.fields_by_name['frozen_height']._serialized_options = b'\310\336\037\000'
  _CLIENTSTATE.fields_by_name['latest_height']._options = None
  _CLIENTSTATE.fields_by_name['latest_height']._serialized_options = b'\310\336\037\000'
  _CLIENTSTATE.fields_by_name['allow_update_after_expiry']._options = None
  _CLIENTSTATE.fields_by_name['allow_update_after_expiry']._serialized_options = b'\030\001'
  _CLIENTSTATE.fields_by_name['allow_update_after_misbehaviour']._options = None
  _CLIENTSTATE.fields_by_name['allow_update_after_misbehaviour']._serialized_options = b'\030\001'
  _CLIENTSTATE._options = None
  _CLIENTSTATE._serialized_options = b'\210\240\037\000'
  _CONSENSUSSTATE.fields_by_name['timestamp']._options = None
  _CONSENSUSSTATE.fields_by_name['timestamp']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _CONSENSUSSTATE.fields_by_name['root']._options = None
  _CONSENSUSSTATE.fields_by_name['root']._serialized_options = b'\310\336\037\000'
  _CONSENSUSSTATE.fields_by_name['next_validators_hash']._options = None
  _CONSENSUSSTATE.fields_by_name['next_validators_hash']._serialized_options = b'\372\336\0370github.com/cometbft/cometbft/libs/bytes.HexBytes'
  _CONSENSUSSTATE._options = None
  _CONSENSUSSTATE._serialized_options = b'\210\240\037\000'
  _MISBEHAVIOUR.fields_by_name['client_id']._options = None
  _MISBEHAVIOUR.fields_by_name['client_id']._serialized_options = b'\030\001'
  _MISBEHAVIOUR.fields_by_name['header_1']._options = None
  _MISBEHAVIOUR.fields_by_name['header_1']._serialized_options = b'\342\336\037\007Header1'
  _MISBEHAVIOUR.fields_by_name['header_2']._options = None
  _MISBEHAVIOUR.fields_by_name['header_2']._serialized_options = b'\342\336\037\007Header2'
  _MISBEHAVIOUR._options = None
  _MISBEHAVIOUR._serialized_options = b'\210\240\037\000'
  _HEADER.fields_by_name['signed_header']._options = None
  _HEADER.fields_by_name['signed_header']._serialized_options = b'\320\336\037\001'
  _HEADER.fields_by_name['trusted_height']._options = None
  _HEADER.fields_by_name['trusted_height']._serialized_options = b'\310\336\037\000'
  _globals['_CLIENTSTATE']._serialized_start=339
  _globals['_CLIENTSTATE']._serialized_end=901
  _globals['_CONSENSUSSTATE']._serialized_start=904
  _globals['_CONSENSUSSTATE']._serialized_end=1123
  _globals['_MISBEHAVIOUR']._serialized_start=1126
  _globals['_MISBEHAVIOUR']._serialized_end=1311
  _globals['_HEADER']._serialized_start=1314
  _globals['_HEADER']._serialized_end=1556
  _globals['_FRACTION']._serialized_start=1558
  _globals['_FRACTION']._serialized_end=1608
# @@protoc_insertion_point(module_scope)
