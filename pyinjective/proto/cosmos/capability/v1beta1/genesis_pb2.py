# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/capability/v1beta1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.capability.v1beta1 import capability_pb2 as cosmos_dot_capability_dot_v1beta1_dot_capability__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cosmos/capability/v1beta1/genesis.proto\x12\x19\x63osmos.capability.v1beta1\x1a\x14gogoproto/gogo.proto\x1a*cosmos/capability/v1beta1/capability.proto\x1a\x11\x61mino/amino.proto\"l\n\rGenesisOwners\x12\r\n\x05index\x18\x01 \x01(\x04\x12L\n\x0cindex_owners\x18\x02 \x01(\x0b\x32+.cosmos.capability.v1beta1.CapabilityOwnersB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"b\n\x0cGenesisState\x12\r\n\x05index\x18\x01 \x01(\x04\x12\x43\n\x06owners\x18\x02 \x03(\x0b\x32(.cosmos.capability.v1beta1.GenesisOwnersB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x42\x31Z/github.com/cosmos/cosmos-sdk/x/capability/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.capability.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z/github.com/cosmos/cosmos-sdk/x/capability/types'
  _globals['_GENESISOWNERS'].fields_by_name['index_owners']._loaded_options = None
  _globals['_GENESISOWNERS'].fields_by_name['index_owners']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['owners']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['owners']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISOWNERS']._serialized_start=155
  _globals['_GENESISOWNERS']._serialized_end=263
  _globals['_GENESISSTATE']._serialized_start=265
  _globals['_GENESISSTATE']._serialized_end=363
# @@protoc_insertion_point(module_scope)
