# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/app/v1alpha1/config.proto
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
    'cosmos/app/v1alpha1/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/app/v1alpha1/config.proto\x12\x13\x63osmos.app.v1alpha1\x1a\x19google/protobuf/any.proto\"\x92\x01\n\x06\x43onfig\x12;\n\x07modules\x18\x01 \x03(\x0b\x32!.cosmos.app.v1alpha1.ModuleConfigR\x07modules\x12K\n\x0fgolang_bindings\x18\x02 \x03(\x0b\x32\".cosmos.app.v1alpha1.GolangBindingR\x0egolangBindings\"\x9d\x01\n\x0cModuleConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12,\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyR\x06\x63onfig\x12K\n\x0fgolang_bindings\x18\x03 \x03(\x0b\x32\".cosmos.app.v1alpha1.GolangBindingR\x0egolangBindings\"^\n\rGolangBinding\x12%\n\x0einterface_type\x18\x01 \x01(\tR\rinterfaceType\x12&\n\x0eimplementation\x18\x02 \x01(\tR\x0eimplementationB\x94\x01\n\x17\x63om.cosmos.app.v1alpha1B\x0b\x43onfigProtoP\x01\xa2\x02\x03\x43\x41X\xaa\x02\x13\x43osmos.App.V1alpha1\xca\x02\x13\x43osmos\\App\\V1alpha1\xe2\x02\x1f\x43osmos\\App\\V1alpha1\\GPBMetadata\xea\x02\x15\x43osmos::App::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.app.v1alpha1.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.cosmos.app.v1alpha1B\013ConfigProtoP\001\242\002\003CAX\252\002\023Cosmos.App.V1alpha1\312\002\023Cosmos\\App\\V1alpha1\342\002\037Cosmos\\App\\V1alpha1\\GPBMetadata\352\002\025Cosmos::App::V1alpha1'
  _globals['_CONFIG']._serialized_start=85
  _globals['_CONFIG']._serialized_end=231
  _globals['_MODULECONFIG']._serialized_start=234
  _globals['_MODULECONFIG']._serialized_end=391
  _globals['_GOLANGBINDING']._serialized_start=393
  _globals['_GOLANGBINDING']._serialized_end=487
# @@protoc_insertion_point(module_scope)
