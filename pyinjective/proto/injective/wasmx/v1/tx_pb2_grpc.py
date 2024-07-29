# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.injective.wasmx.v1 import tx_pb2 as injective_dot_wasmx_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the wasmx Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateRegistryContractParams = channel.unary_unary(
                '/injective.wasmx.v1.Msg/UpdateRegistryContractParams',
                request_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateContract.SerializeToString,
                response_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateContractResponse.FromString,
                _registered_method=True)
        self.ActivateRegistryContract = channel.unary_unary(
                '/injective.wasmx.v1.Msg/ActivateRegistryContract',
                request_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgActivateContract.SerializeToString,
                response_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgActivateContractResponse.FromString,
                _registered_method=True)
        self.DeactivateRegistryContract = channel.unary_unary(
                '/injective.wasmx.v1.Msg/DeactivateRegistryContract',
                request_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgDeactivateContract.SerializeToString,
                response_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgDeactivateContractResponse.FromString,
                _registered_method=True)
        self.ExecuteContractCompat = channel.unary_unary(
                '/injective.wasmx.v1.Msg/ExecuteContractCompat',
                request_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgExecuteContractCompat.SerializeToString,
                response_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgExecuteContractCompatResponse.FromString,
                _registered_method=True)
        self.UpdateParams = channel.unary_unary(
                '/injective.wasmx.v1.Msg/UpdateParams',
                request_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
                response_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
                _registered_method=True)
        self.RegisterContract = channel.unary_unary(
                '/injective.wasmx.v1.Msg/RegisterContract',
                request_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgRegisterContract.SerializeToString,
                response_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgRegisterContractResponse.FromString,
                _registered_method=True)


class MsgServicer(object):
    """Msg defines the wasmx Msg service.
    """

    def UpdateRegistryContractParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActivateRegistryContract(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeactivateRegistryContract(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteContractCompat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterContract(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateRegistryContractParams': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRegistryContractParams,
                    request_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateContract.FromString,
                    response_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateContractResponse.SerializeToString,
            ),
            'ActivateRegistryContract': grpc.unary_unary_rpc_method_handler(
                    servicer.ActivateRegistryContract,
                    request_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgActivateContract.FromString,
                    response_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgActivateContractResponse.SerializeToString,
            ),
            'DeactivateRegistryContract': grpc.unary_unary_rpc_method_handler(
                    servicer.DeactivateRegistryContract,
                    request_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgDeactivateContract.FromString,
                    response_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgDeactivateContractResponse.SerializeToString,
            ),
            'ExecuteContractCompat': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteContractCompat,
                    request_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgExecuteContractCompat.FromString,
                    response_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgExecuteContractCompatResponse.SerializeToString,
            ),
            'UpdateParams': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateParams,
                    request_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateParams.FromString,
                    response_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateParamsResponse.SerializeToString,
            ),
            'RegisterContract': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterContract,
                    request_deserializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgRegisterContract.FromString,
                    response_serializer=injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgRegisterContractResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.wasmx.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective.wasmx.v1.Msg', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the wasmx Msg service.
    """

    @staticmethod
    def UpdateRegistryContractParams(request,
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
            '/injective.wasmx.v1.Msg/UpdateRegistryContractParams',
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateContract.SerializeToString,
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateContractResponse.FromString,
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
    def ActivateRegistryContract(request,
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
            '/injective.wasmx.v1.Msg/ActivateRegistryContract',
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgActivateContract.SerializeToString,
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgActivateContractResponse.FromString,
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
    def DeactivateRegistryContract(request,
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
            '/injective.wasmx.v1.Msg/DeactivateRegistryContract',
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgDeactivateContract.SerializeToString,
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgDeactivateContractResponse.FromString,
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
    def ExecuteContractCompat(request,
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
            '/injective.wasmx.v1.Msg/ExecuteContractCompat',
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgExecuteContractCompat.SerializeToString,
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgExecuteContractCompatResponse.FromString,
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
    def UpdateParams(request,
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
            '/injective.wasmx.v1.Msg/UpdateParams',
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
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
    def RegisterContract(request,
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
            '/injective.wasmx.v1.Msg/RegisterContract',
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgRegisterContract.SerializeToString,
            injective_dot_wasmx_dot_v1_dot_tx__pb2.MsgRegisterContractResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
