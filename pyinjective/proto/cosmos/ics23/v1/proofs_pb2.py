# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/ics23/v1/proofs.proto
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
    'cosmos/ics23/v1/proofs.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63osmos/ics23/v1/proofs.proto\x12\x0f\x63osmos.ics23.v1\"\x93\x01\n\x0e\x45xistenceProof\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x0cR\x05value\x12+\n\x04leaf\x18\x03 \x01(\x0b\x32\x17.cosmos.ics23.v1.LeafOpR\x04leaf\x12,\n\x04path\x18\x04 \x03(\x0b\x32\x18.cosmos.ics23.v1.InnerOpR\x04path\"\x91\x01\n\x11NonExistenceProof\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\x12\x33\n\x04left\x18\x02 \x01(\x0b\x32\x1f.cosmos.ics23.v1.ExistenceProofR\x04left\x12\x35\n\x05right\x18\x03 \x01(\x0b\x32\x1f.cosmos.ics23.v1.ExistenceProofR\x05right\"\x93\x02\n\x0f\x43ommitmentProof\x12\x37\n\x05\x65xist\x18\x01 \x01(\x0b\x32\x1f.cosmos.ics23.v1.ExistenceProofH\x00R\x05\x65xist\x12@\n\x08nonexist\x18\x02 \x01(\x0b\x32\".cosmos.ics23.v1.NonExistenceProofH\x00R\x08nonexist\x12\x33\n\x05\x62\x61tch\x18\x03 \x01(\x0b\x32\x1b.cosmos.ics23.v1.BatchProofH\x00R\x05\x62\x61tch\x12G\n\ncompressed\x18\x04 \x01(\x0b\x32%.cosmos.ics23.v1.CompressedBatchProofH\x00R\ncompressedB\x07\n\x05proof\"\xf8\x01\n\x06LeafOp\x12+\n\x04hash\x18\x01 \x01(\x0e\x32\x17.cosmos.ics23.v1.HashOpR\x04hash\x12\x38\n\x0bprehash_key\x18\x02 \x01(\x0e\x32\x17.cosmos.ics23.v1.HashOpR\nprehashKey\x12<\n\rprehash_value\x18\x03 \x01(\x0e\x32\x17.cosmos.ics23.v1.HashOpR\x0cprehashValue\x12\x31\n\x06length\x18\x04 \x01(\x0e\x32\x19.cosmos.ics23.v1.LengthOpR\x06length\x12\x16\n\x06prefix\x18\x05 \x01(\x0cR\x06prefix\"f\n\x07InnerOp\x12+\n\x04hash\x18\x01 \x01(\x0e\x32\x17.cosmos.ics23.v1.HashOpR\x04hash\x12\x16\n\x06prefix\x18\x02 \x01(\x0cR\x06prefix\x12\x16\n\x06suffix\x18\x03 \x01(\x0cR\x06suffix\"\xf9\x01\n\tProofSpec\x12\x34\n\tleaf_spec\x18\x01 \x01(\x0b\x32\x17.cosmos.ics23.v1.LeafOpR\x08leafSpec\x12\x39\n\ninner_spec\x18\x02 \x01(\x0b\x32\x1a.cosmos.ics23.v1.InnerSpecR\tinnerSpec\x12\x1b\n\tmax_depth\x18\x03 \x01(\x05R\x08maxDepth\x12\x1b\n\tmin_depth\x18\x04 \x01(\x05R\x08minDepth\x12\x41\n\x1dprehash_key_before_comparison\x18\x05 \x01(\x08R\x1aprehashKeyBeforeComparison\"\xf1\x01\n\tInnerSpec\x12\x1f\n\x0b\x63hild_order\x18\x01 \x03(\x05R\nchildOrder\x12\x1d\n\nchild_size\x18\x02 \x01(\x05R\tchildSize\x12*\n\x11min_prefix_length\x18\x03 \x01(\x05R\x0fminPrefixLength\x12*\n\x11max_prefix_length\x18\x04 \x01(\x05R\x0fmaxPrefixLength\x12\x1f\n\x0b\x65mpty_child\x18\x05 \x01(\x0cR\nemptyChild\x12+\n\x04hash\x18\x06 \x01(\x0e\x32\x17.cosmos.ics23.v1.HashOpR\x04hash\"C\n\nBatchProof\x12\x35\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1b.cosmos.ics23.v1.BatchEntryR\x07\x65ntries\"\x90\x01\n\nBatchEntry\x12\x37\n\x05\x65xist\x18\x01 \x01(\x0b\x32\x1f.cosmos.ics23.v1.ExistenceProofH\x00R\x05\x65xist\x12@\n\x08nonexist\x18\x02 \x01(\x0b\x32\".cosmos.ics23.v1.NonExistenceProofH\x00R\x08nonexistB\x07\n\x05proof\"\x96\x01\n\x14\x43ompressedBatchProof\x12?\n\x07\x65ntries\x18\x01 \x03(\x0b\x32%.cosmos.ics23.v1.CompressedBatchEntryR\x07\x65ntries\x12=\n\rlookup_inners\x18\x02 \x03(\x0b\x32\x18.cosmos.ics23.v1.InnerOpR\x0clookupInners\"\xae\x01\n\x14\x43ompressedBatchEntry\x12\x41\n\x05\x65xist\x18\x01 \x01(\x0b\x32).cosmos.ics23.v1.CompressedExistenceProofH\x00R\x05\x65xist\x12J\n\x08nonexist\x18\x02 \x01(\x0b\x32,.cosmos.ics23.v1.CompressedNonExistenceProofH\x00R\x08nonexistB\x07\n\x05proof\"\x83\x01\n\x18\x43ompressedExistenceProof\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x0cR\x05value\x12+\n\x04leaf\x18\x03 \x01(\x0b\x32\x17.cosmos.ics23.v1.LeafOpR\x04leaf\x12\x12\n\x04path\x18\x04 \x03(\x05R\x04path\"\xaf\x01\n\x1b\x43ompressedNonExistenceProof\x12\x10\n\x03key\x18\x01 \x01(\x0cR\x03key\x12=\n\x04left\x18\x02 \x01(\x0b\x32).cosmos.ics23.v1.CompressedExistenceProofR\x04left\x12?\n\x05right\x18\x03 \x01(\x0b\x32).cosmos.ics23.v1.CompressedExistenceProofR\x05right*\x96\x01\n\x06HashOp\x12\x0b\n\x07NO_HASH\x10\x00\x12\n\n\x06SHA256\x10\x01\x12\n\n\x06SHA512\x10\x02\x12\r\n\tKECCAK256\x10\x03\x12\r\n\tRIPEMD160\x10\x04\x12\x0b\n\x07\x42ITCOIN\x10\x05\x12\x0e\n\nSHA512_256\x10\x06\x12\x0f\n\x0b\x42LAKE2B_512\x10\x07\x12\x0f\n\x0b\x42LAKE2S_256\x10\x08\x12\n\n\x06\x42LAKE3\x10\t*\xab\x01\n\x08LengthOp\x12\r\n\tNO_PREFIX\x10\x00\x12\r\n\tVAR_PROTO\x10\x01\x12\x0b\n\x07VAR_RLP\x10\x02\x12\x0f\n\x0b\x46IXED32_BIG\x10\x03\x12\x12\n\x0e\x46IXED32_LITTLE\x10\x04\x12\x0f\n\x0b\x46IXED64_BIG\x10\x05\x12\x12\n\x0e\x46IXED64_LITTLE\x10\x06\x12\x14\n\x10REQUIRE_32_BYTES\x10\x07\x12\x14\n\x10REQUIRE_64_BYTES\x10\x08\x42\xa2\x01\n\x13\x63om.cosmos.ics23.v1B\x0bProofsProtoP\x01Z github.com/cosmos/ics23/go;ics23\xa2\x02\x03\x43IX\xaa\x02\x0f\x43osmos.Ics23.V1\xca\x02\x0f\x43osmos\\Ics23\\V1\xe2\x02\x1b\x43osmos\\Ics23\\V1\\GPBMetadata\xea\x02\x11\x43osmos::Ics23::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.ics23.v1.proofs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.cosmos.ics23.v1B\013ProofsProtoP\001Z github.com/cosmos/ics23/go;ics23\242\002\003CIX\252\002\017Cosmos.Ics23.V1\312\002\017Cosmos\\Ics23\\V1\342\002\033Cosmos\\Ics23\\V1\\GPBMetadata\352\002\021Cosmos::Ics23::V1'
  _globals['_HASHOP']._serialized_start=2335
  _globals['_HASHOP']._serialized_end=2485
  _globals['_LENGTHOP']._serialized_start=2488
  _globals['_LENGTHOP']._serialized_end=2659
  _globals['_EXISTENCEPROOF']._serialized_start=50
  _globals['_EXISTENCEPROOF']._serialized_end=197
  _globals['_NONEXISTENCEPROOF']._serialized_start=200
  _globals['_NONEXISTENCEPROOF']._serialized_end=345
  _globals['_COMMITMENTPROOF']._serialized_start=348
  _globals['_COMMITMENTPROOF']._serialized_end=623
  _globals['_LEAFOP']._serialized_start=626
  _globals['_LEAFOP']._serialized_end=874
  _globals['_INNEROP']._serialized_start=876
  _globals['_INNEROP']._serialized_end=978
  _globals['_PROOFSPEC']._serialized_start=981
  _globals['_PROOFSPEC']._serialized_end=1230
  _globals['_INNERSPEC']._serialized_start=1233
  _globals['_INNERSPEC']._serialized_end=1474
  _globals['_BATCHPROOF']._serialized_start=1476
  _globals['_BATCHPROOF']._serialized_end=1543
  _globals['_BATCHENTRY']._serialized_start=1546
  _globals['_BATCHENTRY']._serialized_end=1690
  _globals['_COMPRESSEDBATCHPROOF']._serialized_start=1693
  _globals['_COMPRESSEDBATCHPROOF']._serialized_end=1843
  _globals['_COMPRESSEDBATCHENTRY']._serialized_start=1846
  _globals['_COMPRESSEDBATCHENTRY']._serialized_end=2020
  _globals['_COMPRESSEDEXISTENCEPROOF']._serialized_start=2023
  _globals['_COMPRESSEDEXISTENCEPROOF']._serialized_end=2154
  _globals['_COMPRESSEDNONEXISTENCEPROOF']._serialized_start=2157
  _globals['_COMPRESSEDNONEXISTENCEPROOF']._serialized_end=2332
# @@protoc_insertion_point(module_scope)
