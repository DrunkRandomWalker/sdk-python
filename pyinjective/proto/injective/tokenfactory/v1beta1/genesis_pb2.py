# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective.tokenfactory.v1beta1 import authorityMetadata_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2
from injective.tokenfactory.v1beta1 import params_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,injective/tokenfactory/v1beta1/genesis.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x36injective/tokenfactory/v1beta1/authorityMetadata.proto\x1a+injective/tokenfactory/v1beta1/params.proto\"\xb1\x01\n\x0cGenesisState\x12<\n\x06params\x18\x01 \x01(\x0b\x32&.injective.tokenfactory.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12\x63\n\x0e\x66\x61\x63tory_denoms\x18\x02 \x03(\x0b\x32,.injective.tokenfactory.v1beta1.GenesisDenomB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:\"factory_denoms\"\"\xee\x01\n\x0cGenesisDenom\x12\x1f\n\x05\x64\x65nom\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"denom\"\x12u\n\x12\x61uthority_metadata\x18\x02 \x01(\x0b\x32\x36.injective.tokenfactory.v1beta1.DenomAuthorityMetadataB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:\"authority_metadata\"\x12\x1d\n\x04name\x18\x03 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:\"name\"\x12!\n\x06symbol\x18\x04 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"symbol\":\x04\xe8\xa0\x1f\x01\x42TZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.tokenfactory.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['factory_denoms']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['factory_denoms']._serialized_options = b'\310\336\037\000\362\336\037\025yaml:\"factory_denoms\"'
  _globals['_GENESISDENOM'].fields_by_name['denom']._loaded_options = None
  _globals['_GENESISDENOM'].fields_by_name['denom']._serialized_options = b'\362\336\037\014yaml:\"denom\"'
  _globals['_GENESISDENOM'].fields_by_name['authority_metadata']._loaded_options = None
  _globals['_GENESISDENOM'].fields_by_name['authority_metadata']._serialized_options = b'\310\336\037\000\362\336\037\031yaml:\"authority_metadata\"'
  _globals['_GENESISDENOM'].fields_by_name['name']._loaded_options = None
  _globals['_GENESISDENOM'].fields_by_name['name']._serialized_options = b'\362\336\037\013yaml:\"name\"'
  _globals['_GENESISDENOM'].fields_by_name['symbol']._loaded_options = None
  _globals['_GENESISDENOM'].fields_by_name['symbol']._serialized_options = b'\362\336\037\ryaml:\"symbol\"'
  _globals['_GENESISDENOM']._loaded_options = None
  _globals['_GENESISDENOM']._serialized_options = b'\350\240\037\001'
  _globals['_GENESISSTATE']._serialized_start=204
  _globals['_GENESISSTATE']._serialized_end=381
  _globals['_GENESISDENOM']._serialized_start=384
  _globals['_GENESISDENOM']._serialized_end=622
# @@protoc_insertion_point(module_scope)
