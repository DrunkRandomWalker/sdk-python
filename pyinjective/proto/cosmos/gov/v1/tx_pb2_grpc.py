# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.cosmos.gov.v1 import tx_pb2 as cosmos_dot_gov_dot_v1_dot_tx__pb2

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
        + f' but the generated code in cosmos/gov/v1/tx_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class MsgStub(object):
    """Msg defines the gov Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubmitProposal = channel.unary_unary(
                '/cosmos.gov.v1.Msg/SubmitProposal',
                request_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgSubmitProposal.SerializeToString,
                response_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgSubmitProposalResponse.FromString,
                _registered_method=True)
        self.ExecLegacyContent = channel.unary_unary(
                '/cosmos.gov.v1.Msg/ExecLegacyContent',
                request_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgExecLegacyContent.SerializeToString,
                response_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgExecLegacyContentResponse.FromString,
                _registered_method=True)
        self.Vote = channel.unary_unary(
                '/cosmos.gov.v1.Msg/Vote',
                request_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVote.SerializeToString,
                response_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVoteResponse.FromString,
                _registered_method=True)
        self.VoteWeighted = channel.unary_unary(
                '/cosmos.gov.v1.Msg/VoteWeighted',
                request_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVoteWeighted.SerializeToString,
                response_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVoteWeightedResponse.FromString,
                _registered_method=True)
        self.Deposit = channel.unary_unary(
                '/cosmos.gov.v1.Msg/Deposit',
                request_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgDeposit.SerializeToString,
                response_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgDepositResponse.FromString,
                _registered_method=True)
        self.UpdateParams = channel.unary_unary(
                '/cosmos.gov.v1.Msg/UpdateParams',
                request_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
                response_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
                _registered_method=True)


class MsgServicer(object):
    """Msg defines the gov Msg service.
    """

    def SubmitProposal(self, request, context):
        """SubmitProposal defines a method to create new proposal given the messages.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecLegacyContent(self, request, context):
        """ExecLegacyContent defines a Msg to be in included in a MsgSubmitProposal
        to execute a legacy content-based proposal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Vote(self, request, context):
        """Vote defines a method to add a vote on a specific proposal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteWeighted(self, request, context):
        """VoteWeighted defines a method to add a weighted vote on a specific proposal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deposit(self, request, context):
        """Deposit defines a method to add deposit on a specific proposal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateParams(self, request, context):
        """UpdateParams defines a governance operation for updating the x/gov module
        parameters. The authority is defined in the keeper.

        Since: cosmos-sdk 0.47
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubmitProposal': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitProposal,
                    request_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgSubmitProposal.FromString,
                    response_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgSubmitProposalResponse.SerializeToString,
            ),
            'ExecLegacyContent': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecLegacyContent,
                    request_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgExecLegacyContent.FromString,
                    response_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgExecLegacyContentResponse.SerializeToString,
            ),
            'Vote': grpc.unary_unary_rpc_method_handler(
                    servicer.Vote,
                    request_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVote.FromString,
                    response_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVoteResponse.SerializeToString,
            ),
            'VoteWeighted': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteWeighted,
                    request_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVoteWeighted.FromString,
                    response_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVoteWeightedResponse.SerializeToString,
            ),
            'Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Deposit,
                    request_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgDeposit.FromString,
                    response_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgDepositResponse.SerializeToString,
            ),
            'UpdateParams': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateParams,
                    request_deserializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgUpdateParams.FromString,
                    response_serializer=cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgUpdateParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.gov.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cosmos.gov.v1.Msg', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the gov Msg service.
    """

    @staticmethod
    def SubmitProposal(request,
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
            '/cosmos.gov.v1.Msg/SubmitProposal',
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgSubmitProposal.SerializeToString,
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgSubmitProposalResponse.FromString,
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
    def ExecLegacyContent(request,
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
            '/cosmos.gov.v1.Msg/ExecLegacyContent',
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgExecLegacyContent.SerializeToString,
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgExecLegacyContentResponse.FromString,
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
    def Vote(request,
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
            '/cosmos.gov.v1.Msg/Vote',
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVote.SerializeToString,
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVoteResponse.FromString,
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
    def VoteWeighted(request,
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
            '/cosmos.gov.v1.Msg/VoteWeighted',
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVoteWeighted.SerializeToString,
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgVoteWeightedResponse.FromString,
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
    def Deposit(request,
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
            '/cosmos.gov.v1.Msg/Deposit',
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgDeposit.SerializeToString,
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgDepositResponse.FromString,
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
            '/cosmos.gov.v1.Msg/UpdateParams',
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
            cosmos_dot_gov_dot_v1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
