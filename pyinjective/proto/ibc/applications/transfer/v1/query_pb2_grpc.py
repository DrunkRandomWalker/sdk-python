# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.ibc.applications.transfer.v1 import query_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in ibc/applications/transfer/v1/query_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class QueryStub(object):
    """Query provides defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DenomTraces = channel.unary_unary(
                '/ibc.applications.transfer.v1.Query/DenomTraces',
                request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesResponse.FromString,
                _registered_method=True)
        self.DenomTrace = channel.unary_unary(
                '/ibc.applications.transfer.v1.Query/DenomTrace',
                request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceResponse.FromString,
                _registered_method=True)
        self.Params = channel.unary_unary(
                '/ibc.applications.transfer.v1.Query/Params',
                request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
                _registered_method=True)
        self.DenomHash = channel.unary_unary(
                '/ibc.applications.transfer.v1.Query/DenomHash',
                request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashResponse.FromString,
                _registered_method=True)
        self.EscrowAddress = channel.unary_unary(
                '/ibc.applications.transfer.v1.Query/EscrowAddress',
                request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressResponse.FromString,
                _registered_method=True)
        self.TotalEscrowForDenom = channel.unary_unary(
                '/ibc.applications.transfer.v1.Query/TotalEscrowForDenom',
                request_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryTotalEscrowForDenomRequest.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryTotalEscrowForDenomResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Query provides defines the gRPC querier service.
    """

    def DenomTraces(self, request, context):
        """DenomTraces queries all denomination traces.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomTrace(self, request, context):
        """DenomTrace queries a denomination trace information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params queries all parameters of the ibc-transfer module.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomHash(self, request, context):
        """DenomHash queries a denomination hash information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EscrowAddress(self, request, context):
        """EscrowAddress returns the escrow address for a particular port and channel id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalEscrowForDenom(self, request, context):
        """TotalEscrowForDenom returns the total amount of tokens in escrow based on the denom.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DenomTraces': grpc.unary_unary_rpc_method_handler(
                    servicer.DenomTraces,
                    request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesResponse.SerializeToString,
            ),
            'DenomTrace': grpc.unary_unary_rpc_method_handler(
                    servicer.DenomTrace,
                    request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceResponse.SerializeToString,
            ),
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'DenomHash': grpc.unary_unary_rpc_method_handler(
                    servicer.DenomHash,
                    request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashResponse.SerializeToString,
            ),
            'EscrowAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.EscrowAddress,
                    request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressResponse.SerializeToString,
            ),
            'TotalEscrowForDenom': grpc.unary_unary_rpc_method_handler(
                    servicer.TotalEscrowForDenom,
                    request_deserializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryTotalEscrowForDenomRequest.FromString,
                    response_serializer=ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryTotalEscrowForDenomResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ibc.applications.transfer.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ibc.applications.transfer.v1.Query', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query provides defines the gRPC querier service.
    """

    @staticmethod
    def DenomTraces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ibc.applications.transfer.v1.Query/DenomTraces',
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesRequest.SerializeToString,
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTracesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DenomTrace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ibc.applications.transfer.v1.Query/DenomTrace',
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceRequest.SerializeToString,
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomTraceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ibc.applications.transfer.v1.Query/Params',
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DenomHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ibc.applications.transfer.v1.Query/DenomHash',
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashRequest.SerializeToString,
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryDenomHashResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EscrowAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ibc.applications.transfer.v1.Query/EscrowAddress',
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressRequest.SerializeToString,
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryEscrowAddressResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def TotalEscrowForDenom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ibc.applications.transfer.v1.Query/TotalEscrowForDenom',
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryTotalEscrowForDenomRequest.SerializeToString,
            ibc_dot_applications_dot_transfer_dot_v1_dot_query__pb2.QueryTotalEscrowForDenomResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
