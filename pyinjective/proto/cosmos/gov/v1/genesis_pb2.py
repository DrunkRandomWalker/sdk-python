# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.gov.v1 import gov_pb2 as cosmos_dot_gov_dot_v1_dot_gov__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63osmos/gov/v1/genesis.proto\x12\rcosmos.gov.v1\x1a\x17\x63osmos/gov/v1/gov.proto\"\xf5\x02\n\x0cGenesisState\x12\x1c\n\x14starting_proposal_id\x18\x01 \x01(\x04\x12(\n\x08\x64\x65posits\x18\x02 \x03(\x0b\x32\x16.cosmos.gov.v1.Deposit\x12\"\n\x05votes\x18\x03 \x03(\x0b\x32\x13.cosmos.gov.v1.Vote\x12*\n\tproposals\x18\x04 \x03(\x0b\x32\x17.cosmos.gov.v1.Proposal\x12\x38\n\x0e\x64\x65posit_params\x18\x05 \x01(\x0b\x32\x1c.cosmos.gov.v1.DepositParamsB\x02\x18\x01\x12\x36\n\rvoting_params\x18\x06 \x01(\x0b\x32\x1b.cosmos.gov.v1.VotingParamsB\x02\x18\x01\x12\x34\n\x0ctally_params\x18\x07 \x01(\x0b\x32\x1a.cosmos.gov.v1.TallyParamsB\x02\x18\x01\x12%\n\x06params\x18\x08 \x01(\x0b\x32\x15.cosmos.gov.v1.ParamsB-Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1'
  _GENESISSTATE.fields_by_name['deposit_params']._options = None
  _GENESISSTATE.fields_by_name['deposit_params']._serialized_options = b'\030\001'
  _GENESISSTATE.fields_by_name['voting_params']._options = None
  _GENESISSTATE.fields_by_name['voting_params']._serialized_options = b'\030\001'
  _GENESISSTATE.fields_by_name['tally_params']._options = None
  _GENESISSTATE.fields_by_name['tally_params']._serialized_options = b'\030\001'
  _globals['_GENESISSTATE']._serialized_start=72
  _globals['_GENESISSTATE']._serialized_end=445
# @@protoc_insertion_point(module_scope)
