# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ibc/applications/interchain_accounts/host/v1/tx.proto
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
    'ibc/applications/interchain_accounts/host/v1/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.ibc.applications.interchain_accounts.host.v1 import host_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5ibc/applications/interchain_accounts/host/v1/tx.proto\x12,ibc.applications.interchain_accounts.host.v1\x1a\x14gogoproto/gogo.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x37ibc/applications/interchain_accounts/host/v1/host.proto\"\x8e\x01\n\x0fMsgUpdateParams\x12\x16\n\x06signer\x18\x01 \x01(\tR\x06signer\x12R\n\x06params\x18\x02 \x01(\x0b\x32\x34.ibc.applications.interchain_accounts.host.v1.ParamsB\x04\xc8\xde\x1f\x00R\x06params:\x0f\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer\"\x19\n\x17MsgUpdateParamsResponse\"\x95\x01\n\x12MsgModuleQuerySafe\x12\x16\n\x06signer\x18\x01 \x01(\tR\x06signer\x12V\n\x08requests\x18\x02 \x03(\x0b\x32:.ibc.applications.interchain_accounts.host.v1.QueryRequestR\x08requests:\x0f\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer\"R\n\x1aMsgModuleQuerySafeResponse\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x1c\n\tresponses\x18\x02 \x03(\x0cR\tresponses2\xc3\x02\n\x03Msg\x12\x94\x01\n\x0cUpdateParams\x12=.ibc.applications.interchain_accounts.host.v1.MsgUpdateParams\x1a\x45.ibc.applications.interchain_accounts.host.v1.MsgUpdateParamsResponse\x12\x9d\x01\n\x0fModuleQuerySafe\x12@.ibc.applications.interchain_accounts.host.v1.MsgModuleQuerySafe\x1aH.ibc.applications.interchain_accounts.host.v1.MsgModuleQuerySafeResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xd8\x02\n0com.ibc.applications.interchain_accounts.host.v1B\x07TxProtoP\x01ZJgithub.com/cosmos/ibc-go/v8/modules/apps/27-interchain-accounts/host/types\xa2\x02\x04IAIH\xaa\x02+Ibc.Applications.InterchainAccounts.Host.V1\xca\x02+Ibc\\Applications\\InterchainAccounts\\Host\\V1\xe2\x02\x37Ibc\\Applications\\InterchainAccounts\\Host\\V1\\GPBMetadata\xea\x02/Ibc::Applications::InterchainAccounts::Host::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.host.v1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n0com.ibc.applications.interchain_accounts.host.v1B\007TxProtoP\001ZJgithub.com/cosmos/ibc-go/v8/modules/apps/27-interchain-accounts/host/types\242\002\004IAIH\252\002+Ibc.Applications.InterchainAccounts.Host.V1\312\002+Ibc\\Applications\\InterchainAccounts\\Host\\V1\342\0027Ibc\\Applications\\InterchainAccounts\\Host\\V1\\GPBMetadata\352\002/Ibc::Applications::InterchainAccounts::Host::V1'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\210\240\037\000\202\347\260*\006signer'
  _globals['_MSGMODULEQUERYSAFE']._loaded_options = None
  _globals['_MSGMODULEQUERYSAFE']._serialized_options = b'\210\240\037\000\202\347\260*\006signer'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._serialized_start=208
  _globals['_MSGUPDATEPARAMS']._serialized_end=350
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=352
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=377
  _globals['_MSGMODULEQUERYSAFE']._serialized_start=380
  _globals['_MSGMODULEQUERYSAFE']._serialized_end=529
  _globals['_MSGMODULEQUERYSAFERESPONSE']._serialized_start=531
  _globals['_MSGMODULEQUERYSAFERESPONSE']._serialized_end=613
  _globals['_MSG']._serialized_start=616
  _globals['_MSG']._serialized_end=939
# @@protoc_insertion_point(module_scope)
