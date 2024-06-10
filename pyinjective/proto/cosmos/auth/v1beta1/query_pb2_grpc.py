# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from cosmos.auth.v1beta1 import query_pb2 as cosmos_dot_auth_dot_v1beta1_dot_query__pb2

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
        + f' but the generated code in cosmos/auth/v1beta1/query_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Accounts = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/Accounts',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.FromString,
                _registered_method=True)
        self.Account = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/Account',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.FromString,
                _registered_method=True)
        self.AccountAddressByID = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/AccountAddressByID',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountAddressByIDRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountAddressByIDResponse.FromString,
                _registered_method=True)
        self.Params = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/Params',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
                _registered_method=True)
        self.ModuleAccounts = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/ModuleAccounts',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsResponse.FromString,
                _registered_method=True)
        self.ModuleAccountByName = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/ModuleAccountByName',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountByNameRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountByNameResponse.FromString,
                _registered_method=True)
        self.Bech32Prefix = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/Bech32Prefix',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixResponse.FromString,
                _registered_method=True)
        self.AddressBytesToString = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/AddressBytesToString',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringResponse.FromString,
                _registered_method=True)
        self.AddressStringToBytes = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/AddressStringToBytes',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesResponse.FromString,
                _registered_method=True)
        self.AccountInfo = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/AccountInfo',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountInfoRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountInfoResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Accounts(self, request, context):
        """Accounts returns all the existing accounts.

        When called from another module, this query might consume a high amount of
        gas if the pagination field is incorrectly set.

        Since: cosmos-sdk 0.43
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Account(self, request, context):
        """Account returns account details based on address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountAddressByID(self, request, context):
        """AccountAddressByID returns account address based on account number.

        Since: cosmos-sdk 0.46.2
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params queries all parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModuleAccounts(self, request, context):
        """ModuleAccounts returns all the existing module accounts.

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModuleAccountByName(self, request, context):
        """ModuleAccountByName returns the module account info by module name
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Bech32Prefix(self, request, context):
        """Bech32Prefix queries bech32Prefix

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddressBytesToString(self, request, context):
        """AddressBytesToString converts Account Address bytes to string

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddressStringToBytes(self, request, context):
        """AddressStringToBytes converts Address string to bytes

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountInfo(self, request, context):
        """AccountInfo queries account info which is common to all account types.

        Since: cosmos-sdk 0.47
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Accounts': grpc.unary_unary_rpc_method_handler(
                    servicer.Accounts,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.SerializeToString,
            ),
            'Account': grpc.unary_unary_rpc_method_handler(
                    servicer.Account,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.SerializeToString,
            ),
            'AccountAddressByID': grpc.unary_unary_rpc_method_handler(
                    servicer.AccountAddressByID,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountAddressByIDRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountAddressByIDResponse.SerializeToString,
            ),
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'ModuleAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.ModuleAccounts,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsResponse.SerializeToString,
            ),
            'ModuleAccountByName': grpc.unary_unary_rpc_method_handler(
                    servicer.ModuleAccountByName,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountByNameRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountByNameResponse.SerializeToString,
            ),
            'Bech32Prefix': grpc.unary_unary_rpc_method_handler(
                    servicer.Bech32Prefix,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixResponse.SerializeToString,
            ),
            'AddressBytesToString': grpc.unary_unary_rpc_method_handler(
                    servicer.AddressBytesToString,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringResponse.SerializeToString,
            ),
            'AddressStringToBytes': grpc.unary_unary_rpc_method_handler(
                    servicer.AddressStringToBytes,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesResponse.SerializeToString,
            ),
            'AccountInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.AccountInfo,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountInfoRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.auth.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cosmos.auth.v1beta1.Query', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Accounts(request,
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
            '/cosmos.auth.v1beta1.Query/Accounts',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.FromString,
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
    def Account(request,
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
            '/cosmos.auth.v1beta1.Query/Account',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.FromString,
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
    def AccountAddressByID(request,
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
            '/cosmos.auth.v1beta1.Query/AccountAddressByID',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountAddressByIDRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountAddressByIDResponse.FromString,
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
            '/cosmos.auth.v1beta1.Query/Params',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
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
    def ModuleAccounts(request,
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
            '/cosmos.auth.v1beta1.Query/ModuleAccounts',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsResponse.FromString,
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
    def ModuleAccountByName(request,
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
            '/cosmos.auth.v1beta1.Query/ModuleAccountByName',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountByNameRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountByNameResponse.FromString,
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
    def Bech32Prefix(request,
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
            '/cosmos.auth.v1beta1.Query/Bech32Prefix',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixResponse.FromString,
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
    def AddressBytesToString(request,
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
            '/cosmos.auth.v1beta1.Query/AddressBytesToString',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringResponse.FromString,
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
    def AddressStringToBytes(request,
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
            '/cosmos.auth.v1beta1.Query/AddressStringToBytes',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesResponse.FromString,
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
    def AccountInfo(request,
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
            '/cosmos.auth.v1beta1.Query/AccountInfo',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountInfoRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
