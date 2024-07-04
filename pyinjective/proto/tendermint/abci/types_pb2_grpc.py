# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2


class ABCIStub(object):
    """NOTE: When using custom types, mind the warnings.
    https://github.com/cosmos/gogoproto/blob/master/custom_types.md#warnings-and-issues

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Echo = channel.unary_unary(
                '/tendermint.abci.ABCI/Echo',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestEcho.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseEcho.FromString,
                _registered_method=True)
        self.Flush = channel.unary_unary(
                '/tendermint.abci.ABCI/Flush',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestFlush.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseFlush.FromString,
                _registered_method=True)
        self.Info = channel.unary_unary(
                '/tendermint.abci.ABCI/Info',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestInfo.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseInfo.FromString,
                _registered_method=True)
        self.CheckTx = channel.unary_unary(
                '/tendermint.abci.ABCI/CheckTx',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestCheckTx.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseCheckTx.FromString,
                _registered_method=True)
        self.Query = channel.unary_unary(
                '/tendermint.abci.ABCI/Query',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestQuery.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseQuery.FromString,
                _registered_method=True)
        self.Commit = channel.unary_unary(
                '/tendermint.abci.ABCI/Commit',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestCommit.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseCommit.FromString,
                _registered_method=True)
        self.InitChain = channel.unary_unary(
                '/tendermint.abci.ABCI/InitChain',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestInitChain.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseInitChain.FromString,
                _registered_method=True)
        self.ListSnapshots = channel.unary_unary(
                '/tendermint.abci.ABCI/ListSnapshots',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestListSnapshots.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseListSnapshots.FromString,
                _registered_method=True)
        self.OfferSnapshot = channel.unary_unary(
                '/tendermint.abci.ABCI/OfferSnapshot',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestOfferSnapshot.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseOfferSnapshot.FromString,
                _registered_method=True)
        self.LoadSnapshotChunk = channel.unary_unary(
                '/tendermint.abci.ABCI/LoadSnapshotChunk',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestLoadSnapshotChunk.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseLoadSnapshotChunk.FromString,
                _registered_method=True)
        self.ApplySnapshotChunk = channel.unary_unary(
                '/tendermint.abci.ABCI/ApplySnapshotChunk',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestApplySnapshotChunk.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseApplySnapshotChunk.FromString,
                _registered_method=True)
        self.PrepareProposal = channel.unary_unary(
                '/tendermint.abci.ABCI/PrepareProposal',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestPrepareProposal.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponsePrepareProposal.FromString,
                _registered_method=True)
        self.ProcessProposal = channel.unary_unary(
                '/tendermint.abci.ABCI/ProcessProposal',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestProcessProposal.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseProcessProposal.FromString,
                _registered_method=True)
        self.ExtendVote = channel.unary_unary(
                '/tendermint.abci.ABCI/ExtendVote',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestExtendVote.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseExtendVote.FromString,
                _registered_method=True)
        self.VerifyVoteExtension = channel.unary_unary(
                '/tendermint.abci.ABCI/VerifyVoteExtension',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestVerifyVoteExtension.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseVerifyVoteExtension.FromString,
                _registered_method=True)
        self.FinalizeBlock = channel.unary_unary(
                '/tendermint.abci.ABCI/FinalizeBlock',
                request_serializer=tendermint_dot_abci_dot_types__pb2.RequestFinalizeBlock.SerializeToString,
                response_deserializer=tendermint_dot_abci_dot_types__pb2.ResponseFinalizeBlock.FromString,
                _registered_method=True)


class ABCIServicer(object):
    """NOTE: When using custom types, mind the warnings.
    https://github.com/cosmos/gogoproto/blob/master/custom_types.md#warnings-and-issues

    """

    def Echo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Flush(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckTx(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Commit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitChain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSnapshots(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OfferSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadSnapshotChunk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ApplySnapshotChunk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrepareProposal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProcessProposal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExtendVote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyVoteExtension(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinalizeBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ABCIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Echo': grpc.unary_unary_rpc_method_handler(
                    servicer.Echo,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestEcho.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseEcho.SerializeToString,
            ),
            'Flush': grpc.unary_unary_rpc_method_handler(
                    servicer.Flush,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestFlush.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseFlush.SerializeToString,
            ),
            'Info': grpc.unary_unary_rpc_method_handler(
                    servicer.Info,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestInfo.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseInfo.SerializeToString,
            ),
            'CheckTx': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckTx,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestCheckTx.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseCheckTx.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestQuery.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseQuery.SerializeToString,
            ),
            'Commit': grpc.unary_unary_rpc_method_handler(
                    servicer.Commit,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestCommit.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseCommit.SerializeToString,
            ),
            'InitChain': grpc.unary_unary_rpc_method_handler(
                    servicer.InitChain,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestInitChain.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseInitChain.SerializeToString,
            ),
            'ListSnapshots': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSnapshots,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestListSnapshots.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseListSnapshots.SerializeToString,
            ),
            'OfferSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.OfferSnapshot,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestOfferSnapshot.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseOfferSnapshot.SerializeToString,
            ),
            'LoadSnapshotChunk': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadSnapshotChunk,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestLoadSnapshotChunk.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseLoadSnapshotChunk.SerializeToString,
            ),
            'ApplySnapshotChunk': grpc.unary_unary_rpc_method_handler(
                    servicer.ApplySnapshotChunk,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestApplySnapshotChunk.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseApplySnapshotChunk.SerializeToString,
            ),
            'PrepareProposal': grpc.unary_unary_rpc_method_handler(
                    servicer.PrepareProposal,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestPrepareProposal.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponsePrepareProposal.SerializeToString,
            ),
            'ProcessProposal': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessProposal,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestProcessProposal.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseProcessProposal.SerializeToString,
            ),
            'ExtendVote': grpc.unary_unary_rpc_method_handler(
                    servicer.ExtendVote,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestExtendVote.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseExtendVote.SerializeToString,
            ),
            'VerifyVoteExtension': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyVoteExtension,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestVerifyVoteExtension.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseVerifyVoteExtension.SerializeToString,
            ),
            'FinalizeBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.FinalizeBlock,
                    request_deserializer=tendermint_dot_abci_dot_types__pb2.RequestFinalizeBlock.FromString,
                    response_serializer=tendermint_dot_abci_dot_types__pb2.ResponseFinalizeBlock.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tendermint.abci.ABCI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('tendermint.abci.ABCI', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ABCI(object):
    """NOTE: When using custom types, mind the warnings.
    https://github.com/cosmos/gogoproto/blob/master/custom_types.md#warnings-and-issues

    """

    @staticmethod
    def Echo(request,
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
            '/tendermint.abci.ABCI/Echo',
            tendermint_dot_abci_dot_types__pb2.RequestEcho.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseEcho.FromString,
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
    def Flush(request,
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
            '/tendermint.abci.ABCI/Flush',
            tendermint_dot_abci_dot_types__pb2.RequestFlush.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseFlush.FromString,
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
    def Info(request,
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
            '/tendermint.abci.ABCI/Info',
            tendermint_dot_abci_dot_types__pb2.RequestInfo.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseInfo.FromString,
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
    def CheckTx(request,
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
            '/tendermint.abci.ABCI/CheckTx',
            tendermint_dot_abci_dot_types__pb2.RequestCheckTx.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseCheckTx.FromString,
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
    def Query(request,
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
            '/tendermint.abci.ABCI/Query',
            tendermint_dot_abci_dot_types__pb2.RequestQuery.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseQuery.FromString,
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
    def Commit(request,
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
            '/tendermint.abci.ABCI/Commit',
            tendermint_dot_abci_dot_types__pb2.RequestCommit.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseCommit.FromString,
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
    def InitChain(request,
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
            '/tendermint.abci.ABCI/InitChain',
            tendermint_dot_abci_dot_types__pb2.RequestInitChain.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseInitChain.FromString,
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
    def ListSnapshots(request,
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
            '/tendermint.abci.ABCI/ListSnapshots',
            tendermint_dot_abci_dot_types__pb2.RequestListSnapshots.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseListSnapshots.FromString,
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
    def OfferSnapshot(request,
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
            '/tendermint.abci.ABCI/OfferSnapshot',
            tendermint_dot_abci_dot_types__pb2.RequestOfferSnapshot.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseOfferSnapshot.FromString,
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
    def LoadSnapshotChunk(request,
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
            '/tendermint.abci.ABCI/LoadSnapshotChunk',
            tendermint_dot_abci_dot_types__pb2.RequestLoadSnapshotChunk.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseLoadSnapshotChunk.FromString,
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
    def ApplySnapshotChunk(request,
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
            '/tendermint.abci.ABCI/ApplySnapshotChunk',
            tendermint_dot_abci_dot_types__pb2.RequestApplySnapshotChunk.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseApplySnapshotChunk.FromString,
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
    def PrepareProposal(request,
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
            '/tendermint.abci.ABCI/PrepareProposal',
            tendermint_dot_abci_dot_types__pb2.RequestPrepareProposal.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponsePrepareProposal.FromString,
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
    def ProcessProposal(request,
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
            '/tendermint.abci.ABCI/ProcessProposal',
            tendermint_dot_abci_dot_types__pb2.RequestProcessProposal.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseProcessProposal.FromString,
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
    def ExtendVote(request,
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
            '/tendermint.abci.ABCI/ExtendVote',
            tendermint_dot_abci_dot_types__pb2.RequestExtendVote.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseExtendVote.FromString,
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
    def VerifyVoteExtension(request,
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
            '/tendermint.abci.ABCI/VerifyVoteExtension',
            tendermint_dot_abci_dot_types__pb2.RequestVerifyVoteExtension.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseVerifyVoteExtension.FromString,
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
    def FinalizeBlock(request,
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
            '/tendermint.abci.ABCI/FinalizeBlock',
            tendermint_dot_abci_dot_types__pb2.RequestFinalizeBlock.SerializeToString,
            tendermint_dot_abci_dot_types__pb2.ResponseFinalizeBlock.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
