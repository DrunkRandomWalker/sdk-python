# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/oracle/v1beta1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&injective/oracle/v1beta1/genesis.proto\x12\x18injective.oracle.v1beta1\x1a%injective/oracle/v1beta1/oracle.proto\x1a\x14gogoproto/gogo.proto\"\xc5\x07\n\x0cGenesisState\x12\x36\n\x06params\x18\x01 \x01(\x0b\x32 .injective.oracle.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12\x15\n\rband_relayers\x18\x02 \x03(\t\x12\x43\n\x11\x62\x61nd_price_states\x18\x03 \x03(\x0b\x32(.injective.oracle.v1beta1.BandPriceState\x12I\n\x17price_feed_price_states\x18\x04 \x03(\x0b\x32(.injective.oracle.v1beta1.PriceFeedState\x12K\n\x15\x63oinbase_price_states\x18\x05 \x03(\x0b\x32,.injective.oracle.v1beta1.CoinbasePriceState\x12G\n\x15\x62\x61nd_ibc_price_states\x18\x06 \x03(\x0b\x32(.injective.oracle.v1beta1.BandPriceState\x12M\n\x18\x62\x61nd_ibc_oracle_requests\x18\x07 \x03(\x0b\x32+.injective.oracle.v1beta1.BandOracleRequest\x12\x46\n\x0f\x62\x61nd_ibc_params\x18\x08 \x01(\x0b\x32\'.injective.oracle.v1beta1.BandIBCParamsB\x04\xc8\xde\x1f\x00\x12!\n\x19\x62\x61nd_ibc_latest_client_id\x18\t \x01(\x04\x12\x42\n\x10\x63\x61lldata_records\x18\n \x03(\x0b\x32(.injective.oracle.v1beta1.CalldataRecord\x12\"\n\x1a\x62\x61nd_ibc_latest_request_id\x18\x0b \x01(\x04\x12M\n\x16\x63hainlink_price_states\x18\x0c \x03(\x0b\x32-.injective.oracle.v1beta1.ChainlinkPriceState\x12H\n\x18historical_price_records\x18\r \x03(\x0b\x32&.injective.oracle.v1beta1.PriceRecords\x12@\n\x0fprovider_states\x18\x0e \x03(\x0b\x32\'.injective.oracle.v1beta1.ProviderState\x12\x43\n\x11pyth_price_states\x18\x0f \x03(\x0b\x32(.injective.oracle.v1beta1.PythPriceState\"5\n\x0e\x43\x61lldataRecord\x12\x11\n\tclient_id\x18\x01 \x01(\x04\x12\x10\n\x08\x63\x61lldata\x18\x02 \x01(\x0c\x42NZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.oracle.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE'].fields_by_name['band_ibc_params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['band_ibc_params']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=130
  _globals['_GENESISSTATE']._serialized_end=1095
  _globals['_CALLDATARECORD']._serialized_start=1097
  _globals['_CALLDATARECORD']._serialized_end=1150
# @@protoc_insertion_point(module_scope)
