# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/events.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/bank/v1beta1/events.proto\x12\x13\x63osmos.bank.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x11\x61mino/amino.proto\"O\n\x10\x45ventSetBalances\x12;\n\x0f\x62\x61lance_updates\x18\x01 \x03(\x0b\x32\".cosmos.bank.v1beta1.BalanceUpdate\"|\n\rBalanceUpdate\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\x0c\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\x0c\x12N\n\x03\x61mt\x18\x03 \x01(\tBA\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int\xa8\xe7\xb0*\x01\x42+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
  _globals['_BALANCEUPDATE'].fields_by_name['amt']._loaded_options = None
  _globals['_BALANCEUPDATE'].fields_by_name['amt']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\322\264-\ncosmos.Int\250\347\260*\001'
  _globals['_EVENTSETBALANCES']._serialized_start=125
  _globals['_EVENTSETBALANCES']._serialized_end=204
  _globals['_BALANCEUPDATE']._serialized_start=206
  _globals['_BALANCEUPDATE']._serialized_end=330
# @@protoc_insertion_point(module_scope)
