# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/insurance/v1beta1/insurance.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+injective/insurance/v1beta1/insurance.proto\x12\x1binjective.insurance.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a%injective/oracle/v1beta1/oracle.proto\x1a\x11\x61mino/amino.proto\"\xb0\x01\n\x06Params\x12\x8a\x01\n)default_redemption_notice_period_duration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB<\xc8\xde\x1f\x00\xf2\xde\x1f\x30yaml:\"default_redemption_notice_period_duration\"\x98\xdf\x1f\x01:\x19\xe8\xa0\x1f\x01\x8a\xe7\xb0*\x10insurance/Params\"\xca\x03\n\rInsuranceFund\x12\x15\n\rdeposit_denom\x18\x01 \x01(\t\x12\"\n\x1ainsurance_pool_token_denom\x18\x02 \x01(\t\x12z\n!redemption_notice_period_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB4\xc8\xde\x1f\x00\xf2\xde\x1f(yaml:\"redemption_notice_period_duration\"\x98\xdf\x1f\x01\x12.\n\x07\x62\x61lance\x18\x04 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\x12\x32\n\x0btotal_share\x18\x05 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15\x63osmossdk.io/math.Int\x12\x11\n\tmarket_id\x18\x06 \x01(\t\x12\x15\n\rmarket_ticker\x18\x07 \x01(\t\x12\x13\n\x0boracle_base\x18\x08 \x01(\t\x12\x14\n\x0coracle_quote\x18\t \x01(\t\x12\x39\n\x0boracle_type\x18\n \x01(\x0e\x32$.injective.oracle.v1beta1.OracleType\x12\x0e\n\x06\x65xpiry\x18\x0b \x01(\x03\"\xed\x01\n\x12RedemptionSchedule\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x10\n\x08marketId\x18\x02 \x01(\t\x12\x10\n\x08redeemer\x18\x03 \x01(\t\x12k\n\x19\x63laimable_redemption_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB,\xc8\xde\x1f\x00\xf2\xde\x1f yaml:\"claimable_redemption_time\"\x90\xdf\x1f\x01\x12:\n\x11redemption_amount\x18\x05 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x42QZOgithub.com/InjectiveLabs/injective-core/injective-chain/modules/insurance/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.insurance.v1beta1.insurance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZOgithub.com/InjectiveLabs/injective-core/injective-chain/modules/insurance/types'
  _globals['_PARAMS'].fields_by_name['default_redemption_notice_period_duration']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['default_redemption_notice_period_duration']._serialized_options = b'\310\336\037\000\362\336\0370yaml:\"default_redemption_notice_period_duration\"\230\337\037\001'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\350\240\037\001\212\347\260*\020insurance/Params'
  _globals['_INSURANCEFUND'].fields_by_name['redemption_notice_period_duration']._loaded_options = None
  _globals['_INSURANCEFUND'].fields_by_name['redemption_notice_period_duration']._serialized_options = b'\310\336\037\000\362\336\037(yaml:\"redemption_notice_period_duration\"\230\337\037\001'
  _globals['_INSURANCEFUND'].fields_by_name['balance']._loaded_options = None
  _globals['_INSURANCEFUND'].fields_by_name['balance']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int'
  _globals['_INSURANCEFUND'].fields_by_name['total_share']._loaded_options = None
  _globals['_INSURANCEFUND'].fields_by_name['total_share']._serialized_options = b'\310\336\037\000\332\336\037\025cosmossdk.io/math.Int'
  _globals['_REDEMPTIONSCHEDULE'].fields_by_name['claimable_redemption_time']._loaded_options = None
  _globals['_REDEMPTIONSCHEDULE'].fields_by_name['claimable_redemption_time']._serialized_options = b'\310\336\037\000\362\336\037 yaml:\"claimable_redemption_time\"\220\337\037\001'
  _globals['_REDEMPTIONSCHEDULE'].fields_by_name['redemption_amount']._loaded_options = None
  _globals['_REDEMPTIONSCHEDULE'].fields_by_name['redemption_amount']._serialized_options = b'\310\336\037\000'
  _globals['_PARAMS']._serialized_start=254
  _globals['_PARAMS']._serialized_end=430
  _globals['_INSURANCEFUND']._serialized_start=433
  _globals['_INSURANCEFUND']._serialized_end=891
  _globals['_REDEMPTIONSCHEDULE']._serialized_start=894
  _globals['_REDEMPTIONSCHEDULE']._serialized_end=1131
# @@protoc_insertion_point(module_scope)
