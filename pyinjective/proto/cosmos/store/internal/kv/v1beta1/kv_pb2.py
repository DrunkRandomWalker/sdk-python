# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/store/internal/kv/v1beta1/kv.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cosmos/store/internal/kv/v1beta1/kv.proto\x12 cosmos.store.internal.kv.v1beta1\x1a\x14gogoproto/gogo.proto\"D\n\x05Pairs\x12;\n\x05pairs\x18\x01 \x03(\x0b\x32&.cosmos.store.internal.kv.v1beta1.PairB\x04\xc8\xde\x1f\x00\"\"\n\x04Pair\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x42 Z\x1e\x63osmossdk.io/store/internal/kvb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.store.internal.kv.v1beta1.kv_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\036cosmossdk.io/store/internal/kv'
  _globals['_PAIRS'].fields_by_name['pairs']._loaded_options = None
  _globals['_PAIRS'].fields_by_name['pairs']._serialized_options = b'\310\336\037\000'
  _globals['_PAIRS']._serialized_start=101
  _globals['_PAIRS']._serialized_end=169
  _globals['_PAIR']._serialized_start=171
  _globals['_PAIR']._serialized_end=205
# @@protoc_insertion_point(module_scope)
