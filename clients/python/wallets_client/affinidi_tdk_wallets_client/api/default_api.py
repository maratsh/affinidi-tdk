# coding: utf-8

"""
    CloudWalletEssentials

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr

from affinidi_tdk_wallets_client.models.get_revocation_list_credential_result_dto import GetRevocationListCredentialResultDto

from affinidi_tdk_wallets_client.api_client import ApiClient
from affinidi_tdk_wallets_client.api_response import ApiResponse
from affinidi_tdk_wallets_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_revocation_credential_status(self, project_id : Annotated[StrictStr, Field(..., description="Description for projectId.")], wallet_id : Annotated[StrictStr, Field(..., description="Description for walletId.")], status_id : Annotated[StrictStr, Field(..., description="Description for statusId.")], **kwargs) -> GetRevocationListCredentialResultDto:  # noqa: E501
        """get_revocation_credential_status  # noqa: E501

        Get revocation status list as RevocationListCredential  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_revocation_credential_status(project_id, wallet_id, status_id, async_req=True)
        >>> result = thread.get()

        :param project_id: Description for projectId. (required)
        :type project_id: str
        :param wallet_id: Description for walletId. (required)
        :type wallet_id: str
        :param status_id: Description for statusId. (required)
        :type status_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetRevocationListCredentialResultDto
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_revocation_credential_status_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_revocation_credential_status_with_http_info(project_id, wallet_id, status_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_revocation_credential_status_with_http_info(self, project_id : Annotated[StrictStr, Field(..., description="Description for projectId.")], wallet_id : Annotated[StrictStr, Field(..., description="Description for walletId.")], status_id : Annotated[StrictStr, Field(..., description="Description for statusId.")], **kwargs) -> ApiResponse:  # noqa: E501
        """get_revocation_credential_status  # noqa: E501

        Get revocation status list as RevocationListCredential  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_revocation_credential_status_with_http_info(project_id, wallet_id, status_id, async_req=True)
        >>> result = thread.get()

        :param project_id: Description for projectId. (required)
        :type project_id: str
        :param wallet_id: Description for walletId. (required)
        :type wallet_id: str
        :param status_id: Description for statusId. (required)
        :type status_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetRevocationListCredentialResultDto, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'project_id',
            'wallet_id',
            'status_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_revocation_credential_status" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['project_id'] is not None:
            _path_params['projectId'] = _params['project_id']

        if _params['wallet_id'] is not None:
            _path_params['walletId'] = _params['wallet_id']

        if _params['status_id'] is not None:
            _path_params['statusId'] = _params['status_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ProjectTokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "GetRevocationListCredentialResultDto",
            '404': "NotFoundError",
        }

        return self.api_client.call_api(
            '/v1/projects/{projectId}/wallets/{walletId}/revocation-statuses/{statusId}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
