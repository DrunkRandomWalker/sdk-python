# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: testpb/bank_query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from pyinjective.proto.testpb import bank_pb2 as testpb_dot_bank__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17testpb/bank_query.proto\x12\x06testpb\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x11testpb/bank.proto\"3\n\x11GetBalanceRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\"4\n\x12GetBalanceResponse\x12\x1e\n\x05value\x18\x01 \x01(\x0b\x32\x0f.testpb.Balance\"\xd8\x04\n\x12ListBalanceRequest\x12;\n\x0cprefix_query\x18\x01 \x01(\x0b\x32#.testpb.ListBalanceRequest.IndexKeyH\x00\x12<\n\x0brange_query\x18\x02 \x01(\x0b\x32%.testpb.ListBalanceRequest.RangeQueryH\x00\x12:\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x1a\x8f\x02\n\x08IndexKey\x12I\n\raddress_denom\x18\x01 \x01(\x0b\x32\x30.testpb.ListBalanceRequest.IndexKey.AddressDenomH\x00\x12:\n\x05\x64\x65nom\x18\x02 \x01(\x0b\x32).testpb.ListBalanceRequest.IndexKey.DenomH\x00\x1aN\n\x0c\x41\x64\x64ressDenom\x12\x14\n\x07\x61\x64\x64ress\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x64\x65nom\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\n\n\x08_addressB\x08\n\x06_denom\x1a%\n\x05\x44\x65nom\x12\x12\n\x05\x64\x65nom\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_denomB\x05\n\x03key\x1ap\n\nRangeQuery\x12\x31\n\x04\x66rom\x18\x01 \x01(\x0b\x32#.testpb.ListBalanceRequest.IndexKey\x12/\n\x02to\x18\x02 \x01(\x0b\x32#.testpb.ListBalanceRequest.IndexKeyB\x07\n\x05query\"s\n\x13ListBalanceResponse\x12\x1f\n\x06values\x18\x01 \x03(\x0b\x32\x0f.testpb.Balance\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"!\n\x10GetSupplyRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"2\n\x11GetSupplyResponse\x12\x1d\n\x05value\x18\x01 \x01(\x0b\x32\x0e.testpb.Supply\"\xb6\x03\n\x11ListSupplyRequest\x12:\n\x0cprefix_query\x18\x01 \x01(\x0b\x32\".testpb.ListSupplyRequest.IndexKeyH\x00\x12;\n\x0brange_query\x18\x02 \x01(\x0b\x32$.testpb.ListSupplyRequest.RangeQueryH\x00\x12:\n\npagination\x18\x03 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x1as\n\x08IndexKey\x12\x39\n\x05\x64\x65nom\x18\x01 \x01(\x0b\x32(.testpb.ListSupplyRequest.IndexKey.DenomH\x00\x1a%\n\x05\x44\x65nom\x12\x12\n\x05\x64\x65nom\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_denomB\x05\n\x03key\x1an\n\nRangeQuery\x12\x30\n\x04\x66rom\x18\x01 \x01(\x0b\x32\".testpb.ListSupplyRequest.IndexKey\x12.\n\x02to\x18\x02 \x01(\x0b\x32\".testpb.ListSupplyRequest.IndexKeyB\x07\n\x05query\"q\n\x12ListSupplyResponse\x12\x1e\n\x06values\x18\x01 \x03(\x0b\x32\x0e.testpb.Supply\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xae\x02\n\x10\x42\x61nkQueryService\x12\x45\n\nGetBalance\x12\x19.testpb.GetBalanceRequest\x1a\x1a.testpb.GetBalanceResponse\"\x00\x12H\n\x0bListBalance\x12\x1a.testpb.ListBalanceRequest\x1a\x1b.testpb.ListBalanceResponse\"\x00\x12\x42\n\tGetSupply\x12\x18.testpb.GetSupplyRequest\x1a\x19.testpb.GetSupplyResponse\"\x00\x12\x45\n\nListSupply\x12\x19.testpb.ListSupplyRequest\x1a\x1a.testpb.ListSupplyResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'testpb.bank_query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETBALANCEREQUEST']._serialized_start=98
  _globals['_GETBALANCEREQUEST']._serialized_end=149
  _globals['_GETBALANCERESPONSE']._serialized_start=151
  _globals['_GETBALANCERESPONSE']._serialized_end=203
  _globals['_LISTBALANCEREQUEST']._serialized_start=206
  _globals['_LISTBALANCEREQUEST']._serialized_end=806
  _globals['_LISTBALANCEREQUEST_INDEXKEY']._serialized_start=412
  _globals['_LISTBALANCEREQUEST_INDEXKEY']._serialized_end=683
  _globals['_LISTBALANCEREQUEST_INDEXKEY_ADDRESSDENOM']._serialized_start=559
  _globals['_LISTBALANCEREQUEST_INDEXKEY_ADDRESSDENOM']._serialized_end=637
  _globals['_LISTBALANCEREQUEST_INDEXKEY_DENOM']._serialized_start=639
  _globals['_LISTBALANCEREQUEST_INDEXKEY_DENOM']._serialized_end=676
  _globals['_LISTBALANCEREQUEST_RANGEQUERY']._serialized_start=685
  _globals['_LISTBALANCEREQUEST_RANGEQUERY']._serialized_end=797
  _globals['_LISTBALANCERESPONSE']._serialized_start=808
  _globals['_LISTBALANCERESPONSE']._serialized_end=923
  _globals['_GETSUPPLYREQUEST']._serialized_start=925
  _globals['_GETSUPPLYREQUEST']._serialized_end=958
  _globals['_GETSUPPLYRESPONSE']._serialized_start=960
  _globals['_GETSUPPLYRESPONSE']._serialized_end=1010
  _globals['_LISTSUPPLYREQUEST']._serialized_start=1013
  _globals['_LISTSUPPLYREQUEST']._serialized_end=1451
  _globals['_LISTSUPPLYREQUEST_INDEXKEY']._serialized_start=1215
  _globals['_LISTSUPPLYREQUEST_INDEXKEY']._serialized_end=1330
  _globals['_LISTSUPPLYREQUEST_INDEXKEY_DENOM']._serialized_start=639
  _globals['_LISTSUPPLYREQUEST_INDEXKEY_DENOM']._serialized_end=676
  _globals['_LISTSUPPLYREQUEST_RANGEQUERY']._serialized_start=1332
  _globals['_LISTSUPPLYREQUEST_RANGEQUERY']._serialized_end=1442
  _globals['_LISTSUPPLYRESPONSE']._serialized_start=1453
  _globals['_LISTSUPPLYRESPONSE']._serialized_end=1566
  _globals['_BANKQUERYSERVICE']._serialized_start=1569
  _globals['_BANKQUERYSERVICE']._serialized_end=1871
# @@protoc_insertion_point(module_scope)
