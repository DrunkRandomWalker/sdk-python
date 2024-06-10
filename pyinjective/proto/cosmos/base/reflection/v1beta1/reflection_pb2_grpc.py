# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from cosmos.base.reflection.v1beta1 import reflection_pb2 as cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2

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
        + f' but the generated code in cosmos/base/reflection/v1beta1/reflection_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ReflectionServiceStub(object):
    """ReflectionService defines a service for interface reflection.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAllInterfaces = channel.unary_unary(
                '/cosmos.base.reflection.v1beta1.ReflectionService/ListAllInterfaces',
                request_serializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListAllInterfacesRequest.SerializeToString,
                response_deserializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListAllInterfacesResponse.FromString,
                _registered_method=True)
        self.ListImplementations = channel.unary_unary(
                '/cosmos.base.reflection.v1beta1.ReflectionService/ListImplementations',
                request_serializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListImplementationsRequest.SerializeToString,
                response_deserializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListImplementationsResponse.FromString,
                _registered_method=True)


class ReflectionServiceServicer(object):
    """ReflectionService defines a service for interface reflection.
    """

    def ListAllInterfaces(self, request, context):
        """ListAllInterfaces lists all the interfaces registered in the interface
        registry.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListImplementations(self, request, context):
        """ListImplementations list all the concrete types that implement a given
        interface.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReflectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListAllInterfaces': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAllInterfaces,
                    request_deserializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListAllInterfacesRequest.FromString,
                    response_serializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListAllInterfacesResponse.SerializeToString,
            ),
            'ListImplementations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListImplementations,
                    request_deserializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListImplementationsRequest.FromString,
                    response_serializer=cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListImplementationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.base.reflection.v1beta1.ReflectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cosmos.base.reflection.v1beta1.ReflectionService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ReflectionService(object):
    """ReflectionService defines a service for interface reflection.
    """

    @staticmethod
    def ListAllInterfaces(request,
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
            '/cosmos.base.reflection.v1beta1.ReflectionService/ListAllInterfaces',
            cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListAllInterfacesRequest.SerializeToString,
            cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListAllInterfacesResponse.FromString,
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
    def ListImplementations(request,
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
            '/cosmos.base.reflection.v1beta1.ReflectionService/ListImplementations',
            cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListImplementationsRequest.SerializeToString,
            cosmos_dot_base_dot_reflection_dot_v1beta1_dot_reflection__pb2.ListImplementationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
