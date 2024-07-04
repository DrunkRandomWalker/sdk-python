# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmwasm/wasm/v1/tx.proto
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
    'cosmwasm/wasm/v1/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmwasm.wasm.v1 import types_pb2 as cosmwasm_dot_wasm_dot_v1_dot_types__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63osmwasm/wasm/v1/tx.proto\x12\x10\x63osmwasm.wasm.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmwasm/wasm/v1/types.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xfe\x01\n\x0cMsgStoreCode\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x36\n\x0ewasm_byte_code\x18\x02 \x01(\x0c\x42\x10\xe2\xde\x1f\x0cWASMByteCodeR\x0cwasmByteCode\x12U\n\x16instantiate_permission\x18\x05 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigR\x15instantiatePermission:!\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x11wasm/MsgStoreCodeJ\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05\"W\n\x14MsgStoreCodeResponse\x12#\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeIDR\x06\x63odeId\x12\x1a\n\x08\x63hecksum\x18\x02 \x01(\x0cR\x08\x63hecksum\"\x95\x03\n\x16MsgInstantiateContract\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12.\n\x05\x61\x64min\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12#\n\x07\x63ode_id\x18\x03 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeIDR\x06\x63odeId\x12\x14\n\x05label\x18\x04 \x01(\tR\x05label\x12\x38\n\x03msg\x18\x05 \x01(\x0c\x42&\xfa\xde\x1f\x12RawContractMessage\x9a\xe7\xb0*\x0binline_jsonR\x03msg\x12w\n\x05\x66unds\x18\x06 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x05\x66unds:+\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1bwasm/MsgInstantiateContract\"h\n\x1eMsgInstantiateContractResponse\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\"\xc4\x03\n\x17MsgInstantiateContract2\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12.\n\x05\x61\x64min\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12#\n\x07\x63ode_id\x18\x03 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeIDR\x06\x63odeId\x12\x14\n\x05label\x18\x04 \x01(\tR\x05label\x12\x38\n\x03msg\x18\x05 \x01(\x0c\x42&\xfa\xde\x1f\x12RawContractMessage\x9a\xe7\xb0*\x0binline_jsonR\x03msg\x12w\n\x05\x66unds\x18\x06 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x05\x66unds\x12\x12\n\x04salt\x18\x07 \x01(\x0cR\x04salt\x12\x17\n\x07\x66ix_msg\x18\x08 \x01(\x08R\x06\x66ixMsg:,\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1cwasm/MsgInstantiateContract2\"i\n\x1fMsgInstantiateContract2Response\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\"\xd8\x02\n\x12MsgExecuteContract\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x34\n\x08\x63ontract\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08\x63ontract\x12\x38\n\x03msg\x18\x03 \x01(\x0c\x42&\xfa\xde\x1f\x12RawContractMessage\x9a\xe7\xb0*\x0binline_jsonR\x03msg\x12w\n\x05\x66unds\x18\x05 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x05\x66unds:\'\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x17wasm/MsgExecuteContract\"0\n\x1aMsgExecuteContractResponse\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"\x84\x02\n\x12MsgMigrateContract\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x34\n\x08\x63ontract\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08\x63ontract\x12#\n\x07\x63ode_id\x18\x03 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeIDR\x06\x63odeId\x12\x38\n\x03msg\x18\x04 \x01(\x0c\x42&\xfa\xde\x1f\x12RawContractMessage\x9a\xe7\xb0*\x0binline_jsonR\x03msg:\'\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x17wasm/MsgMigrateContract\"0\n\x1aMsgMigrateContractResponse\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"\xd4\x01\n\x0eMsgUpdateAdmin\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x35\n\tnew_admin\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08newAdmin\x12\x34\n\x08\x63ontract\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08\x63ontract:#\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x13wasm/MsgUpdateAdmin\"\x18\n\x16MsgUpdateAdminResponse\"\x9b\x01\n\rMsgClearAdmin\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x34\n\x08\x63ontract\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08\x63ontract:\"\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x12wasm/MsgClearAdmin\"\x17\n\x15MsgClearAdminResponse\"\x82\x02\n\x1aMsgUpdateInstantiateConfig\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12#\n\x07\x63ode_id\x18\x02 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeIDR\x06\x63odeId\x12\\\n\x1anew_instantiate_permission\x18\x03 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigR\x18newInstantiatePermission:/\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1fwasm/MsgUpdateInstantiateConfig\"$\n\"MsgUpdateInstantiateConfigResponse\"\xaf\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12;\n\x06params\x18\x02 \x01(\x0b\x32\x18.cosmwasm.wasm.v1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params:\'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x14wasm/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse\"\xe2\x01\n\x0fMsgSudoContract\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x34\n\x08\x63ontract\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08\x63ontract\x12\x38\n\x03msg\x18\x03 \x01(\x0c\x42&\xfa\xde\x1f\x12RawContractMessage\x9a\xe7\xb0*\x0binline_jsonR\x03msg:\'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x14wasm/MsgSudoContract\"-\n\x17MsgSudoContractResponse\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"\xa5\x01\n\x0bMsgPinCodes\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x39\n\x08\x63ode_ids\x18\x02 \x03(\x04\x42\x1e\xe2\xde\x1f\x07\x43odeIDs\xf2\xde\x1f\x0fyaml:\"code_ids\"R\x07\x63odeIds:#\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x10wasm/MsgPinCodes\"\x15\n\x13MsgPinCodesResponse\"\xa9\x01\n\rMsgUnpinCodes\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x39\n\x08\x63ode_ids\x18\x02 \x03(\x04\x42\x1e\xe2\xde\x1f\x07\x43odeIDs\xf2\xde\x1f\x0fyaml:\"code_ids\"R\x07\x63odeIds:%\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x12wasm/MsgUnpinCodes\"\x17\n\x15MsgUnpinCodesResponse\"\x86\x05\n\x1eMsgStoreAndInstantiateContract\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x36\n\x0ewasm_byte_code\x18\x03 \x01(\x0c\x42\x10\xe2\xde\x1f\x0cWASMByteCodeR\x0cwasmByteCode\x12U\n\x16instantiate_permission\x18\x04 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigR\x15instantiatePermission\x12\x1d\n\nunpin_code\x18\x05 \x01(\x08R\tunpinCode\x12.\n\x05\x61\x64min\x18\x06 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12\x14\n\x05label\x18\x07 \x01(\tR\x05label\x12\x38\n\x03msg\x18\x08 \x01(\x0c\x42&\xfa\xde\x1f\x12RawContractMessage\x9a\xe7\xb0*\x0binline_jsonR\x03msg\x12w\n\x05\x66unds\x18\t \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x05\x66unds\x12\x16\n\x06source\x18\n \x01(\tR\x06source\x12\x18\n\x07\x62uilder\x18\x0b \x01(\tR\x07\x62uilder\x12\x1b\n\tcode_hash\x18\x0c \x01(\x0cR\x08\x63odeHash:6\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*#wasm/MsgStoreAndInstantiateContract\"p\n&MsgStoreAndInstantiateContractResponse\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\"\xc6\x01\n\x1fMsgAddCodeUploadParamsAddresses\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x32\n\taddresses\x18\x02 \x03(\tB\x14\xf2\xde\x1f\x10yaml:\"addresses\"R\taddresses:7\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*$wasm/MsgAddCodeUploadParamsAddresses\")\n\'MsgAddCodeUploadParamsAddressesResponse\"\xcc\x01\n\"MsgRemoveCodeUploadParamsAddresses\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x32\n\taddresses\x18\x02 \x03(\tB\x14\xf2\xde\x1f\x10yaml:\"addresses\"R\taddresses::\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\'wasm/MsgRemoveCodeUploadParamsAddresses\",\n*MsgRemoveCodeUploadParamsAddressesResponse\"\xed\x02\n\x1aMsgStoreAndMigrateContract\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x36\n\x0ewasm_byte_code\x18\x02 \x01(\x0c\x42\x10\xe2\xde\x1f\x0cWASMByteCodeR\x0cwasmByteCode\x12U\n\x16instantiate_permission\x18\x03 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigR\x15instantiatePermission\x12\x1a\n\x08\x63ontract\x18\x04 \x01(\tR\x08\x63ontract\x12\x38\n\x03msg\x18\x05 \x01(\x0c\x42&\xfa\xde\x1f\x12RawContractMessage\x9a\xe7\xb0*\x0binline_jsonR\x03msg:2\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1fwasm/MsgStoreAndMigrateContract\"y\n\"MsgStoreAndMigrateContractResponse\x12#\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeIDR\x06\x63odeId\x12\x1a\n\x08\x63hecksum\x18\x02 \x01(\x0cR\x08\x63hecksum\x12\x12\n\x04\x64\x61ta\x18\x03 \x01(\x0cR\x04\x64\x61ta\"\xca\x01\n\x16MsgUpdateContractLabel\x12\x30\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x06sender\x12\x1b\n\tnew_label\x18\x02 \x01(\tR\x08newLabel\x12\x34\n\x08\x63ontract\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08\x63ontract:+\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1bwasm/MsgUpdateContractLabel\" \n\x1eMsgUpdateContractLabelResponse2\xd5\x0e\n\x03Msg\x12S\n\tStoreCode\x12\x1e.cosmwasm.wasm.v1.MsgStoreCode\x1a&.cosmwasm.wasm.v1.MsgStoreCodeResponse\x12q\n\x13InstantiateContract\x12(.cosmwasm.wasm.v1.MsgInstantiateContract\x1a\x30.cosmwasm.wasm.v1.MsgInstantiateContractResponse\x12t\n\x14InstantiateContract2\x12).cosmwasm.wasm.v1.MsgInstantiateContract2\x1a\x31.cosmwasm.wasm.v1.MsgInstantiateContract2Response\x12\x65\n\x0f\x45xecuteContract\x12$.cosmwasm.wasm.v1.MsgExecuteContract\x1a,.cosmwasm.wasm.v1.MsgExecuteContractResponse\x12\x65\n\x0fMigrateContract\x12$.cosmwasm.wasm.v1.MsgMigrateContract\x1a,.cosmwasm.wasm.v1.MsgMigrateContractResponse\x12Y\n\x0bUpdateAdmin\x12 .cosmwasm.wasm.v1.MsgUpdateAdmin\x1a(.cosmwasm.wasm.v1.MsgUpdateAdminResponse\x12V\n\nClearAdmin\x12\x1f.cosmwasm.wasm.v1.MsgClearAdmin\x1a\'.cosmwasm.wasm.v1.MsgClearAdminResponse\x12}\n\x17UpdateInstantiateConfig\x12,.cosmwasm.wasm.v1.MsgUpdateInstantiateConfig\x1a\x34.cosmwasm.wasm.v1.MsgUpdateInstantiateConfigResponse\x12\\\n\x0cUpdateParams\x12!.cosmwasm.wasm.v1.MsgUpdateParams\x1a).cosmwasm.wasm.v1.MsgUpdateParamsResponse\x12\\\n\x0cSudoContract\x12!.cosmwasm.wasm.v1.MsgSudoContract\x1a).cosmwasm.wasm.v1.MsgSudoContractResponse\x12P\n\x08PinCodes\x12\x1d.cosmwasm.wasm.v1.MsgPinCodes\x1a%.cosmwasm.wasm.v1.MsgPinCodesResponse\x12V\n\nUnpinCodes\x12\x1f.cosmwasm.wasm.v1.MsgUnpinCodes\x1a\'.cosmwasm.wasm.v1.MsgUnpinCodesResponse\x12\x89\x01\n\x1bStoreAndInstantiateContract\x12\x30.cosmwasm.wasm.v1.MsgStoreAndInstantiateContract\x1a\x38.cosmwasm.wasm.v1.MsgStoreAndInstantiateContractResponse\x12\x95\x01\n\x1fRemoveCodeUploadParamsAddresses\x12\x34.cosmwasm.wasm.v1.MsgRemoveCodeUploadParamsAddresses\x1a<.cosmwasm.wasm.v1.MsgRemoveCodeUploadParamsAddressesResponse\x12\x8c\x01\n\x1c\x41\x64\x64\x43odeUploadParamsAddresses\x12\x31.cosmwasm.wasm.v1.MsgAddCodeUploadParamsAddresses\x1a\x39.cosmwasm.wasm.v1.MsgAddCodeUploadParamsAddressesResponse\x12}\n\x17StoreAndMigrateContract\x12,.cosmwasm.wasm.v1.MsgStoreAndMigrateContract\x1a\x34.cosmwasm.wasm.v1.MsgStoreAndMigrateContractResponse\x12q\n\x13UpdateContractLabel\x12(.cosmwasm.wasm.v1.MsgUpdateContractLabel\x1a\x30.cosmwasm.wasm.v1.MsgUpdateContractLabelResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xad\x01\n\x14\x63om.cosmwasm.wasm.v1B\x07TxProtoP\x01Z&github.com/CosmWasm/wasmd/x/wasm/types\xa2\x02\x03\x43WX\xaa\x02\x10\x43osmwasm.Wasm.V1\xca\x02\x10\x43osmwasm\\Wasm\\V1\xe2\x02\x1c\x43osmwasm\\Wasm\\V1\\GPBMetadata\xea\x02\x12\x43osmwasm::Wasm::V1\xc8\xe1\x1e\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmwasm.wasm.v1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cosmwasm.wasm.v1B\007TxProtoP\001Z&github.com/CosmWasm/wasmd/x/wasm/types\242\002\003CWX\252\002\020Cosmwasm.Wasm.V1\312\002\020Cosmwasm\\Wasm\\V1\342\002\034Cosmwasm\\Wasm\\V1\\GPBMetadata\352\002\022Cosmwasm::Wasm::V1\310\341\036\000'
  _globals['_MSGSTORECODE'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGSTORECODE'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSTORECODE'].fields_by_name['wasm_byte_code']._loaded_options = None
  _globals['_MSGSTORECODE'].fields_by_name['wasm_byte_code']._serialized_options = b'\342\336\037\014WASMByteCode'
  _globals['_MSGSTORECODE']._loaded_options = None
  _globals['_MSGSTORECODE']._serialized_options = b'\202\347\260*\006sender\212\347\260*\021wasm/MsgStoreCode'
  _globals['_MSGSTORECODERESPONSE'].fields_by_name['code_id']._loaded_options = None
  _globals['_MSGSTORECODERESPONSE'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_MSGINSTANTIATECONTRACT'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGINSTANTIATECONTRACT'].fields_by_name['admin']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT'].fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGINSTANTIATECONTRACT'].fields_by_name['code_id']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_MSGINSTANTIATECONTRACT'].fields_by_name['msg']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage\232\347\260*\013inline_json'
  _globals['_MSGINSTANTIATECONTRACT'].fields_by_name['funds']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT'].fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGINSTANTIATECONTRACT']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT']._serialized_options = b'\202\347\260*\006sender\212\347\260*\033wasm/MsgInstantiateContract'
  _globals['_MSGINSTANTIATECONTRACTRESPONSE'].fields_by_name['address']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACTRESPONSE'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGINSTANTIATECONTRACT2'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT2'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGINSTANTIATECONTRACT2'].fields_by_name['admin']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT2'].fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGINSTANTIATECONTRACT2'].fields_by_name['code_id']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT2'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_MSGINSTANTIATECONTRACT2'].fields_by_name['msg']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT2'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage\232\347\260*\013inline_json'
  _globals['_MSGINSTANTIATECONTRACT2'].fields_by_name['funds']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT2'].fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGINSTANTIATECONTRACT2']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT2']._serialized_options = b'\202\347\260*\006sender\212\347\260*\034wasm/MsgInstantiateContract2'
  _globals['_MSGINSTANTIATECONTRACT2RESPONSE'].fields_by_name['address']._loaded_options = None
  _globals['_MSGINSTANTIATECONTRACT2RESPONSE'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGEXECUTECONTRACT'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGEXECUTECONTRACT'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGEXECUTECONTRACT'].fields_by_name['contract']._loaded_options = None
  _globals['_MSGEXECUTECONTRACT'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGEXECUTECONTRACT'].fields_by_name['msg']._loaded_options = None
  _globals['_MSGEXECUTECONTRACT'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage\232\347\260*\013inline_json'
  _globals['_MSGEXECUTECONTRACT'].fields_by_name['funds']._loaded_options = None
  _globals['_MSGEXECUTECONTRACT'].fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGEXECUTECONTRACT']._loaded_options = None
  _globals['_MSGEXECUTECONTRACT']._serialized_options = b'\202\347\260*\006sender\212\347\260*\027wasm/MsgExecuteContract'
  _globals['_MSGMIGRATECONTRACT'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGMIGRATECONTRACT'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGMIGRATECONTRACT'].fields_by_name['contract']._loaded_options = None
  _globals['_MSGMIGRATECONTRACT'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGMIGRATECONTRACT'].fields_by_name['code_id']._loaded_options = None
  _globals['_MSGMIGRATECONTRACT'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_MSGMIGRATECONTRACT'].fields_by_name['msg']._loaded_options = None
  _globals['_MSGMIGRATECONTRACT'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage\232\347\260*\013inline_json'
  _globals['_MSGMIGRATECONTRACT']._loaded_options = None
  _globals['_MSGMIGRATECONTRACT']._serialized_options = b'\202\347\260*\006sender\212\347\260*\027wasm/MsgMigrateContract'
  _globals['_MSGUPDATEADMIN'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGUPDATEADMIN'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEADMIN'].fields_by_name['new_admin']._loaded_options = None
  _globals['_MSGUPDATEADMIN'].fields_by_name['new_admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEADMIN'].fields_by_name['contract']._loaded_options = None
  _globals['_MSGUPDATEADMIN'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEADMIN']._loaded_options = None
  _globals['_MSGUPDATEADMIN']._serialized_options = b'\202\347\260*\006sender\212\347\260*\023wasm/MsgUpdateAdmin'
  _globals['_MSGCLEARADMIN'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGCLEARADMIN'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGCLEARADMIN'].fields_by_name['contract']._loaded_options = None
  _globals['_MSGCLEARADMIN'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGCLEARADMIN']._loaded_options = None
  _globals['_MSGCLEARADMIN']._serialized_options = b'\202\347\260*\006sender\212\347\260*\022wasm/MsgClearAdmin'
  _globals['_MSGUPDATEINSTANTIATECONFIG'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGUPDATEINSTANTIATECONFIG'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEINSTANTIATECONFIG'].fields_by_name['code_id']._loaded_options = None
  _globals['_MSGUPDATEINSTANTIATECONFIG'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_MSGUPDATEINSTANTIATECONFIG']._loaded_options = None
  _globals['_MSGUPDATEINSTANTIATECONFIG']._serialized_options = b'\202\347\260*\006sender\212\347\260*\037wasm/MsgUpdateInstantiateConfig'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\024wasm/MsgUpdateParams'
  _globals['_MSGSUDOCONTRACT'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGSUDOCONTRACT'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSUDOCONTRACT'].fields_by_name['contract']._loaded_options = None
  _globals['_MSGSUDOCONTRACT'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSUDOCONTRACT'].fields_by_name['msg']._loaded_options = None
  _globals['_MSGSUDOCONTRACT'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage\232\347\260*\013inline_json'
  _globals['_MSGSUDOCONTRACT']._loaded_options = None
  _globals['_MSGSUDOCONTRACT']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\024wasm/MsgSudoContract'
  _globals['_MSGPINCODES'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGPINCODES'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGPINCODES'].fields_by_name['code_ids']._loaded_options = None
  _globals['_MSGPINCODES'].fields_by_name['code_ids']._serialized_options = b'\342\336\037\007CodeIDs\362\336\037\017yaml:\"code_ids\"'
  _globals['_MSGPINCODES']._loaded_options = None
  _globals['_MSGPINCODES']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\020wasm/MsgPinCodes'
  _globals['_MSGUNPINCODES'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUNPINCODES'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUNPINCODES'].fields_by_name['code_ids']._loaded_options = None
  _globals['_MSGUNPINCODES'].fields_by_name['code_ids']._serialized_options = b'\342\336\037\007CodeIDs\362\336\037\017yaml:\"code_ids\"'
  _globals['_MSGUNPINCODES']._loaded_options = None
  _globals['_MSGUNPINCODES']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\022wasm/MsgUnpinCodes'
  _globals['_MSGSTOREANDINSTANTIATECONTRACT'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGSTOREANDINSTANTIATECONTRACT'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSTOREANDINSTANTIATECONTRACT'].fields_by_name['wasm_byte_code']._loaded_options = None
  _globals['_MSGSTOREANDINSTANTIATECONTRACT'].fields_by_name['wasm_byte_code']._serialized_options = b'\342\336\037\014WASMByteCode'
  _globals['_MSGSTOREANDINSTANTIATECONTRACT'].fields_by_name['admin']._loaded_options = None
  _globals['_MSGSTOREANDINSTANTIATECONTRACT'].fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSTOREANDINSTANTIATECONTRACT'].fields_by_name['msg']._loaded_options = None
  _globals['_MSGSTOREANDINSTANTIATECONTRACT'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage\232\347\260*\013inline_json'
  _globals['_MSGSTOREANDINSTANTIATECONTRACT'].fields_by_name['funds']._loaded_options = None
  _globals['_MSGSTOREANDINSTANTIATECONTRACT'].fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGSTOREANDINSTANTIATECONTRACT']._loaded_options = None
  _globals['_MSGSTOREANDINSTANTIATECONTRACT']._serialized_options = b'\202\347\260*\tauthority\212\347\260*#wasm/MsgStoreAndInstantiateContract'
  _globals['_MSGSTOREANDINSTANTIATECONTRACTRESPONSE'].fields_by_name['address']._loaded_options = None
  _globals['_MSGSTOREANDINSTANTIATECONTRACTRESPONSE'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSES'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSES'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSES'].fields_by_name['addresses']._loaded_options = None
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSES'].fields_by_name['addresses']._serialized_options = b'\362\336\037\020yaml:\"addresses\"'
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSES']._loaded_options = None
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSES']._serialized_options = b'\202\347\260*\tauthority\212\347\260*$wasm/MsgAddCodeUploadParamsAddresses'
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSES'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSES'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSES'].fields_by_name['addresses']._loaded_options = None
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSES'].fields_by_name['addresses']._serialized_options = b'\362\336\037\020yaml:\"addresses\"'
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSES']._loaded_options = None
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSES']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\'wasm/MsgRemoveCodeUploadParamsAddresses'
  _globals['_MSGSTOREANDMIGRATECONTRACT'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGSTOREANDMIGRATECONTRACT'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSTOREANDMIGRATECONTRACT'].fields_by_name['wasm_byte_code']._loaded_options = None
  _globals['_MSGSTOREANDMIGRATECONTRACT'].fields_by_name['wasm_byte_code']._serialized_options = b'\342\336\037\014WASMByteCode'
  _globals['_MSGSTOREANDMIGRATECONTRACT'].fields_by_name['msg']._loaded_options = None
  _globals['_MSGSTOREANDMIGRATECONTRACT'].fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage\232\347\260*\013inline_json'
  _globals['_MSGSTOREANDMIGRATECONTRACT']._loaded_options = None
  _globals['_MSGSTOREANDMIGRATECONTRACT']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\037wasm/MsgStoreAndMigrateContract'
  _globals['_MSGSTOREANDMIGRATECONTRACTRESPONSE'].fields_by_name['code_id']._loaded_options = None
  _globals['_MSGSTOREANDMIGRATECONTRACTRESPONSE'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_MSGUPDATECONTRACTLABEL'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGUPDATECONTRACTLABEL'].fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATECONTRACTLABEL'].fields_by_name['contract']._loaded_options = None
  _globals['_MSGUPDATECONTRACTLABEL'].fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATECONTRACTLABEL']._loaded_options = None
  _globals['_MSGUPDATECONTRACTLABEL']._serialized_options = b'\202\347\260*\006sender\212\347\260*\033wasm/MsgUpdateContractLabel'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGSTORECODE']._serialized_start=203
  _globals['_MSGSTORECODE']._serialized_end=457
  _globals['_MSGSTORECODERESPONSE']._serialized_start=459
  _globals['_MSGSTORECODERESPONSE']._serialized_end=546
  _globals['_MSGINSTANTIATECONTRACT']._serialized_start=549
  _globals['_MSGINSTANTIATECONTRACT']._serialized_end=954
  _globals['_MSGINSTANTIATECONTRACTRESPONSE']._serialized_start=956
  _globals['_MSGINSTANTIATECONTRACTRESPONSE']._serialized_end=1060
  _globals['_MSGINSTANTIATECONTRACT2']._serialized_start=1063
  _globals['_MSGINSTANTIATECONTRACT2']._serialized_end=1515
  _globals['_MSGINSTANTIATECONTRACT2RESPONSE']._serialized_start=1517
  _globals['_MSGINSTANTIATECONTRACT2RESPONSE']._serialized_end=1622
  _globals['_MSGEXECUTECONTRACT']._serialized_start=1625
  _globals['_MSGEXECUTECONTRACT']._serialized_end=1969
  _globals['_MSGEXECUTECONTRACTRESPONSE']._serialized_start=1971
  _globals['_MSGEXECUTECONTRACTRESPONSE']._serialized_end=2019
  _globals['_MSGMIGRATECONTRACT']._serialized_start=2022
  _globals['_MSGMIGRATECONTRACT']._serialized_end=2282
  _globals['_MSGMIGRATECONTRACTRESPONSE']._serialized_start=2284
  _globals['_MSGMIGRATECONTRACTRESPONSE']._serialized_end=2332
  _globals['_MSGUPDATEADMIN']._serialized_start=2335
  _globals['_MSGUPDATEADMIN']._serialized_end=2547
  _globals['_MSGUPDATEADMINRESPONSE']._serialized_start=2549
  _globals['_MSGUPDATEADMINRESPONSE']._serialized_end=2573
  _globals['_MSGCLEARADMIN']._serialized_start=2576
  _globals['_MSGCLEARADMIN']._serialized_end=2731
  _globals['_MSGCLEARADMINRESPONSE']._serialized_start=2733
  _globals['_MSGCLEARADMINRESPONSE']._serialized_end=2756
  _globals['_MSGUPDATEINSTANTIATECONFIG']._serialized_start=2759
  _globals['_MSGUPDATEINSTANTIATECONFIG']._serialized_end=3017
  _globals['_MSGUPDATEINSTANTIATECONFIGRESPONSE']._serialized_start=3019
  _globals['_MSGUPDATEINSTANTIATECONFIGRESPONSE']._serialized_end=3055
  _globals['_MSGUPDATEPARAMS']._serialized_start=3058
  _globals['_MSGUPDATEPARAMS']._serialized_end=3233
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=3235
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=3260
  _globals['_MSGSUDOCONTRACT']._serialized_start=3263
  _globals['_MSGSUDOCONTRACT']._serialized_end=3489
  _globals['_MSGSUDOCONTRACTRESPONSE']._serialized_start=3491
  _globals['_MSGSUDOCONTRACTRESPONSE']._serialized_end=3536
  _globals['_MSGPINCODES']._serialized_start=3539
  _globals['_MSGPINCODES']._serialized_end=3704
  _globals['_MSGPINCODESRESPONSE']._serialized_start=3706
  _globals['_MSGPINCODESRESPONSE']._serialized_end=3727
  _globals['_MSGUNPINCODES']._serialized_start=3730
  _globals['_MSGUNPINCODES']._serialized_end=3899
  _globals['_MSGUNPINCODESRESPONSE']._serialized_start=3901
  _globals['_MSGUNPINCODESRESPONSE']._serialized_end=3924
  _globals['_MSGSTOREANDINSTANTIATECONTRACT']._serialized_start=3927
  _globals['_MSGSTOREANDINSTANTIATECONTRACT']._serialized_end=4573
  _globals['_MSGSTOREANDINSTANTIATECONTRACTRESPONSE']._serialized_start=4575
  _globals['_MSGSTOREANDINSTANTIATECONTRACTRESPONSE']._serialized_end=4687
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSES']._serialized_start=4690
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSES']._serialized_end=4888
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSESRESPONSE']._serialized_start=4890
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSESRESPONSE']._serialized_end=4931
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSES']._serialized_start=4934
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSES']._serialized_end=5138
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSESRESPONSE']._serialized_start=5140
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSESRESPONSE']._serialized_end=5184
  _globals['_MSGSTOREANDMIGRATECONTRACT']._serialized_start=5187
  _globals['_MSGSTOREANDMIGRATECONTRACT']._serialized_end=5552
  _globals['_MSGSTOREANDMIGRATECONTRACTRESPONSE']._serialized_start=5554
  _globals['_MSGSTOREANDMIGRATECONTRACTRESPONSE']._serialized_end=5675
  _globals['_MSGUPDATECONTRACTLABEL']._serialized_start=5678
  _globals['_MSGUPDATECONTRACTLABEL']._serialized_end=5880
  _globals['_MSGUPDATECONTRACTLABELRESPONSE']._serialized_start=5882
  _globals['_MSGUPDATECONTRACTLABELRESPONSE']._serialized_end=5914
  _globals['_MSG']._serialized_start=5917
  _globals['_MSG']._serialized_end=7794
# @@protoc_insertion_point(module_scope)
