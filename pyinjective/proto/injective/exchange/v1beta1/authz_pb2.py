# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/exchange/v1beta1/authz.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&injective/exchange/v1beta1/authz.proto\x12\x1ainjective.exchange.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\x80\x01\n\x19\x43reateSpotLimitOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:8\xca\xb4-\rAuthorization\x8a\xe7\xb0*\"exchange/CreateSpotLimitOrderAuthz\"\x82\x01\n\x1a\x43reateSpotMarketOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:9\xca\xb4-\rAuthorization\x8a\xe7\xb0*#exchange/CreateSpotMarketOrderAuthz\"\x8c\x01\n\x1f\x42\x61tchCreateSpotLimitOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:>\xca\xb4-\rAuthorization\x8a\xe7\xb0*(exchange/BatchCreateSpotLimitOrdersAuthz\"v\n\x14\x43\x61ncelSpotOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:3\xca\xb4-\rAuthorization\x8a\xe7\xb0*\x1d\x65xchange/CancelSpotOrderAuthz\"\x82\x01\n\x1a\x42\x61tchCancelSpotOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:9\xca\xb4-\rAuthorization\x8a\xe7\xb0*#exchange/BatchCancelSpotOrdersAuthz\"\x8c\x01\n\x1f\x43reateDerivativeLimitOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:>\xca\xb4-\rAuthorization\x8a\xe7\xb0*(exchange/CreateDerivativeLimitOrderAuthz\"\x8e\x01\n CreateDerivativeMarketOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:?\xca\xb4-\rAuthorization\x8a\xe7\xb0*)exchange/CreateDerivativeMarketOrderAuthz\"\x98\x01\n%BatchCreateDerivativeLimitOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:D\xca\xb4-\rAuthorization\x8a\xe7\xb0*.exchange/BatchCreateDerivativeLimitOrdersAuthz\"\x82\x01\n\x1a\x43\x61ncelDerivativeOrderAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:9\xca\xb4-\rAuthorization\x8a\xe7\xb0*#exchange/CancelDerivativeOrderAuthz\"\x8e\x01\n BatchCancelDerivativeOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x12\n\nmarket_ids\x18\x02 \x03(\t:?\xca\xb4-\rAuthorization\x8a\xe7\xb0*)exchange/BatchCancelDerivativeOrdersAuthz\"\x98\x01\n\x16\x42\x61tchUpdateOrdersAuthz\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x14\n\x0cspot_markets\x18\x02 \x03(\t\x12\x1a\n\x12\x64\x65rivative_markets\x18\x03 \x03(\t:5\xca\xb4-\rAuthorization\x8a\xe7\xb0*\x1f\x65xchange/BatchUpdateOrdersAuthzBPZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.exchange.v1beta1.authz_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types'
  _globals['_CREATESPOTLIMITORDERAUTHZ']._loaded_options = None
  _globals['_CREATESPOTLIMITORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*\"exchange/CreateSpotLimitOrderAuthz'
  _globals['_CREATESPOTMARKETORDERAUTHZ']._loaded_options = None
  _globals['_CREATESPOTMARKETORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*#exchange/CreateSpotMarketOrderAuthz'
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._loaded_options = None
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*(exchange/BatchCreateSpotLimitOrdersAuthz'
  _globals['_CANCELSPOTORDERAUTHZ']._loaded_options = None
  _globals['_CANCELSPOTORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*\035exchange/CancelSpotOrderAuthz'
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._loaded_options = None
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*#exchange/BatchCancelSpotOrdersAuthz'
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._loaded_options = None
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*(exchange/CreateDerivativeLimitOrderAuthz'
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._loaded_options = None
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*)exchange/CreateDerivativeMarketOrderAuthz'
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._loaded_options = None
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*.exchange/BatchCreateDerivativeLimitOrdersAuthz'
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._loaded_options = None
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*#exchange/CancelDerivativeOrderAuthz'
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._loaded_options = None
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*)exchange/BatchCancelDerivativeOrdersAuthz'
  _globals['_BATCHUPDATEORDERSAUTHZ']._loaded_options = None
  _globals['_BATCHUPDATEORDERSAUTHZ']._serialized_options = b'\312\264-\rAuthorization\212\347\260*\037exchange/BatchUpdateOrdersAuthz'
  _globals['_CREATESPOTLIMITORDERAUTHZ']._serialized_start=117
  _globals['_CREATESPOTLIMITORDERAUTHZ']._serialized_end=245
  _globals['_CREATESPOTMARKETORDERAUTHZ']._serialized_start=248
  _globals['_CREATESPOTMARKETORDERAUTHZ']._serialized_end=378
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._serialized_start=381
  _globals['_BATCHCREATESPOTLIMITORDERSAUTHZ']._serialized_end=521
  _globals['_CANCELSPOTORDERAUTHZ']._serialized_start=523
  _globals['_CANCELSPOTORDERAUTHZ']._serialized_end=641
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._serialized_start=644
  _globals['_BATCHCANCELSPOTORDERSAUTHZ']._serialized_end=774
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._serialized_start=777
  _globals['_CREATEDERIVATIVELIMITORDERAUTHZ']._serialized_end=917
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._serialized_start=920
  _globals['_CREATEDERIVATIVEMARKETORDERAUTHZ']._serialized_end=1062
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._serialized_start=1065
  _globals['_BATCHCREATEDERIVATIVELIMITORDERSAUTHZ']._serialized_end=1217
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._serialized_start=1220
  _globals['_CANCELDERIVATIVEORDERAUTHZ']._serialized_end=1350
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._serialized_start=1353
  _globals['_BATCHCANCELDERIVATIVEORDERSAUTHZ']._serialized_end=1495
  _globals['_BATCHUPDATEORDERSAUTHZ']._serialized_start=1498
  _globals['_BATCHUPDATEORDERSAUTHZ']._serialized_end=1650
# @@protoc_insertion_point(module_scope)
