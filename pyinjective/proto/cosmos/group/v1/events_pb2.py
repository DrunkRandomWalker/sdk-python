# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/group/v1/events.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmos.group.v1 import types_pb2 as cosmos_dot_group_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63osmos/group/v1/events.proto\x12\x0f\x63osmos.group.v1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1b\x63osmos/group/v1/types.proto\"$\n\x10\x45ventCreateGroup\x12\x10\n\x08group_id\x18\x01 \x01(\x04\"$\n\x10\x45ventUpdateGroup\x12\x10\n\x08group_id\x18\x01 \x01(\x04\"C\n\x16\x45ventCreateGroupPolicy\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"C\n\x16\x45ventUpdateGroupPolicy\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"*\n\x13\x45ventSubmitProposal\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\",\n\x15\x45ventWithdrawProposal\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\" \n\tEventVote\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\"g\n\tEventExec\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\x37\n\x06result\x18\x02 \x01(\x0e\x32\'.cosmos.group.v1.ProposalExecutorResult\x12\x0c\n\x04logs\x18\x03 \x01(\t\"N\n\x0f\x45ventLeaveGroup\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12)\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"\x8f\x01\n\x13\x45ventProposalPruned\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12/\n\x06status\x18\x02 \x01(\x0e\x32\x1f.cosmos.group.v1.ProposalStatus\x12\x32\n\x0ctally_result\x18\x03 \x01(\x0b\x32\x1c.cosmos.group.v1.TallyResultB&Z$github.com/cosmos/cosmos-sdk/x/groupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.group.v1.events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/group'
  _globals['_EVENTCREATEGROUPPOLICY'].fields_by_name['address']._options = None
  _globals['_EVENTCREATEGROUPPOLICY'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EVENTUPDATEGROUPPOLICY'].fields_by_name['address']._options = None
  _globals['_EVENTUPDATEGROUPPOLICY'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EVENTLEAVEGROUP'].fields_by_name['address']._options = None
  _globals['_EVENTLEAVEGROUP'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_EVENTCREATEGROUP']._serialized_start=105
  _globals['_EVENTCREATEGROUP']._serialized_end=141
  _globals['_EVENTUPDATEGROUP']._serialized_start=143
  _globals['_EVENTUPDATEGROUP']._serialized_end=179
  _globals['_EVENTCREATEGROUPPOLICY']._serialized_start=181
  _globals['_EVENTCREATEGROUPPOLICY']._serialized_end=248
  _globals['_EVENTUPDATEGROUPPOLICY']._serialized_start=250
  _globals['_EVENTUPDATEGROUPPOLICY']._serialized_end=317
  _globals['_EVENTSUBMITPROPOSAL']._serialized_start=319
  _globals['_EVENTSUBMITPROPOSAL']._serialized_end=361
  _globals['_EVENTWITHDRAWPROPOSAL']._serialized_start=363
  _globals['_EVENTWITHDRAWPROPOSAL']._serialized_end=407
  _globals['_EVENTVOTE']._serialized_start=409
  _globals['_EVENTVOTE']._serialized_end=441
  _globals['_EVENTEXEC']._serialized_start=443
  _globals['_EVENTEXEC']._serialized_end=546
  _globals['_EVENTLEAVEGROUP']._serialized_start=548
  _globals['_EVENTLEAVEGROUP']._serialized_end=626
  _globals['_EVENTPROPOSALPRUNED']._serialized_start=629
  _globals['_EVENTPROPOSALPRUNED']._serialized_end=772
# @@protoc_insertion_point(module_scope)
