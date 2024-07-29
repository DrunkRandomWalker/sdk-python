# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/slashing/v1beta1/genesis.proto
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
    'cosmos/slashing/v1beta1/genesis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/slashing/v1beta1/genesis.proto\x12\x17\x63osmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&cosmos/slashing/v1beta1/slashing.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\x88\x02\n\x0cGenesisState\x12\x42\n\x06params\x18\x01 \x01(\x0b\x32\x1f.cosmos.slashing.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params\x12T\n\rsigning_infos\x18\x02 \x03(\x0b\x32$.cosmos.slashing.v1beta1.SigningInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0csigningInfos\x12^\n\rmissed_blocks\x18\x03 \x03(\x0b\x32..cosmos.slashing.v1beta1.ValidatorMissedBlocksB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0cmissedBlocks\"\xba\x01\n\x0bSigningInfo\x12;\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ConsensusAddressStringR\x07\x61\x64\x64ress\x12n\n\x16validator_signing_info\x18\x02 \x01(\x0b\x32-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x14validatorSigningInfo\"\xaa\x01\n\x15ValidatorMissedBlocks\x12;\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ConsensusAddressStringR\x07\x61\x64\x64ress\x12T\n\rmissed_blocks\x18\x02 \x03(\x0b\x32$.cosmos.slashing.v1beta1.MissedBlockB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0cmissedBlocks\";\n\x0bMissedBlock\x12\x14\n\x05index\x18\x01 \x01(\x03R\x05index\x12\x16\n\x06missed\x18\x02 \x01(\x08R\x06missedB\xd8\x01\n\x1b\x63om.cosmos.slashing.v1beta1B\x0cGenesisProtoP\x01Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa2\x02\x03\x43SX\xaa\x02\x17\x43osmos.Slashing.V1beta1\xca\x02\x17\x43osmos\\Slashing\\V1beta1\xe2\x02#Cosmos\\Slashing\\V1beta1\\GPBMetadata\xea\x02\x19\x43osmos::Slashing::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.slashing.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cosmos.slashing.v1beta1B\014GenesisProtoP\001Z-github.com/cosmos/cosmos-sdk/x/slashing/types\242\002\003CSX\252\002\027Cosmos.Slashing.V1beta1\312\002\027Cosmos\\Slashing\\V1beta1\342\002#Cosmos\\Slashing\\V1beta1\\GPBMetadata\352\002\031Cosmos::Slashing::V1beta1'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['signing_infos']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['signing_infos']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['missed_blocks']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['missed_blocks']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_SIGNINGINFO'].fields_by_name['address']._loaded_options = None
  _globals['_SIGNINGINFO'].fields_by_name['address']._serialized_options = b'\322\264-\035cosmos.ConsensusAddressString'
  _globals['_SIGNINGINFO'].fields_by_name['validator_signing_info']._loaded_options = None
  _globals['_SIGNINGINFO'].fields_by_name['validator_signing_info']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['address']._loaded_options = None
  _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['address']._serialized_options = b'\322\264-\035cosmos.ConsensusAddressString'
  _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['missed_blocks']._loaded_options = None
  _globals['_VALIDATORMISSEDBLOCKS'].fields_by_name['missed_blocks']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE']._serialized_start=175
  _globals['_GENESISSTATE']._serialized_end=439
  _globals['_SIGNINGINFO']._serialized_start=442
  _globals['_SIGNINGINFO']._serialized_end=628
  _globals['_VALIDATORMISSEDBLOCKS']._serialized_start=631
  _globals['_VALIDATORMISSEDBLOCKS']._serialized_end=801
  _globals['_MISSEDBLOCK']._serialized_start=803
  _globals['_MISSEDBLOCK']._serialized_end=862
# @@protoc_insertion_point(module_scope)
