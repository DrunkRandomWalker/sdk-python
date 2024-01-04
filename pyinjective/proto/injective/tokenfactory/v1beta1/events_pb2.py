# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/events.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from injective.tokenfactory.v1beta1 import authorityMetadata_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+injective/tokenfactory/v1beta1/events.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x36injective/tokenfactory/v1beta1/authorityMetadata.proto\"4\n\x12\x45ventCreateTFDenom\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\"^\n\x10\x45ventMintTFDenom\x12\x19\n\x11recipient_address\x18\x01 \x01(\t\x12/\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"Y\n\x0e\x45ventBurnDenom\x12\x16\n\x0e\x62urner_address\x18\x01 \x01(\t\x12/\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\">\n\x12\x45ventChangeTFAdmin\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x19\n\x11new_admin_address\x18\x02 \x01(\t\"_\n\x17\x45ventSetTFDenomMetadata\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x35\n\x08metadata\x18\x02 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00\x42TZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.tokenfactory.v1beta1.events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types'
  _EVENTMINTTFDENOM.fields_by_name['amount']._options = None
  _EVENTMINTTFDENOM.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _EVENTBURNDENOM.fields_by_name['amount']._options = None
  _EVENTBURNDENOM.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _EVENTSETTFDENOMMETADATA.fields_by_name['metadata']._options = None
  _EVENTSETTFDENOMMETADATA.fields_by_name['metadata']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTCREATETFDENOM']._serialized_start=221
  _globals['_EVENTCREATETFDENOM']._serialized_end=273
  _globals['_EVENTMINTTFDENOM']._serialized_start=275
  _globals['_EVENTMINTTFDENOM']._serialized_end=369
  _globals['_EVENTBURNDENOM']._serialized_start=371
  _globals['_EVENTBURNDENOM']._serialized_end=460
  _globals['_EVENTCHANGETFADMIN']._serialized_start=462
  _globals['_EVENTCHANGETFADMIN']._serialized_end=524
  _globals['_EVENTSETTFDENOMMETADATA']._serialized_start=526
  _globals['_EVENTSETTFDENOMMETADATA']._serialized_end=621
# @@protoc_insertion_point(module_scope)
