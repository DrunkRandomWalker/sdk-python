# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/reflection/v1/reflection.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/reflection/v1/reflection.proto\x12\x14\x63osmos.reflection.v1\x1a google/protobuf/descriptor.proto\x1a\x1b\x63osmos/query/v1/query.proto\"\x18\n\x16\x46ileDescriptorsRequest\"N\n\x17\x46ileDescriptorsResponse\x12\x33\n\x05\x66iles\x18\x01 \x03(\x0b\x32$.google.protobuf.FileDescriptorProto2\x8a\x01\n\x11ReflectionService\x12u\n\x0f\x46ileDescriptors\x12,.cosmos.reflection.v1.FileDescriptorsRequest\x1a-.cosmos.reflection.v1.FileDescriptorsResponse\"\x05\x88\xe7\xb0*\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.reflection.v1.reflection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REFLECTIONSERVICE'].methods_by_name['FileDescriptors']._loaded_options = None
  _globals['_REFLECTIONSERVICE'].methods_by_name['FileDescriptors']._serialized_options = b'\210\347\260*\000'
  _globals['_FILEDESCRIPTORSREQUEST']._serialized_start=126
  _globals['_FILEDESCRIPTORSREQUEST']._serialized_end=150
  _globals['_FILEDESCRIPTORSRESPONSE']._serialized_start=152
  _globals['_FILEDESCRIPTORSRESPONSE']._serialized_end=230
  _globals['_REFLECTIONSERVICE']._serialized_start=233
  _globals['_REFLECTIONSERVICE']._serialized_end=371
# @@protoc_insertion_point(module_scope)
