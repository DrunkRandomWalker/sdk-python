# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/app/runtime/v1alpha1/module.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.app.v1alpha1 import module_pb2 as cosmos_dot_app_dot_v1alpha1_dot_module__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(cosmos/app/runtime/v1alpha1/module.proto\x12\x1b\x63osmos.app.runtime.v1alpha1\x1a cosmos/app/v1alpha1/module.proto\"\x85\x02\n\x06Module\x12\x10\n\x08\x61pp_name\x18\x01 \x01(\t\x12\x16\n\x0e\x62\x65gin_blockers\x18\x02 \x03(\t\x12\x14\n\x0c\x65nd_blockers\x18\x03 \x03(\t\x12\x14\n\x0cinit_genesis\x18\x04 \x03(\t\x12\x16\n\x0e\x65xport_genesis\x18\x05 \x03(\t\x12H\n\x13override_store_keys\x18\x06 \x03(\x0b\x32+.cosmos.app.runtime.v1alpha1.StoreKeyConfig:C\xba\xc0\x96\xda\x01=\n$github.com/cosmos/cosmos-sdk/runtime\x12\x15\n\x13\x63osmos.app.v1alpha1\";\n\x0eStoreKeyConfig\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12\x14\n\x0ckv_store_key\x18\x02 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.app.runtime.v1alpha1.module_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODULE._options = None
  _MODULE._serialized_options = b'\272\300\226\332\001=\n$github.com/cosmos/cosmos-sdk/runtime\022\025\n\023cosmos.app.v1alpha1'
  _globals['_MODULE']._serialized_start=108
  _globals['_MODULE']._serialized_end=369
  _globals['_STOREKEYCONFIG']._serialized_start=371
  _globals['_STOREKEYCONFIG']._serialized_end=430
# @@protoc_insertion_point(module_scope)
