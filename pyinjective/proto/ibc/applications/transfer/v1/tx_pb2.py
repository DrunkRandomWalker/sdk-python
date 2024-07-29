# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ibc/applications/transfer/v1/tx.proto
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
    'ibc/applications/transfer/v1/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from pyinjective.proto.ibc.applications.transfer.v1 import transfer_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%ibc/applications/transfer/v1/tx.proto\x12\x1cibc.applications.transfer.v1\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1fibc/core/client/v1/client.proto\x1a+ibc/applications/transfer/v1/transfer.proto\"\x80\x03\n\x0bMsgTransfer\x12\x1f\n\x0bsource_port\x18\x01 \x01(\tR\nsourcePort\x12%\n\x0esource_channel\x18\x02 \x01(\tR\rsourceChannel\x12:\n\x05token\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x05token\x12\x16\n\x06sender\x18\x04 \x01(\tR\x06sender\x12\x1a\n\x08receiver\x18\x05 \x01(\tR\x08receiver\x12L\n\x0etimeout_height\x18\x06 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\rtimeoutHeight\x12+\n\x11timeout_timestamp\x18\x07 \x01(\x04R\x10timeoutTimestamp\x12\x12\n\x04memo\x18\x08 \x01(\tR\x04memo:*\x88\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x16\x63osmos-sdk/MsgTransfer\"7\n\x13MsgTransferResponse\x12\x1a\n\x08sequence\x18\x01 \x01(\x04R\x08sequence:\x04\x88\xa0\x1f\x00\"~\n\x0fMsgUpdateParams\x12\x16\n\x06signer\x18\x01 \x01(\tR\x06signer\x12\x42\n\x06params\x18\x02 \x01(\x0b\x32$.ibc.applications.transfer.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params:\x0f\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer\"\x19\n\x17MsgUpdateParamsResponse2\xec\x01\n\x03Msg\x12h\n\x08Transfer\x12).ibc.applications.transfer.v1.MsgTransfer\x1a\x31.ibc.applications.transfer.v1.MsgTransferResponse\x12t\n\x0cUpdateParams\x12-.ibc.applications.transfer.v1.MsgUpdateParams\x1a\x35.ibc.applications.transfer.v1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xf7\x01\n com.ibc.applications.transfer.v1B\x07TxProtoP\x01Z7github.com/cosmos/ibc-go/v8/modules/apps/transfer/types\xa2\x02\x03IAT\xaa\x02\x1cIbc.Applications.Transfer.V1\xca\x02\x1cIbc\\Applications\\Transfer\\V1\xe2\x02(Ibc\\Applications\\Transfer\\V1\\GPBMetadata\xea\x02\x1fIbc::Applications::Transfer::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.ibc.applications.transfer.v1B\007TxProtoP\001Z7github.com/cosmos/ibc-go/v8/modules/apps/transfer/types\242\002\003IAT\252\002\034Ibc.Applications.Transfer.V1\312\002\034Ibc\\Applications\\Transfer\\V1\342\002(Ibc\\Applications\\Transfer\\V1\\GPBMetadata\352\002\037Ibc::Applications::Transfer::V1'
  _globals['_MSGTRANSFER'].fields_by_name['token']._loaded_options = None
  _globals['_MSGTRANSFER'].fields_by_name['token']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGTRANSFER'].fields_by_name['timeout_height']._loaded_options = None
  _globals['_MSGTRANSFER'].fields_by_name['timeout_height']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGTRANSFER']._loaded_options = None
  _globals['_MSGTRANSFER']._serialized_options = b'\210\240\037\000\202\347\260*\006sender\212\347\260*\026cosmos-sdk/MsgTransfer'
  _globals['_MSGTRANSFERRESPONSE']._loaded_options = None
  _globals['_MSGTRANSFERRESPONSE']._serialized_options = b'\210\240\037\000'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\210\240\037\000\202\347\260*\006signer'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGTRANSFER']._serialized_start=248
  _globals['_MSGTRANSFER']._serialized_end=632
  _globals['_MSGTRANSFERRESPONSE']._serialized_start=634
  _globals['_MSGTRANSFERRESPONSE']._serialized_end=689
  _globals['_MSGUPDATEPARAMS']._serialized_start=691
  _globals['_MSGUPDATEPARAMS']._serialized_end=817
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=819
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=844
  _globals['_MSG']._serialized_start=847
  _globals['_MSG']._serialized_end=1083
# @@protoc_insertion_point(module_scope)
