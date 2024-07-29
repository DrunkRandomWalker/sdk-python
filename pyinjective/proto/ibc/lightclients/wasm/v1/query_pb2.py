# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ibc/lightclients/wasm/v1/query.proto
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
    'ibc/lightclients/wasm/v1/query.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$ibc/lightclients/wasm/v1/query.proto\x12\x18ibc.lightclients.wasm.v1\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\"_\n\x15QueryChecksumsRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x7f\n\x16QueryChecksumsResponse\x12\x1c\n\tchecksums\x18\x01 \x03(\tR\tchecksums\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\".\n\x10QueryCodeRequest\x12\x1a\n\x08\x63hecksum\x18\x01 \x01(\tR\x08\x63hecksum\"\'\n\x11QueryCodeResponse\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta2\xc4\x02\n\x05Query\x12\x9b\x01\n\tChecksums\x12/.ibc.lightclients.wasm.v1.QueryChecksumsRequest\x1a\x30.ibc.lightclients.wasm.v1.QueryChecksumsResponse\"+\x82\xd3\xe4\x93\x02%\x12#/ibc/lightclients/wasm/v1/checksums\x12\x9c\x01\n\x04\x43ode\x12*.ibc.lightclients.wasm.v1.QueryCodeRequest\x1a+.ibc.lightclients.wasm.v1.QueryCodeResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/ibc/lightclients/wasm/v1/checksums/{checksum}/codeB\xeb\x01\n\x1c\x63om.ibc.lightclients.wasm.v1B\nQueryProtoP\x01Z<github.com/cosmos/ibc-go/modules/light-clients/08-wasm/types\xa2\x02\x03ILW\xaa\x02\x18Ibc.Lightclients.Wasm.V1\xca\x02\x18Ibc\\Lightclients\\Wasm\\V1\xe2\x02$Ibc\\Lightclients\\Wasm\\V1\\GPBMetadata\xea\x02\x1bIbc::Lightclients::Wasm::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.wasm.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.ibc.lightclients.wasm.v1B\nQueryProtoP\001Z<github.com/cosmos/ibc-go/modules/light-clients/08-wasm/types\242\002\003ILW\252\002\030Ibc.Lightclients.Wasm.V1\312\002\030Ibc\\Lightclients\\Wasm\\V1\342\002$Ibc\\Lightclients\\Wasm\\V1\\GPBMetadata\352\002\033Ibc::Lightclients::Wasm::V1'
  _globals['_QUERY'].methods_by_name['Checksums']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Checksums']._serialized_options = b'\202\323\344\223\002%\022#/ibc/lightclients/wasm/v1/checksums'
  _globals['_QUERY'].methods_by_name['Code']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Code']._serialized_options = b'\202\323\344\223\0025\0223/ibc/lightclients/wasm/v1/checksums/{checksum}/code'
  _globals['_QUERYCHECKSUMSREQUEST']._serialized_start=140
  _globals['_QUERYCHECKSUMSREQUEST']._serialized_end=235
  _globals['_QUERYCHECKSUMSRESPONSE']._serialized_start=237
  _globals['_QUERYCHECKSUMSRESPONSE']._serialized_end=364
  _globals['_QUERYCODEREQUEST']._serialized_start=366
  _globals['_QUERYCODEREQUEST']._serialized_end=412
  _globals['_QUERYCODERESPONSE']._serialized_start=414
  _globals['_QUERYCODERESPONSE']._serialized_end=453
  _globals['_QUERY']._serialized_start=456
  _globals['_QUERY']._serialized_end=780
# @@protoc_insertion_point(module_scope)
