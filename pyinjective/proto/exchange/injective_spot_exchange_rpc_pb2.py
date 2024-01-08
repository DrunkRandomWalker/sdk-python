# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_spot_exchange_rpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*exchange/injective_spot_exchange_rpc.proto\x12\x1binjective_spot_exchange_rpc\"i\n\x0eMarketsRequest\x12\x15\n\rmarket_status\x18\x01 \x01(\t\x12\x12\n\nbase_denom\x18\x02 \x01(\t\x12\x13\n\x0bquote_denom\x18\x03 \x01(\t\x12\x17\n\x0fmarket_statuses\x18\x04 \x03(\t\"O\n\x0fMarketsResponse\x12<\n\x07markets\x18\x01 \x03(\x0b\x32+.injective_spot_exchange_rpc.SpotMarketInfo\"\x81\x03\n\x0eSpotMarketInfo\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x15\n\rmarket_status\x18\x02 \x01(\t\x12\x0e\n\x06ticker\x18\x03 \x01(\t\x12\x12\n\nbase_denom\x18\x04 \x01(\t\x12?\n\x0f\x62\x61se_token_meta\x18\x05 \x01(\x0b\x32&.injective_spot_exchange_rpc.TokenMeta\x12\x13\n\x0bquote_denom\x18\x06 \x01(\t\x12@\n\x10quote_token_meta\x18\x07 \x01(\x0b\x32&.injective_spot_exchange_rpc.TokenMeta\x12\x16\n\x0emaker_fee_rate\x18\x08 \x01(\t\x12\x16\n\x0etaker_fee_rate\x18\t \x01(\t\x12\x1c\n\x14service_provider_fee\x18\n \x01(\t\x12\x1b\n\x13min_price_tick_size\x18\x0b \x01(\t\x12\x1e\n\x16min_quantity_tick_size\x18\x0c \x01(\t\"n\n\tTokenMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12\x0c\n\x04logo\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x05 \x01(\x11\x12\x12\n\nupdated_at\x18\x06 \x01(\x12\"\"\n\rMarketRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\"M\n\x0eMarketResponse\x12;\n\x06market\x18\x01 \x01(\x0b\x32+.injective_spot_exchange_rpc.SpotMarketInfo\"*\n\x14StreamMarketsRequest\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"\x7f\n\x15StreamMarketsResponse\x12;\n\x06market\x18\x01 \x01(\x0b\x32+.injective_spot_exchange_rpc.SpotMarketInfo\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\"\'\n\x12OrderbookV2Request\x12\x11\n\tmarket_id\x18\x01 \x01(\t\"[\n\x13OrderbookV2Response\x12\x44\n\torderbook\x18\x01 \x01(\x0b\x32\x31.injective_spot_exchange_rpc.SpotLimitOrderbookV2\"\xaa\x01\n\x14SpotLimitOrderbookV2\x12\x35\n\x04\x62uys\x18\x01 \x03(\x0b\x32\'.injective_spot_exchange_rpc.PriceLevel\x12\x36\n\x05sells\x18\x02 \x03(\x0b\x32\'.injective_spot_exchange_rpc.PriceLevel\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x11\n\ttimestamp\x18\x04 \x01(\x12\"@\n\nPriceLevel\x12\r\n\x05price\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\")\n\x13OrderbooksV2Request\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"c\n\x14OrderbooksV2Response\x12K\n\norderbooks\x18\x01 \x03(\x0b\x32\x37.injective_spot_exchange_rpc.SingleSpotLimitOrderbookV2\"u\n\x1aSingleSpotLimitOrderbookV2\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x44\n\torderbook\x18\x02 \x01(\x0b\x32\x31.injective_spot_exchange_rpc.SpotLimitOrderbookV2\".\n\x18StreamOrderbookV2Request\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"\x9f\x01\n\x19StreamOrderbookV2Response\x12\x44\n\torderbook\x18\x01 \x01(\x0b\x32\x31.injective_spot_exchange_rpc.SpotLimitOrderbookV2\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\x12\x11\n\tmarket_id\x18\x04 \x01(\t\"2\n\x1cStreamOrderbookUpdateRequest\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"\xb2\x01\n\x1dStreamOrderbookUpdateResponse\x12S\n\x17orderbook_level_updates\x18\x01 \x01(\x0b\x32\x32.injective_spot_exchange_rpc.OrderbookLevelUpdates\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\x12\x11\n\tmarket_id\x18\x04 \x01(\t\"\xcb\x01\n\x15OrderbookLevelUpdates\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12;\n\x04\x62uys\x18\x03 \x03(\x0b\x32-.injective_spot_exchange_rpc.PriceLevelUpdate\x12<\n\x05sells\x18\x04 \x03(\x0b\x32-.injective_spot_exchange_rpc.PriceLevelUpdate\x12\x12\n\nupdated_at\x18\x05 \x01(\x12\"Y\n\x10PriceLevelUpdate\x12\r\n\x05price\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\t\x12\x11\n\tis_active\x18\x03 \x01(\x08\x12\x11\n\ttimestamp\x18\x04 \x01(\x12\"\xfe\x01\n\rOrdersRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x12\n\norder_side\x18\x02 \x01(\t\x12\x15\n\rsubaccount_id\x18\x03 \x01(\t\x12\x0c\n\x04skip\x18\x04 \x01(\x04\x12\r\n\x05limit\x18\x05 \x01(\x11\x12\x12\n\nstart_time\x18\x06 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x07 \x01(\x12\x12\x12\n\nmarket_ids\x18\x08 \x03(\t\x12\x18\n\x10include_inactive\x18\t \x01(\x08\x12\x1f\n\x17subaccount_total_orders\x18\n \x01(\x08\x12\x10\n\x08trade_id\x18\x0b \x01(\t\x12\x0b\n\x03\x63id\x18\x0c \x01(\t\"\x82\x01\n\x0eOrdersResponse\x12;\n\x06orders\x18\x01 \x03(\x0b\x32+.injective_spot_exchange_rpc.SpotLimitOrder\x12\x33\n\x06paging\x18\x02 \x01(\x0b\x32#.injective_spot_exchange_rpc.Paging\"\xa1\x02\n\x0eSpotLimitOrder\x12\x12\n\norder_hash\x18\x01 \x01(\t\x12\x12\n\norder_side\x18\x02 \x01(\t\x12\x11\n\tmarket_id\x18\x03 \x01(\t\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\t\x12\x10\n\x08quantity\x18\x06 \x01(\t\x12\x19\n\x11unfilled_quantity\x18\x07 \x01(\t\x12\x15\n\rtrigger_price\x18\x08 \x01(\t\x12\x15\n\rfee_recipient\x18\t \x01(\t\x12\r\n\x05state\x18\n \x01(\t\x12\x12\n\ncreated_at\x18\x0b \x01(\x12\x12\x12\n\nupdated_at\x18\x0c \x01(\x12\x12\x0f\n\x07tx_hash\x18\r \x01(\t\x12\x0b\n\x03\x63id\x18\x0e \x01(\t\"\\\n\x06Paging\x12\r\n\x05total\x18\x01 \x01(\x12\x12\x0c\n\x04\x66rom\x18\x02 \x01(\x11\x12\n\n\x02to\x18\x03 \x01(\x11\x12\x1b\n\x13\x63ount_by_subaccount\x18\x04 \x01(\x12\x12\x0c\n\x04next\x18\x05 \x03(\t\"\x84\x02\n\x13StreamOrdersRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x12\n\norder_side\x18\x02 \x01(\t\x12\x15\n\rsubaccount_id\x18\x03 \x01(\t\x12\x0c\n\x04skip\x18\x04 \x01(\x04\x12\r\n\x05limit\x18\x05 \x01(\x11\x12\x12\n\nstart_time\x18\x06 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x07 \x01(\x12\x12\x12\n\nmarket_ids\x18\x08 \x03(\t\x12\x18\n\x10include_inactive\x18\t \x01(\x08\x12\x1f\n\x17subaccount_total_orders\x18\n \x01(\x08\x12\x10\n\x08trade_id\x18\x0b \x01(\t\x12\x0b\n\x03\x63id\x18\x0c \x01(\t\"}\n\x14StreamOrdersResponse\x12:\n\x05order\x18\x01 \x01(\x0b\x32+.injective_spot_exchange_rpc.SpotLimitOrder\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\"\xa4\x02\n\rTradesRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x16\n\x0e\x65xecution_side\x18\x02 \x01(\t\x12\x11\n\tdirection\x18\x03 \x01(\t\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\x0c\n\x04skip\x18\x05 \x01(\x04\x12\r\n\x05limit\x18\x06 \x01(\x11\x12\x12\n\nstart_time\x18\x07 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x12\x12\x12\n\nmarket_ids\x18\t \x03(\t\x12\x16\n\x0esubaccount_ids\x18\n \x03(\t\x12\x17\n\x0f\x65xecution_types\x18\x0b \x03(\t\x12\x10\n\x08trade_id\x18\x0c \x01(\t\x12\x17\n\x0f\x61\x63\x63ount_address\x18\r \x01(\t\x12\x0b\n\x03\x63id\x18\x0e \x01(\t\"}\n\x0eTradesResponse\x12\x36\n\x06trades\x18\x01 \x03(\x0b\x32&.injective_spot_exchange_rpc.SpotTrade\x12\x33\n\x06paging\x18\x02 \x01(\x0b\x32#.injective_spot_exchange_rpc.Paging\"\xa8\x02\n\tSpotTrade\x12\x12\n\norder_hash\x18\x01 \x01(\t\x12\x15\n\rsubaccount_id\x18\x02 \x01(\t\x12\x11\n\tmarket_id\x18\x03 \x01(\t\x12\x1c\n\x14trade_execution_type\x18\x04 \x01(\t\x12\x17\n\x0ftrade_direction\x18\x05 \x01(\t\x12\x36\n\x05price\x18\x06 \x01(\x0b\x32\'.injective_spot_exchange_rpc.PriceLevel\x12\x0b\n\x03\x66\x65\x65\x18\x07 \x01(\t\x12\x13\n\x0b\x65xecuted_at\x18\x08 \x01(\x12\x12\x15\n\rfee_recipient\x18\t \x01(\t\x12\x10\n\x08trade_id\x18\n \x01(\t\x12\x16\n\x0e\x65xecution_side\x18\x0b \x01(\t\x12\x0b\n\x03\x63id\x18\x0c \x01(\t\"\xaa\x02\n\x13StreamTradesRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x16\n\x0e\x65xecution_side\x18\x02 \x01(\t\x12\x11\n\tdirection\x18\x03 \x01(\t\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\x0c\n\x04skip\x18\x05 \x01(\x04\x12\r\n\x05limit\x18\x06 \x01(\x11\x12\x12\n\nstart_time\x18\x07 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x12\x12\x12\n\nmarket_ids\x18\t \x03(\t\x12\x16\n\x0esubaccount_ids\x18\n \x03(\t\x12\x17\n\x0f\x65xecution_types\x18\x0b \x03(\t\x12\x10\n\x08trade_id\x18\x0c \x01(\t\x12\x17\n\x0f\x61\x63\x63ount_address\x18\r \x01(\t\x12\x0b\n\x03\x63id\x18\x0e \x01(\t\"x\n\x14StreamTradesResponse\x12\x35\n\x05trade\x18\x01 \x01(\x0b\x32&.injective_spot_exchange_rpc.SpotTrade\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\"\xa6\x02\n\x0fTradesV2Request\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x16\n\x0e\x65xecution_side\x18\x02 \x01(\t\x12\x11\n\tdirection\x18\x03 \x01(\t\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\x0c\n\x04skip\x18\x05 \x01(\x04\x12\r\n\x05limit\x18\x06 \x01(\x11\x12\x12\n\nstart_time\x18\x07 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x12\x12\x12\n\nmarket_ids\x18\t \x03(\t\x12\x16\n\x0esubaccount_ids\x18\n \x03(\t\x12\x17\n\x0f\x65xecution_types\x18\x0b \x03(\t\x12\x10\n\x08trade_id\x18\x0c \x01(\t\x12\x17\n\x0f\x61\x63\x63ount_address\x18\r \x01(\t\x12\x0b\n\x03\x63id\x18\x0e \x01(\t\"\x7f\n\x10TradesV2Response\x12\x36\n\x06trades\x18\x01 \x03(\x0b\x32&.injective_spot_exchange_rpc.SpotTrade\x12\x33\n\x06paging\x18\x02 \x01(\x0b\x32#.injective_spot_exchange_rpc.Paging\"\xac\x02\n\x15StreamTradesV2Request\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x16\n\x0e\x65xecution_side\x18\x02 \x01(\t\x12\x11\n\tdirection\x18\x03 \x01(\t\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\x0c\n\x04skip\x18\x05 \x01(\x04\x12\r\n\x05limit\x18\x06 \x01(\x11\x12\x12\n\nstart_time\x18\x07 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x12\x12\x12\n\nmarket_ids\x18\t \x03(\t\x12\x16\n\x0esubaccount_ids\x18\n \x03(\t\x12\x17\n\x0f\x65xecution_types\x18\x0b \x03(\t\x12\x10\n\x08trade_id\x18\x0c \x01(\t\x12\x17\n\x0f\x61\x63\x63ount_address\x18\r \x01(\t\x12\x0b\n\x03\x63id\x18\x0e \x01(\t\"z\n\x16StreamTradesV2Response\x12\x35\n\x05trade\x18\x01 \x01(\x0b\x32&.injective_spot_exchange_rpc.SpotTrade\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\"d\n\x1bSubaccountOrdersListRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x04\x12\r\n\x05limit\x18\x04 \x01(\x11\"\x90\x01\n\x1cSubaccountOrdersListResponse\x12;\n\x06orders\x18\x01 \x03(\x0b\x32+.injective_spot_exchange_rpc.SpotLimitOrder\x12\x33\n\x06paging\x18\x02 \x01(\x0b\x32#.injective_spot_exchange_rpc.Paging\"\x8f\x01\n\x1bSubaccountTradesListRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x16\n\x0e\x65xecution_type\x18\x03 \x01(\t\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x0c\n\x04skip\x18\x05 \x01(\x04\x12\r\n\x05limit\x18\x06 \x01(\x11\"V\n\x1cSubaccountTradesListResponse\x12\x36\n\x06trades\x18\x01 \x03(\x0b\x32&.injective_spot_exchange_rpc.SpotTrade\"\xa3\x02\n\x14OrdersHistoryRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x04\x12\r\n\x05limit\x18\x04 \x01(\x11\x12\x13\n\x0border_types\x18\x05 \x03(\t\x12\x11\n\tdirection\x18\x06 \x01(\t\x12\x12\n\nstart_time\x18\x07 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x12\x12\r\n\x05state\x18\t \x01(\t\x12\x17\n\x0f\x65xecution_types\x18\n \x03(\t\x12\x12\n\nmarket_ids\x18\x0b \x03(\t\x12\x10\n\x08trade_id\x18\x0c \x01(\t\x12\x1b\n\x13\x61\x63tive_markets_only\x18\r \x01(\x08\x12\x0b\n\x03\x63id\x18\x0e \x01(\t\"\x8b\x01\n\x15OrdersHistoryResponse\x12=\n\x06orders\x18\x01 \x03(\x0b\x32-.injective_spot_exchange_rpc.SpotOrderHistory\x12\x33\n\x06paging\x18\x02 \x01(\x0b\x32#.injective_spot_exchange_rpc.Paging\"\xc8\x02\n\x10SpotOrderHistory\x12\x12\n\norder_hash\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x11\n\tis_active\x18\x03 \x01(\x08\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\x16\n\x0e\x65xecution_type\x18\x05 \x01(\t\x12\x12\n\norder_type\x18\x06 \x01(\t\x12\r\n\x05price\x18\x07 \x01(\t\x12\x15\n\rtrigger_price\x18\x08 \x01(\t\x12\x10\n\x08quantity\x18\t \x01(\t\x12\x17\n\x0f\x66illed_quantity\x18\n \x01(\t\x12\r\n\x05state\x18\x0b \x01(\t\x12\x12\n\ncreated_at\x18\x0c \x01(\x12\x12\x12\n\nupdated_at\x18\r \x01(\x12\x12\x11\n\tdirection\x18\x0e \x01(\t\x12\x0f\n\x07tx_hash\x18\x0f \x01(\t\x12\x0b\n\x03\x63id\x18\x10 \x01(\t\"\x96\x01\n\x1aStreamOrdersHistoryRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x13\n\x0border_types\x18\x03 \x03(\t\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x17\n\x0f\x65xecution_types\x18\x06 \x03(\t\"\x86\x01\n\x1bStreamOrdersHistoryResponse\x12<\n\x05order\x18\x01 \x01(\x0b\x32-.injective_spot_exchange_rpc.SpotOrderHistory\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\"\x8a\x01\n\x18\x41tomicSwapHistoryRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x11\x12\r\n\x05limit\x18\x04 \x01(\x11\x12\x13\n\x0b\x66rom_number\x18\x05 \x01(\x11\x12\x11\n\tto_number\x18\x06 \x01(\x11\"\x87\x01\n\x19\x41tomicSwapHistoryResponse\x12\x33\n\x06paging\x18\x01 \x01(\x0b\x32#.injective_spot_exchange_rpc.Paging\x12\x35\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\'.injective_spot_exchange_rpc.AtomicSwap\"\xdc\x02\n\nAtomicSwap\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\r\n\x05route\x18\x02 \x01(\t\x12\x36\n\x0bsource_coin\x18\x03 \x01(\x0b\x32!.injective_spot_exchange_rpc.Coin\x12\x34\n\tdest_coin\x18\x04 \x01(\x0b\x32!.injective_spot_exchange_rpc.Coin\x12/\n\x04\x66\x65\x65s\x18\x05 \x03(\x0b\x32!.injective_spot_exchange_rpc.Coin\x12\x18\n\x10\x63ontract_address\x18\x06 \x01(\t\x12\x17\n\x0findex_by_sender\x18\x07 \x01(\x11\x12 \n\x18index_by_sender_contract\x18\x08 \x01(\x11\x12\x0f\n\x07tx_hash\x18\t \x01(\t\x12\x13\n\x0b\x65xecuted_at\x18\n \x01(\x12\x12\x15\n\rrefund_amount\x18\x0b \x01(\t\"%\n\x04\x43oin\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\t2\x9e\x11\n\x18InjectiveSpotExchangeRPC\x12\x64\n\x07Markets\x12+.injective_spot_exchange_rpc.MarketsRequest\x1a,.injective_spot_exchange_rpc.MarketsResponse\x12\x61\n\x06Market\x12*.injective_spot_exchange_rpc.MarketRequest\x1a+.injective_spot_exchange_rpc.MarketResponse\x12x\n\rStreamMarkets\x12\x31.injective_spot_exchange_rpc.StreamMarketsRequest\x1a\x32.injective_spot_exchange_rpc.StreamMarketsResponse0\x01\x12p\n\x0bOrderbookV2\x12/.injective_spot_exchange_rpc.OrderbookV2Request\x1a\x30.injective_spot_exchange_rpc.OrderbookV2Response\x12s\n\x0cOrderbooksV2\x12\x30.injective_spot_exchange_rpc.OrderbooksV2Request\x1a\x31.injective_spot_exchange_rpc.OrderbooksV2Response\x12\x84\x01\n\x11StreamOrderbookV2\x12\x35.injective_spot_exchange_rpc.StreamOrderbookV2Request\x1a\x36.injective_spot_exchange_rpc.StreamOrderbookV2Response0\x01\x12\x90\x01\n\x15StreamOrderbookUpdate\x12\x39.injective_spot_exchange_rpc.StreamOrderbookUpdateRequest\x1a:.injective_spot_exchange_rpc.StreamOrderbookUpdateResponse0\x01\x12\x61\n\x06Orders\x12*.injective_spot_exchange_rpc.OrdersRequest\x1a+.injective_spot_exchange_rpc.OrdersResponse\x12u\n\x0cStreamOrders\x12\x30.injective_spot_exchange_rpc.StreamOrdersRequest\x1a\x31.injective_spot_exchange_rpc.StreamOrdersResponse0\x01\x12\x61\n\x06Trades\x12*.injective_spot_exchange_rpc.TradesRequest\x1a+.injective_spot_exchange_rpc.TradesResponse\x12u\n\x0cStreamTrades\x12\x30.injective_spot_exchange_rpc.StreamTradesRequest\x1a\x31.injective_spot_exchange_rpc.StreamTradesResponse0\x01\x12g\n\x08TradesV2\x12,.injective_spot_exchange_rpc.TradesV2Request\x1a-.injective_spot_exchange_rpc.TradesV2Response\x12{\n\x0eStreamTradesV2\x12\x32.injective_spot_exchange_rpc.StreamTradesV2Request\x1a\x33.injective_spot_exchange_rpc.StreamTradesV2Response0\x01\x12\x8b\x01\n\x14SubaccountOrdersList\x12\x38.injective_spot_exchange_rpc.SubaccountOrdersListRequest\x1a\x39.injective_spot_exchange_rpc.SubaccountOrdersListResponse\x12\x8b\x01\n\x14SubaccountTradesList\x12\x38.injective_spot_exchange_rpc.SubaccountTradesListRequest\x1a\x39.injective_spot_exchange_rpc.SubaccountTradesListResponse\x12v\n\rOrdersHistory\x12\x31.injective_spot_exchange_rpc.OrdersHistoryRequest\x1a\x32.injective_spot_exchange_rpc.OrdersHistoryResponse\x12\x8a\x01\n\x13StreamOrdersHistory\x12\x37.injective_spot_exchange_rpc.StreamOrdersHistoryRequest\x1a\x38.injective_spot_exchange_rpc.StreamOrdersHistoryResponse0\x01\x12\x82\x01\n\x11\x41tomicSwapHistory\x12\x35.injective_spot_exchange_rpc.AtomicSwapHistoryRequest\x1a\x36.injective_spot_exchange_rpc.AtomicSwapHistoryResponseB Z\x1e/injective_spot_exchange_rpcpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_spot_exchange_rpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\036/injective_spot_exchange_rpcpb'
  _globals['_MARKETSREQUEST']._serialized_start=75
  _globals['_MARKETSREQUEST']._serialized_end=180
  _globals['_MARKETSRESPONSE']._serialized_start=182
  _globals['_MARKETSRESPONSE']._serialized_end=261
  _globals['_SPOTMARKETINFO']._serialized_start=264
  _globals['_SPOTMARKETINFO']._serialized_end=649
  _globals['_TOKENMETA']._serialized_start=651
  _globals['_TOKENMETA']._serialized_end=761
  _globals['_MARKETREQUEST']._serialized_start=763
  _globals['_MARKETREQUEST']._serialized_end=797
  _globals['_MARKETRESPONSE']._serialized_start=799
  _globals['_MARKETRESPONSE']._serialized_end=876
  _globals['_STREAMMARKETSREQUEST']._serialized_start=878
  _globals['_STREAMMARKETSREQUEST']._serialized_end=920
  _globals['_STREAMMARKETSRESPONSE']._serialized_start=922
  _globals['_STREAMMARKETSRESPONSE']._serialized_end=1049
  _globals['_ORDERBOOKV2REQUEST']._serialized_start=1051
  _globals['_ORDERBOOKV2REQUEST']._serialized_end=1090
  _globals['_ORDERBOOKV2RESPONSE']._serialized_start=1092
  _globals['_ORDERBOOKV2RESPONSE']._serialized_end=1183
  _globals['_SPOTLIMITORDERBOOKV2']._serialized_start=1186
  _globals['_SPOTLIMITORDERBOOKV2']._serialized_end=1356
  _globals['_PRICELEVEL']._serialized_start=1358
  _globals['_PRICELEVEL']._serialized_end=1422
  _globals['_ORDERBOOKSV2REQUEST']._serialized_start=1424
  _globals['_ORDERBOOKSV2REQUEST']._serialized_end=1465
  _globals['_ORDERBOOKSV2RESPONSE']._serialized_start=1467
  _globals['_ORDERBOOKSV2RESPONSE']._serialized_end=1566
  _globals['_SINGLESPOTLIMITORDERBOOKV2']._serialized_start=1568
  _globals['_SINGLESPOTLIMITORDERBOOKV2']._serialized_end=1685
  _globals['_STREAMORDERBOOKV2REQUEST']._serialized_start=1687
  _globals['_STREAMORDERBOOKV2REQUEST']._serialized_end=1733
  _globals['_STREAMORDERBOOKV2RESPONSE']._serialized_start=1736
  _globals['_STREAMORDERBOOKV2RESPONSE']._serialized_end=1895
  _globals['_STREAMORDERBOOKUPDATEREQUEST']._serialized_start=1897
  _globals['_STREAMORDERBOOKUPDATEREQUEST']._serialized_end=1947
  _globals['_STREAMORDERBOOKUPDATERESPONSE']._serialized_start=1950
  _globals['_STREAMORDERBOOKUPDATERESPONSE']._serialized_end=2128
  _globals['_ORDERBOOKLEVELUPDATES']._serialized_start=2131
  _globals['_ORDERBOOKLEVELUPDATES']._serialized_end=2334
  _globals['_PRICELEVELUPDATE']._serialized_start=2336
  _globals['_PRICELEVELUPDATE']._serialized_end=2425
  _globals['_ORDERSREQUEST']._serialized_start=2428
  _globals['_ORDERSREQUEST']._serialized_end=2682
  _globals['_ORDERSRESPONSE']._serialized_start=2685
  _globals['_ORDERSRESPONSE']._serialized_end=2815
  _globals['_SPOTLIMITORDER']._serialized_start=2818
  _globals['_SPOTLIMITORDER']._serialized_end=3107
  _globals['_PAGING']._serialized_start=3109
  _globals['_PAGING']._serialized_end=3201
  _globals['_STREAMORDERSREQUEST']._serialized_start=3204
  _globals['_STREAMORDERSREQUEST']._serialized_end=3464
  _globals['_STREAMORDERSRESPONSE']._serialized_start=3466
  _globals['_STREAMORDERSRESPONSE']._serialized_end=3591
  _globals['_TRADESREQUEST']._serialized_start=3594
  _globals['_TRADESREQUEST']._serialized_end=3886
  _globals['_TRADESRESPONSE']._serialized_start=3888
  _globals['_TRADESRESPONSE']._serialized_end=4013
  _globals['_SPOTTRADE']._serialized_start=4016
  _globals['_SPOTTRADE']._serialized_end=4312
  _globals['_STREAMTRADESREQUEST']._serialized_start=4315
  _globals['_STREAMTRADESREQUEST']._serialized_end=4613
  _globals['_STREAMTRADESRESPONSE']._serialized_start=4615
  _globals['_STREAMTRADESRESPONSE']._serialized_end=4735
  _globals['_TRADESV2REQUEST']._serialized_start=4738
  _globals['_TRADESV2REQUEST']._serialized_end=5032
  _globals['_TRADESV2RESPONSE']._serialized_start=5034
  _globals['_TRADESV2RESPONSE']._serialized_end=5161
  _globals['_STREAMTRADESV2REQUEST']._serialized_start=5164
  _globals['_STREAMTRADESV2REQUEST']._serialized_end=5464
  _globals['_STREAMTRADESV2RESPONSE']._serialized_start=5466
  _globals['_STREAMTRADESV2RESPONSE']._serialized_end=5588
  _globals['_SUBACCOUNTORDERSLISTREQUEST']._serialized_start=5590
  _globals['_SUBACCOUNTORDERSLISTREQUEST']._serialized_end=5690
  _globals['_SUBACCOUNTORDERSLISTRESPONSE']._serialized_start=5693
  _globals['_SUBACCOUNTORDERSLISTRESPONSE']._serialized_end=5837
  _globals['_SUBACCOUNTTRADESLISTREQUEST']._serialized_start=5840
  _globals['_SUBACCOUNTTRADESLISTREQUEST']._serialized_end=5983
  _globals['_SUBACCOUNTTRADESLISTRESPONSE']._serialized_start=5985
  _globals['_SUBACCOUNTTRADESLISTRESPONSE']._serialized_end=6071
  _globals['_ORDERSHISTORYREQUEST']._serialized_start=6074
  _globals['_ORDERSHISTORYREQUEST']._serialized_end=6365
  _globals['_ORDERSHISTORYRESPONSE']._serialized_start=6368
  _globals['_ORDERSHISTORYRESPONSE']._serialized_end=6507
  _globals['_SPOTORDERHISTORY']._serialized_start=6510
  _globals['_SPOTORDERHISTORY']._serialized_end=6838
  _globals['_STREAMORDERSHISTORYREQUEST']._serialized_start=6841
  _globals['_STREAMORDERSHISTORYREQUEST']._serialized_end=6991
  _globals['_STREAMORDERSHISTORYRESPONSE']._serialized_start=6994
  _globals['_STREAMORDERSHISTORYRESPONSE']._serialized_end=7128
  _globals['_ATOMICSWAPHISTORYREQUEST']._serialized_start=7131
  _globals['_ATOMICSWAPHISTORYREQUEST']._serialized_end=7269
  _globals['_ATOMICSWAPHISTORYRESPONSE']._serialized_start=7272
  _globals['_ATOMICSWAPHISTORYRESPONSE']._serialized_end=7407
  _globals['_ATOMICSWAP']._serialized_start=7410
  _globals['_ATOMICSWAP']._serialized_end=7758
  _globals['_COIN']._serialized_start=7760
  _globals['_COIN']._serialized_end=7797
  _globals['_INJECTIVESPOTEXCHANGERPC']._serialized_start=7800
  _globals['_INJECTIVESPOTEXCHANGERPC']._serialized_end=10006
# @@protoc_insertion_point(module_scope)
