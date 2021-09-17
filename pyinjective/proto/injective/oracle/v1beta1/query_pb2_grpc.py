# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective.oracle.v1beta1 import query_pb2 as injective_dot_oracle_dot_v1beta1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary(
                '/injective.oracle.v1beta1.Query/Params',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
                )
        self.BandRelayers = channel.unary_unary(
                '/injective.oracle.v1beta1.Query/BandRelayers',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandRelayersRequest.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandRelayersResponse.FromString,
                )
        self.BandPriceStates = channel.unary_unary(
                '/injective.oracle.v1beta1.Query/BandPriceStates',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandPriceStatesRequest.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandPriceStatesResponse.FromString,
                )
        self.BandIBCPriceStates = channel.unary_unary(
                '/injective.oracle.v1beta1.Query/BandIBCPriceStates',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandIBCPriceStatesRequest.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandIBCPriceStatesResponse.FromString,
                )
        self.PriceFeedPriceStates = channel.unary_unary(
                '/injective.oracle.v1beta1.Query/PriceFeedPriceStates',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryPriceFeedPriceStatesRequest.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryPriceFeedPriceStatesResponse.FromString,
                )
        self.CoinbasePriceStates = channel.unary_unary(
                '/injective.oracle.v1beta1.Query/CoinbasePriceStates',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryCoinbasePriceStatesRequest.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryCoinbasePriceStatesResponse.FromString,
                )
        self.OracleModuleState = channel.unary_unary(
                '/injective.oracle.v1beta1.Query/OracleModuleState',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Retrieves oracle params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BandRelayers(self, request, context):
        """Retrieves the band relayers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BandPriceStates(self, request, context):
        """Retrieves the state for all band price feeds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BandIBCPriceStates(self, request, context):
        """Retrieves the state for all band ibc price feeds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PriceFeedPriceStates(self, request, context):
        """Retrieves the state for all price feeds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CoinbasePriceStates(self, request, context):
        """Retrieves the state for all coinbase price feeds
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OracleModuleState(self, request, context):
        """Retrieves the entire oracle module's state
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'BandRelayers': grpc.unary_unary_rpc_method_handler(
                    servicer.BandRelayers,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandRelayersRequest.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandRelayersResponse.SerializeToString,
            ),
            'BandPriceStates': grpc.unary_unary_rpc_method_handler(
                    servicer.BandPriceStates,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandPriceStatesRequest.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandPriceStatesResponse.SerializeToString,
            ),
            'BandIBCPriceStates': grpc.unary_unary_rpc_method_handler(
                    servicer.BandIBCPriceStates,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandIBCPriceStatesRequest.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandIBCPriceStatesResponse.SerializeToString,
            ),
            'PriceFeedPriceStates': grpc.unary_unary_rpc_method_handler(
                    servicer.PriceFeedPriceStates,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryPriceFeedPriceStatesRequest.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryPriceFeedPriceStatesResponse.SerializeToString,
            ),
            'CoinbasePriceStates': grpc.unary_unary_rpc_method_handler(
                    servicer.CoinbasePriceStates,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryCoinbasePriceStatesRequest.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryCoinbasePriceStatesResponse.SerializeToString,
            ),
            'OracleModuleState': grpc.unary_unary_rpc_method_handler(
                    servicer.OracleModuleState,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.oracle.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Params(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Query/Params',
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BandRelayers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Query/BandRelayers',
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandRelayersRequest.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandRelayersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BandPriceStates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Query/BandPriceStates',
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandPriceStatesRequest.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandPriceStatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BandIBCPriceStates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Query/BandIBCPriceStates',
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandIBCPriceStatesRequest.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryBandIBCPriceStatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PriceFeedPriceStates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Query/PriceFeedPriceStates',
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryPriceFeedPriceStatesRequest.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryPriceFeedPriceStatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CoinbasePriceStates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Query/CoinbasePriceStates',
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryCoinbasePriceStatesRequest.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryCoinbasePriceStatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OracleModuleState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Query/OracleModuleState',
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryModuleStateRequest.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_query__pb2.QueryModuleStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
