# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from injective.wasmx.v1 import wasmx_pb2 as injective_dot_wasmx_dot_v1_dot_wasmx__pb2
from injective.wasmx.v1 import genesis_pb2 as injective_dot_wasmx_dot_v1_dot_genesis__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1einjective/wasmx/v1/query.proto\x12\x12injective.wasmx.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1einjective/wasmx/v1/wasmx.proto\x1a injective/wasmx/v1/genesis.proto\x1a\x14gogoproto/gogo.proto\"\x19\n\x17QueryWasmxParamsRequest\"L\n\x18QueryWasmxParamsResponse\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32\x1a.injective.wasmx.v1.ParamsB\x04\xc8\xde\x1f\x00\"\x19\n\x17QueryModuleStateRequest\"K\n\x18QueryModuleStateResponse\x12/\n\x05state\x18\x01 \x01(\x0b\x32 .injective.wasmx.v1.GenesisState\"@\n$QueryContractRegistrationInfoRequest\x12\x18\n\x10\x63ontract_address\x18\x01 \x01(\t\"a\n%QueryContractRegistrationInfoResponse\x12\x38\n\x08\x63ontract\x18\x01 \x01(\x0b\x32&.injective.wasmx.v1.RegisteredContract2\x84\x04\n\x05Query\x12\x8c\x01\n\x0bWasmxParams\x12+.injective.wasmx.v1.QueryWasmxParamsRequest\x1a,.injective.wasmx.v1.QueryWasmxParamsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/injective/wasmx/v1/params\x12\xd1\x01\n\x18\x43ontractRegistrationInfo\x12\x38.injective.wasmx.v1.QueryContractRegistrationInfoRequest\x1a\x39.injective.wasmx.v1.QueryContractRegistrationInfoResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/injective/wasmx/v1/registration_info/{contract_address}\x12\x97\x01\n\x10WasmxModuleState\x12+.injective.wasmx.v1.QueryModuleStateRequest\x1a,.injective.wasmx.v1.QueryModuleStateResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /injective/wasmx/v1/module_stateBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.wasmx.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types'
  _globals['_QUERYWASMXPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYWASMXPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['WasmxParams']._loaded_options = None
  _globals['_QUERY'].methods_by_name['WasmxParams']._serialized_options = b'\202\323\344\223\002\034\022\032/injective/wasmx/v1/params'
  _globals['_QUERY'].methods_by_name['ContractRegistrationInfo']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ContractRegistrationInfo']._serialized_options = b'\202\323\344\223\002:\0228/injective/wasmx/v1/registration_info/{contract_address}'
  _globals['_QUERY'].methods_by_name['WasmxModuleState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['WasmxModuleState']._serialized_options = b'\202\323\344\223\002\"\022 /injective/wasmx/v1/module_state'
  _globals['_QUERYWASMXPARAMSREQUEST']._serialized_start=172
  _globals['_QUERYWASMXPARAMSREQUEST']._serialized_end=197
  _globals['_QUERYWASMXPARAMSRESPONSE']._serialized_start=199
  _globals['_QUERYWASMXPARAMSRESPONSE']._serialized_end=275
  _globals['_QUERYMODULESTATEREQUEST']._serialized_start=277
  _globals['_QUERYMODULESTATEREQUEST']._serialized_end=302
  _globals['_QUERYMODULESTATERESPONSE']._serialized_start=304
  _globals['_QUERYMODULESTATERESPONSE']._serialized_end=379
  _globals['_QUERYCONTRACTREGISTRATIONINFOREQUEST']._serialized_start=381
  _globals['_QUERYCONTRACTREGISTRATIONINFOREQUEST']._serialized_end=445
  _globals['_QUERYCONTRACTREGISTRATIONINFORESPONSE']._serialized_start=447
  _globals['_QUERYCONTRACTREGISTRATIONINFORESPONSE']._serialized_end=544
  _globals['_QUERY']._serialized_start=547
  _globals['_QUERY']._serialized_end=1063
# @@protoc_insertion_point(module_scope)
