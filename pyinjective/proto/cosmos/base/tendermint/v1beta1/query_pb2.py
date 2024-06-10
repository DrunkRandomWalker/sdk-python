# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/tendermint/v1beta1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from tendermint.p2p import types_pb2 as tendermint_dot_p2p_dot_types__pb2
from tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from cosmos.base.tendermint.v1beta1 import types_pb2 as cosmos_dot_base_dot_tendermint_dot_v1beta1_dot_types__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from tendermint.types import block_pb2 as tendermint_dot_types_dot_block__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cosmos/base/tendermint/v1beta1/query.proto\x12\x1e\x63osmos.base.tendermint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1atendermint/p2p/types.proto\x1a\x1ctendermint/types/types.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a*cosmos/base/tendermint/v1beta1/types.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1ctendermint/types/block.proto\x1a\x11\x61mino/amino.proto\"l\n\x1eGetValidatorSetByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xb3\x01\n\x1fGetValidatorSetByHeightResponse\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x03\x12=\n\nvalidators\x18\x02 \x03(\x0b\x32).cosmos.base.tendermint.v1beta1.Validator\x12;\n\npagination\x18\x03 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"Z\n\x1cGetLatestValidatorSetRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xb1\x01\n\x1dGetLatestValidatorSetResponse\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x03\x12=\n\nvalidators\x18\x02 \x03(\x0b\x32).cosmos.base.tendermint.v1beta1.Validator\x12;\n\npagination\x18\x03 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x8e\x01\n\tValidator\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12%\n\x07pub_key\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x14\n\x0cvoting_power\x18\x03 \x01(\x03\x12\x19\n\x11proposer_priority\x18\x04 \x01(\x03\")\n\x17GetBlockByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\"\xa9\x01\n\x18GetBlockByHeightResponse\x12+\n\x08\x62lock_id\x18\x01 \x01(\x0b\x32\x19.tendermint.types.BlockID\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tendermint.types.Block\x12\x38\n\tsdk_block\x18\x03 \x01(\x0b\x32%.cosmos.base.tendermint.v1beta1.Block\"\x17\n\x15GetLatestBlockRequest\"\xa7\x01\n\x16GetLatestBlockResponse\x12+\n\x08\x62lock_id\x18\x01 \x01(\x0b\x32\x19.tendermint.types.BlockID\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tendermint.types.Block\x12\x38\n\tsdk_block\x18\x03 \x01(\x0b\x32%.cosmos.base.tendermint.v1beta1.Block\"\x13\n\x11GetSyncingRequest\"%\n\x12GetSyncingResponse\x12\x0f\n\x07syncing\x18\x01 \x01(\x08\"\x14\n\x12GetNodeInfoRequest\"\x9b\x01\n\x13GetNodeInfoResponse\x12:\n\x11\x64\x65\x66\x61ult_node_info\x18\x01 \x01(\x0b\x32\x1f.tendermint.p2p.DefaultNodeInfo\x12H\n\x13\x61pplication_version\x18\x02 \x01(\x0b\x32+.cosmos.base.tendermint.v1beta1.VersionInfo\"\xd2\x01\n\x0bVersionInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x12\n\ngit_commit\x18\x04 \x01(\t\x12\x12\n\nbuild_tags\x18\x05 \x01(\t\x12\x12\n\ngo_version\x18\x06 \x01(\t\x12:\n\nbuild_deps\x18\x07 \x03(\x0b\x32&.cosmos.base.tendermint.v1beta1.Module\x12\x1a\n\x12\x63osmos_sdk_version\x18\x08 \x01(\t\"4\n\x06Module\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0b\n\x03sum\x18\x03 \x01(\t\"M\n\x10\x41\x42\x43IQueryRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\r\n\x05prove\x18\x04 \x01(\x08\"\xcd\x01\n\x11\x41\x42\x43IQueryResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\x0c\n\x04info\x18\x04 \x01(\t\x12\r\n\x05index\x18\x05 \x01(\x03\x12\x0b\n\x03key\x18\x06 \x01(\x0c\x12\r\n\x05value\x18\x07 \x01(\x0c\x12;\n\tproof_ops\x18\x08 \x01(\x0b\x32(.cosmos.base.tendermint.v1beta1.ProofOps\x12\x0e\n\x06height\x18\t \x01(\x03\x12\x11\n\tcodespace\x18\n \x01(\tJ\x04\x08\x02\x10\x03\"2\n\x07ProofOp\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"K\n\x08ProofOps\x12?\n\x03ops\x18\x01 \x03(\x0b\x32\'.cosmos.base.tendermint.v1beta1.ProofOpB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x32\xaf\n\n\x07Service\x12\xa9\x01\n\x0bGetNodeInfo\x12\x32.cosmos.base.tendermint.v1beta1.GetNodeInfoRequest\x1a\x33.cosmos.base.tendermint.v1beta1.GetNodeInfoResponse\"1\x82\xd3\xe4\x93\x02+\x12)/cosmos/base/tendermint/v1beta1/node_info\x12\xa4\x01\n\nGetSyncing\x12\x31.cosmos.base.tendermint.v1beta1.GetSyncingRequest\x1a\x32.cosmos.base.tendermint.v1beta1.GetSyncingResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/base/tendermint/v1beta1/syncing\x12\xb6\x01\n\x0eGetLatestBlock\x12\x35.cosmos.base.tendermint.v1beta1.GetLatestBlockRequest\x1a\x36.cosmos.base.tendermint.v1beta1.GetLatestBlockResponse\"5\x82\xd3\xe4\x93\x02/\x12-/cosmos/base/tendermint/v1beta1/blocks/latest\x12\xbe\x01\n\x10GetBlockByHeight\x12\x37.cosmos.base.tendermint.v1beta1.GetBlockByHeightRequest\x1a\x38.cosmos.base.tendermint.v1beta1.GetBlockByHeightResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//cosmos/base/tendermint/v1beta1/blocks/{height}\x12\xd2\x01\n\x15GetLatestValidatorSet\x12<.cosmos.base.tendermint.v1beta1.GetLatestValidatorSetRequest\x1a=.cosmos.base.tendermint.v1beta1.GetLatestValidatorSetResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/cosmos/base/tendermint/v1beta1/validatorsets/latest\x12\xda\x01\n\x17GetValidatorSetByHeight\x12>.cosmos.base.tendermint.v1beta1.GetValidatorSetByHeightRequest\x1a?.cosmos.base.tendermint.v1beta1.GetValidatorSetByHeightResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/cosmos/base/tendermint/v1beta1/validatorsets/{height}\x12\xa4\x01\n\tABCIQuery\x12\x30.cosmos.base.tendermint.v1beta1.ABCIQueryRequest\x1a\x31.cosmos.base.tendermint.v1beta1.ABCIQueryResponse\"2\x82\xd3\xe4\x93\x02,\x12*/cosmos/base/tendermint/v1beta1/abci_queryB5Z3github.com/cosmos/cosmos-sdk/client/grpc/cmtserviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.tendermint.v1beta1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/cosmos/cosmos-sdk/client/grpc/cmtservice'
  _globals['_VALIDATOR'].fields_by_name['address']._loaded_options = None
  _globals['_VALIDATOR'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_PROOFOPS'].fields_by_name['ops']._loaded_options = None
  _globals['_PROOFOPS'].fields_by_name['ops']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_SERVICE'].methods_by_name['GetNodeInfo']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['GetNodeInfo']._serialized_options = b'\202\323\344\223\002+\022)/cosmos/base/tendermint/v1beta1/node_info'
  _globals['_SERVICE'].methods_by_name['GetSyncing']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['GetSyncing']._serialized_options = b'\202\323\344\223\002)\022\'/cosmos/base/tendermint/v1beta1/syncing'
  _globals['_SERVICE'].methods_by_name['GetLatestBlock']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['GetLatestBlock']._serialized_options = b'\202\323\344\223\002/\022-/cosmos/base/tendermint/v1beta1/blocks/latest'
  _globals['_SERVICE'].methods_by_name['GetBlockByHeight']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['GetBlockByHeight']._serialized_options = b'\202\323\344\223\0021\022//cosmos/base/tendermint/v1beta1/blocks/{height}'
  _globals['_SERVICE'].methods_by_name['GetLatestValidatorSet']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['GetLatestValidatorSet']._serialized_options = b'\202\323\344\223\0026\0224/cosmos/base/tendermint/v1beta1/validatorsets/latest'
  _globals['_SERVICE'].methods_by_name['GetValidatorSetByHeight']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['GetValidatorSetByHeight']._serialized_options = b'\202\323\344\223\0028\0226/cosmos/base/tendermint/v1beta1/validatorsets/{height}'
  _globals['_SERVICE'].methods_by_name['ABCIQuery']._loaded_options = None
  _globals['_SERVICE'].methods_by_name['ABCIQuery']._serialized_options = b'\202\323\344\223\002,\022*/cosmos/base/tendermint/v1beta1/abci_query'
  _globals['_GETVALIDATORSETBYHEIGHTREQUEST']._serialized_start=379
  _globals['_GETVALIDATORSETBYHEIGHTREQUEST']._serialized_end=487
  _globals['_GETVALIDATORSETBYHEIGHTRESPONSE']._serialized_start=490
  _globals['_GETVALIDATORSETBYHEIGHTRESPONSE']._serialized_end=669
  _globals['_GETLATESTVALIDATORSETREQUEST']._serialized_start=671
  _globals['_GETLATESTVALIDATORSETREQUEST']._serialized_end=761
  _globals['_GETLATESTVALIDATORSETRESPONSE']._serialized_start=764
  _globals['_GETLATESTVALIDATORSETRESPONSE']._serialized_end=941
  _globals['_VALIDATOR']._serialized_start=944
  _globals['_VALIDATOR']._serialized_end=1086
  _globals['_GETBLOCKBYHEIGHTREQUEST']._serialized_start=1088
  _globals['_GETBLOCKBYHEIGHTREQUEST']._serialized_end=1129
  _globals['_GETBLOCKBYHEIGHTRESPONSE']._serialized_start=1132
  _globals['_GETBLOCKBYHEIGHTRESPONSE']._serialized_end=1301
  _globals['_GETLATESTBLOCKREQUEST']._serialized_start=1303
  _globals['_GETLATESTBLOCKREQUEST']._serialized_end=1326
  _globals['_GETLATESTBLOCKRESPONSE']._serialized_start=1329
  _globals['_GETLATESTBLOCKRESPONSE']._serialized_end=1496
  _globals['_GETSYNCINGREQUEST']._serialized_start=1498
  _globals['_GETSYNCINGREQUEST']._serialized_end=1517
  _globals['_GETSYNCINGRESPONSE']._serialized_start=1519
  _globals['_GETSYNCINGRESPONSE']._serialized_end=1556
  _globals['_GETNODEINFOREQUEST']._serialized_start=1558
  _globals['_GETNODEINFOREQUEST']._serialized_end=1578
  _globals['_GETNODEINFORESPONSE']._serialized_start=1581
  _globals['_GETNODEINFORESPONSE']._serialized_end=1736
  _globals['_VERSIONINFO']._serialized_start=1739
  _globals['_VERSIONINFO']._serialized_end=1949
  _globals['_MODULE']._serialized_start=1951
  _globals['_MODULE']._serialized_end=2003
  _globals['_ABCIQUERYREQUEST']._serialized_start=2005
  _globals['_ABCIQUERYREQUEST']._serialized_end=2082
  _globals['_ABCIQUERYRESPONSE']._serialized_start=2085
  _globals['_ABCIQUERYRESPONSE']._serialized_end=2290
  _globals['_PROOFOP']._serialized_start=2292
  _globals['_PROOFOP']._serialized_end=2342
  _globals['_PROOFOPS']._serialized_start=2344
  _globals['_PROOFOPS']._serialized_end=2419
  _globals['_SERVICE']._serialized_start=2422
  _globals['_SERVICE']._serialized_end=3749
# @@protoc_insertion_point(module_scope)
