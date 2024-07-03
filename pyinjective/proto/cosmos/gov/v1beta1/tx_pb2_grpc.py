# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.cosmos.gov.v1beta1 import tx_pb2 as cosmos_dot_gov_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the bank Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubmitProposal = channel.unary_unary(
                '/cosmos.gov.v1beta1.Msg/SubmitProposal',
                request_serializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgSubmitProposal.SerializeToString,
                response_deserializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgSubmitProposalResponse.FromString,
                )
        self.Vote = channel.unary_unary(
                '/cosmos.gov.v1beta1.Msg/Vote',
                request_serializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVote.SerializeToString,
                response_deserializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVoteResponse.FromString,
                )
        self.VoteWeighted = channel.unary_unary(
                '/cosmos.gov.v1beta1.Msg/VoteWeighted',
                request_serializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVoteWeighted.SerializeToString,
                response_deserializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVoteWeightedResponse.FromString,
                )
        self.Deposit = channel.unary_unary(
                '/cosmos.gov.v1beta1.Msg/Deposit',
                request_serializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgDeposit.SerializeToString,
                response_deserializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgDepositResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the bank Msg service.
    """

    def SubmitProposal(self, request, context):
        """SubmitProposal defines a method to create new proposal given a content.
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

        Since: cosmos-sdk 0.43
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


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubmitProposal': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitProposal,
                    request_deserializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgSubmitProposal.FromString,
                    response_serializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgSubmitProposalResponse.SerializeToString,
            ),
            'Vote': grpc.unary_unary_rpc_method_handler(
                    servicer.Vote,
                    request_deserializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVote.FromString,
                    response_serializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVoteResponse.SerializeToString,
            ),
            'VoteWeighted': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteWeighted,
                    request_deserializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVoteWeighted.FromString,
                    response_serializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVoteWeightedResponse.SerializeToString,
            ),
            'Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Deposit,
                    request_deserializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgDeposit.FromString,
                    response_serializer=cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgDepositResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.gov.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the bank Msg service.
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
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1beta1.Msg/SubmitProposal',
            cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgSubmitProposal.SerializeToString,
            cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgSubmitProposalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1beta1.Msg/Vote',
            cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVote.SerializeToString,
            cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1beta1.Msg/VoteWeighted',
            cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVoteWeighted.SerializeToString,
            cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgVoteWeightedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/cosmos.gov.v1beta1.Msg/Deposit',
            cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgDeposit.SerializeToString,
            cosmos_dot_gov_dot_v1beta1_dot_tx__pb2.MsgDepositResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
