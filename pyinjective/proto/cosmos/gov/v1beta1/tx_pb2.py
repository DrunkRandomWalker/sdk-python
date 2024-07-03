# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1beta1/tx.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63osmos/gov/v1beta1/tx.proto\x12\x12\x63osmos.gov.v1beta1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1c\x63osmos/gov/v1beta1/gov.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\"\xb1\x02\n\x11MsgSubmitProposal\x12\x45\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\x1e\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x12i\n\x0finitial_deposit\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01\x12*\n\x08proposer\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:>\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\x08proposer\x8a\xe7\xb0*\x1c\x63osmos-sdk/MsgSubmitProposal\"F\n\x19MsgSubmitProposalResponse\x12)\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x14\xea\xde\x1f\x0bproposal_id\xa8\xe7\xb0*\x01\"\xaa\x01\n\x07MsgVote\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12.\n\x06option\x18\x03 \x01(\x0e\x32\x1e.cosmos.gov.v1beta1.VoteOption:1\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\x05voter\x8a\xe7\xb0*\x12\x63osmos-sdk/MsgVote\"\x11\n\x0fMsgVoteResponse\"\xe4\x01\n\x0fMsgVoteWeighted\x12)\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x14\xea\xde\x1f\x0bproposal_id\xa8\xe7\xb0*\x01\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x42\n\x07options\x18\x03 \x03(\x0b\x32&.cosmos.gov.v1beta1.WeightedVoteOptionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:9\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\x05voter\x8a\xe7\xb0*\x1a\x63osmos-sdk/MsgVoteWeighted\"\x19\n\x17MsgVoteWeightedResponse\"\x80\x02\n\nMsgDeposit\x12)\n\x0bproposal_id\x18\x01 \x01(\x04\x42\x14\xea\xde\x1f\x0bproposal_id\xa8\xe7\xb0*\x01\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12`\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01:8\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\tdepositor\x8a\xe7\xb0*\x15\x63osmos-sdk/MsgDeposit\"\x14\n\x12MsgDepositResponse2\xf3\x02\n\x03Msg\x12\x66\n\x0eSubmitProposal\x12%.cosmos.gov.v1beta1.MsgSubmitProposal\x1a-.cosmos.gov.v1beta1.MsgSubmitProposalResponse\x12H\n\x04Vote\x12\x1b.cosmos.gov.v1beta1.MsgVote\x1a#.cosmos.gov.v1beta1.MsgVoteResponse\x12`\n\x0cVoteWeighted\x12#.cosmos.gov.v1beta1.MsgVoteWeighted\x1a+.cosmos.gov.v1beta1.MsgVoteWeightedResponse\x12Q\n\x07\x44\x65posit\x12\x1e.cosmos.gov.v1beta1.MsgDeposit\x1a&.cosmos.gov.v1beta1.MsgDepositResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x32Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1'
  _globals['_MSGSUBMITPROPOSAL'].fields_by_name['content']._options = None
  _globals['_MSGSUBMITPROPOSAL'].fields_by_name['content']._serialized_options = b'\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_MSGSUBMITPROPOSAL'].fields_by_name['initial_deposit']._options = None
  _globals['_MSGSUBMITPROPOSAL'].fields_by_name['initial_deposit']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _globals['_MSGSUBMITPROPOSAL'].fields_by_name['proposer']._options = None
  _globals['_MSGSUBMITPROPOSAL'].fields_by_name['proposer']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSUBMITPROPOSAL']._options = None
  _globals['_MSGSUBMITPROPOSAL']._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000\200\334 \000\202\347\260*\010proposer\212\347\260*\034cosmos-sdk/MsgSubmitProposal'
  _globals['_MSGSUBMITPROPOSALRESPONSE'].fields_by_name['proposal_id']._options = None
  _globals['_MSGSUBMITPROPOSALRESPONSE'].fields_by_name['proposal_id']._serialized_options = b'\352\336\037\013proposal_id\250\347\260*\001'
  _globals['_MSGVOTE'].fields_by_name['voter']._options = None
  _globals['_MSGVOTE'].fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGVOTE']._options = None
  _globals['_MSGVOTE']._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000\200\334 \000\202\347\260*\005voter\212\347\260*\022cosmos-sdk/MsgVote'
  _globals['_MSGVOTEWEIGHTED'].fields_by_name['proposal_id']._options = None
  _globals['_MSGVOTEWEIGHTED'].fields_by_name['proposal_id']._serialized_options = b'\352\336\037\013proposal_id\250\347\260*\001'
  _globals['_MSGVOTEWEIGHTED'].fields_by_name['voter']._options = None
  _globals['_MSGVOTEWEIGHTED'].fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGVOTEWEIGHTED'].fields_by_name['options']._options = None
  _globals['_MSGVOTEWEIGHTED'].fields_by_name['options']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGVOTEWEIGHTED']._options = None
  _globals['_MSGVOTEWEIGHTED']._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000\200\334 \000\202\347\260*\005voter\212\347\260*\032cosmos-sdk/MsgVoteWeighted'
  _globals['_MSGDEPOSIT'].fields_by_name['proposal_id']._options = None
  _globals['_MSGDEPOSIT'].fields_by_name['proposal_id']._serialized_options = b'\352\336\037\013proposal_id\250\347\260*\001'
  _globals['_MSGDEPOSIT'].fields_by_name['depositor']._options = None
  _globals['_MSGDEPOSIT'].fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGDEPOSIT'].fields_by_name['amount']._options = None
  _globals['_MSGDEPOSIT'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _globals['_MSGDEPOSIT']._options = None
  _globals['_MSGDEPOSIT']._serialized_options = b'\210\240\037\000\230\240\037\000\350\240\037\000\200\334 \000\202\347\260*\tdepositor\212\347\260*\025cosmos-sdk/MsgDeposit'
  _globals['_MSG']._options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGSUBMITPROPOSAL']._serialized_start=234
  _globals['_MSGSUBMITPROPOSAL']._serialized_end=539
  _globals['_MSGSUBMITPROPOSALRESPONSE']._serialized_start=541
  _globals['_MSGSUBMITPROPOSALRESPONSE']._serialized_end=611
  _globals['_MSGVOTE']._serialized_start=614
  _globals['_MSGVOTE']._serialized_end=784
  _globals['_MSGVOTERESPONSE']._serialized_start=786
  _globals['_MSGVOTERESPONSE']._serialized_end=803
  _globals['_MSGVOTEWEIGHTED']._serialized_start=806
  _globals['_MSGVOTEWEIGHTED']._serialized_end=1034
  _globals['_MSGVOTEWEIGHTEDRESPONSE']._serialized_start=1036
  _globals['_MSGVOTEWEIGHTEDRESPONSE']._serialized_end=1061
  _globals['_MSGDEPOSIT']._serialized_start=1064
  _globals['_MSGDEPOSIT']._serialized_end=1320
  _globals['_MSGDEPOSITRESPONSE']._serialized_start=1322
  _globals['_MSGDEPOSITRESPONSE']._serialized_end=1342
  _globals['_MSG']._serialized_start=1345
  _globals['_MSG']._serialized_end=1716
# @@protoc_insertion_point(module_scope)
