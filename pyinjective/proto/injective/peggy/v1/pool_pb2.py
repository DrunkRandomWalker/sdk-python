# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: injective/peggy/v1/pool.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'injective/peggy/v1/pool.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dinjective/peggy/v1/pool.proto\x12\x12injective.peggy.v1\x1a\x14gogoproto/gogo.proto\"\x19\n\x05IDSet\x12\x10\n\x03ids\x18\x01 \x03(\x04R\x03ids\"_\n\tBatchFees\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12<\n\ntotal_fees\x18\x02 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.IntR\ttotalFeesB\xda\x01\n\x16\x63om.injective.peggy.v1B\tPoolProtoP\x01ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types\xa2\x02\x03IPX\xaa\x02\x12Injective.Peggy.V1\xca\x02\x12Injective\\Peggy\\V1\xe2\x02\x1eInjective\\Peggy\\V1\\GPBMetadata\xea\x02\x14Injective::Peggy::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.peggy.v1.pool_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.injective.peggy.v1B\tPoolProtoP\001ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types\242\002\003IPX\252\002\022Injective.Peggy.V1\312\002\022Injective\\Peggy\\V1\342\002\036Injective\\Peggy\\V1\\GPBMetadata\352\002\024Injective::Peggy::V1'
  _globals['_BATCHFEES'].fields_by_name['total_fees']._loaded_options = None
  _globals['_BATCHFEES'].fields_by_name['total_fees']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int'
  _globals['_IDSET']._serialized_start=75
  _globals['_IDSET']._serialized_end=100
  _globals['_BATCHFEES']._serialized_start=102
  _globals['_BATCHFEES']._serialized_end=197
# @@protoc_insertion_point(module_scope)
