# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: injective/insurance/v1beta1/events.proto
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
    'injective/insurance/v1beta1/events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.injective.insurance.v1beta1 import insurance_pb2 as injective_dot_insurance_dot_v1beta1_dot_insurance__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(injective/insurance/v1beta1/events.proto\x12\x1binjective.insurance.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a+injective/insurance/v1beta1/insurance.proto\"Z\n\x18\x45ventInsuranceFundUpdate\x12>\n\x04\x66und\x18\x01 \x01(\x0b\x32*.injective.insurance.v1beta1.InsuranceFundR\x04\x66und\"e\n\x16\x45ventRequestRedemption\x12K\n\x08schedule\x18\x01 \x01(\x0b\x32/.injective.insurance.v1beta1.RedemptionScheduleR\x08schedule\"\xa8\x01\n\x17\x45ventWithdrawRedemption\x12K\n\x08schedule\x18\x01 \x01(\x0b\x32/.injective.insurance.v1beta1.RedemptionScheduleR\x08schedule\x12@\n\x0bredeem_coin\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\nredeemCoin\"\xc3\x01\n\x0f\x45ventUnderwrite\x12 \n\x0bunderwriter\x18\x01 \x01(\tR\x0bunderwriter\x12\x1a\n\x08marketId\x18\x02 \x01(\tR\x08marketId\x12\x39\n\x07\x64\x65posit\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x07\x64\x65posit\x12\x37\n\x06shares\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\x06shares\"\x9b\x01\n\x16\x45ventInsuranceWithdraw\x12\x1b\n\tmarket_id\x18\x01 \x01(\tR\x08marketId\x12#\n\rmarket_ticker\x18\x02 \x01(\tR\x0cmarketTicker\x12?\n\nwithdrawal\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\nwithdrawalB\x8d\x02\n\x1f\x63om.injective.insurance.v1beta1B\x0b\x45ventsProtoP\x01ZOgithub.com/InjectiveLabs/injective-core/injective-chain/modules/insurance/types\xa2\x02\x03IIX\xaa\x02\x1bInjective.Insurance.V1beta1\xca\x02\x1bInjective\\Insurance\\V1beta1\xe2\x02\'Injective\\Insurance\\V1beta1\\GPBMetadata\xea\x02\x1dInjective::Insurance::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.insurance.v1beta1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.injective.insurance.v1beta1B\013EventsProtoP\001ZOgithub.com/InjectiveLabs/injective-core/injective-chain/modules/insurance/types\242\002\003IIX\252\002\033Injective.Insurance.V1beta1\312\002\033Injective\\Insurance\\V1beta1\342\002\'Injective\\Insurance\\V1beta1\\GPBMetadata\352\002\035Injective::Insurance::V1beta1'
  _globals['_EVENTWITHDRAWREDEMPTION'].fields_by_name['redeem_coin']._loaded_options = None
  _globals['_EVENTWITHDRAWREDEMPTION'].fields_by_name['redeem_coin']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTUNDERWRITE'].fields_by_name['deposit']._loaded_options = None
  _globals['_EVENTUNDERWRITE'].fields_by_name['deposit']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTUNDERWRITE'].fields_by_name['shares']._loaded_options = None
  _globals['_EVENTUNDERWRITE'].fields_by_name['shares']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTINSURANCEWITHDRAW'].fields_by_name['withdrawal']._loaded_options = None
  _globals['_EVENTINSURANCEWITHDRAW'].fields_by_name['withdrawal']._serialized_options = b'\310\336\037\000'
  _globals['_EVENTINSURANCEFUNDUPDATE']._serialized_start=172
  _globals['_EVENTINSURANCEFUNDUPDATE']._serialized_end=262
  _globals['_EVENTREQUESTREDEMPTION']._serialized_start=264
  _globals['_EVENTREQUESTREDEMPTION']._serialized_end=365
  _globals['_EVENTWITHDRAWREDEMPTION']._serialized_start=368
  _globals['_EVENTWITHDRAWREDEMPTION']._serialized_end=536
  _globals['_EVENTUNDERWRITE']._serialized_start=539
  _globals['_EVENTUNDERWRITE']._serialized_end=734
  _globals['_EVENTINSURANCEWITHDRAW']._serialized_start=737
  _globals['_EVENTINSURANCEWITHDRAW']._serialized_end=892
# @@protoc_insertion_point(module_scope)
