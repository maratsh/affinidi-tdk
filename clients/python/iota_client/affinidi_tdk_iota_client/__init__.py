# coding: utf-8

# flake8: noqa

"""
    IotaService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from affinidi_tdk_iota_client.api.callback_api import CallbackApi
from affinidi_tdk_iota_client.api.configurations_api import ConfigurationsApi
from affinidi_tdk_iota_client.api.default_api import DefaultApi
from affinidi_tdk_iota_client.api.iota_api import IotaApi
from affinidi_tdk_iota_client.api.pex_query_api import PexQueryApi

# import ApiClient
from affinidi_tdk_iota_client.api_response import ApiResponse
from affinidi_tdk_iota_client.api_client import ApiClient
from affinidi_tdk_iota_client.configuration import Configuration
from affinidi_tdk_iota_client.exceptions import OpenApiException
from affinidi_tdk_iota_client.exceptions import ApiTypeError
from affinidi_tdk_iota_client.exceptions import ApiValueError
from affinidi_tdk_iota_client.exceptions import ApiKeyError
from affinidi_tdk_iota_client.exceptions import ApiAttributeError
from affinidi_tdk_iota_client.exceptions import ApiException

# import models into sdk package
from affinidi_tdk_iota_client.models.already_exists_error import AlreadyExistsError
from affinidi_tdk_iota_client.models.aws_exchange_credentials import AwsExchangeCredentials
from affinidi_tdk_iota_client.models.aws_exchange_credentials_ok import AwsExchangeCredentialsOK
from affinidi_tdk_iota_client.models.aws_exchange_credentials_project_token import AwsExchangeCredentialsProjectToken
from affinidi_tdk_iota_client.models.aws_exchange_credentials_project_token_ok import AwsExchangeCredentialsProjectTokenOK
from affinidi_tdk_iota_client.models.aws_exchange_credentials_project_token_ok_credentials import AwsExchangeCredentialsProjectTokenOKCredentials
from affinidi_tdk_iota_client.models.callback_input import CallbackInput
from affinidi_tdk_iota_client.models.consent_dto import ConsentDto
from affinidi_tdk_iota_client.models.cors_aws_exchange_credentials_ok import CorsAwsExchangeCredentialsOK
from affinidi_tdk_iota_client.models.cors_aws_exchange_credentials_project_token_ok import CorsAwsExchangeCredentialsProjectTokenOK
from affinidi_tdk_iota_client.models.cors_iot_oidc4vpcallback_ok import CorsIotOidc4vpcallbackOK
from affinidi_tdk_iota_client.models.create_iota_configuration_input import CreateIotaConfigurationInput
from affinidi_tdk_iota_client.models.create_pex_query_input import CreatePexQueryInput
from affinidi_tdk_iota_client.models.delete_pex_queries_input import DeletePexQueriesInput
from affinidi_tdk_iota_client.models.get_iota_configuration_meta_data_ok import GetIotaConfigurationMetaDataOK
from affinidi_tdk_iota_client.models.invalid_parameter_error import InvalidParameterError
from affinidi_tdk_iota_client.models.invalid_parameter_error_details_inner import InvalidParameterErrorDetailsInner
from affinidi_tdk_iota_client.models.iota_configuration_dto import IotaConfigurationDto
from affinidi_tdk_iota_client.models.iota_configuration_dto_client_metadata import IotaConfigurationDtoClientMetadata
from affinidi_tdk_iota_client.models.list_configuration_ok import ListConfigurationOK
from affinidi_tdk_iota_client.models.list_logged_consents_ok import ListLoggedConsentsOK
from affinidi_tdk_iota_client.models.list_pex_queries_ok import ListPexQueriesOK
from affinidi_tdk_iota_client.models.message_publishing_error import MessagePublishingError
from affinidi_tdk_iota_client.models.not_found_error import NotFoundError
from affinidi_tdk_iota_client.models.operation_forbidden_error import OperationForbiddenError
from affinidi_tdk_iota_client.models.pex_query_dto import PexQueryDto
from affinidi_tdk_iota_client.models.prepare_request import PrepareRequest
from affinidi_tdk_iota_client.models.prepare_request_created import PrepareRequestCreated
from affinidi_tdk_iota_client.models.prepare_request_created_data import PrepareRequestCreatedData
from affinidi_tdk_iota_client.models.resource_limit_exceeded_error import ResourceLimitExceededError
from affinidi_tdk_iota_client.models.save_pex_queries_update_input import SavePexQueriesUpdateInput
from affinidi_tdk_iota_client.models.save_pex_queries_update_input_queries_inner import SavePexQueriesUpdateInputQueriesInner
from affinidi_tdk_iota_client.models.update_configuration_by_id_input import UpdateConfigurationByIdInput
from affinidi_tdk_iota_client.models.update_configuration_by_id_ok import UpdateConfigurationByIdOK
from affinidi_tdk_iota_client.models.update_pex_query_input import UpdatePexQueryInput
from affinidi_tdk_iota_client.models.vp_token_validation_error import VPTokenValidationError
