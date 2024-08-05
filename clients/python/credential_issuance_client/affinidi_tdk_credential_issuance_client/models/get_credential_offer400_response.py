# coding: utf-8

"""
    CredentialIssuanceService

    Affinidi Credential Issuance Service Structure

    The version of the OpenAPI document: 1.0.0
    Contact: info@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from affinidi_tdk_credential_issuance_client.models.credential_offer_claimed_error import CredentialOfferClaimedError
from affinidi_tdk_credential_issuance_client.models.credential_offer_expired_error import CredentialOfferExpiredError
from affinidi_tdk_credential_issuance_client.models.invalid_parameter_error import InvalidParameterError
from affinidi_tdk_credential_issuance_client.models.project_credential_config_not_exist_error import ProjectCredentialConfigNotExistError
from affinidi_tdk_credential_issuance_client.models.vc_claimed_error import VcClaimedError
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

GETCREDENTIALOFFER400RESPONSE_ONE_OF_SCHEMAS = ["CredentialOfferClaimedError", "CredentialOfferExpiredError", "InvalidParameterError", "ProjectCredentialConfigNotExistError", "VcClaimedError"]

class GetCredentialOffer400Response(BaseModel):
    """
    GetCredentialOffer400Response
    """
    # data type: InvalidParameterError
    oneof_schema_1_validator: Optional[InvalidParameterError] = None
    # data type: ProjectCredentialConfigNotExistError
    oneof_schema_2_validator: Optional[ProjectCredentialConfigNotExistError] = None
    # data type: CredentialOfferExpiredError
    oneof_schema_3_validator: Optional[CredentialOfferExpiredError] = None
    # data type: CredentialOfferClaimedError
    oneof_schema_4_validator: Optional[CredentialOfferClaimedError] = None
    # data type: VcClaimedError
    oneof_schema_5_validator: Optional[VcClaimedError] = None
    if TYPE_CHECKING:
        actual_instance: Union[CredentialOfferClaimedError, CredentialOfferExpiredError, InvalidParameterError, ProjectCredentialConfigNotExistError, VcClaimedError]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(GETCREDENTIALOFFER400RESPONSE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = GetCredentialOffer400Response.construct()
        error_messages = []
        match = 0
        # validate data type: InvalidParameterError
        if not isinstance(v, InvalidParameterError):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InvalidParameterError`")
        else:
            match += 1
        # validate data type: ProjectCredentialConfigNotExistError
        if not isinstance(v, ProjectCredentialConfigNotExistError):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ProjectCredentialConfigNotExistError`")
        else:
            match += 1
        # validate data type: CredentialOfferExpiredError
        if not isinstance(v, CredentialOfferExpiredError):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CredentialOfferExpiredError`")
        else:
            match += 1
        # validate data type: CredentialOfferClaimedError
        if not isinstance(v, CredentialOfferClaimedError):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CredentialOfferClaimedError`")
        else:
            match += 1
        # validate data type: VcClaimedError
        if not isinstance(v, VcClaimedError):
            error_messages.append(f"Error! Input type `{type(v)}` is not `VcClaimedError`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetCredentialOffer400Response with oneOf schemas: CredentialOfferClaimedError, CredentialOfferExpiredError, InvalidParameterError, ProjectCredentialConfigNotExistError, VcClaimedError. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetCredentialOffer400Response with oneOf schemas: CredentialOfferClaimedError, CredentialOfferExpiredError, InvalidParameterError, ProjectCredentialConfigNotExistError, VcClaimedError. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> GetCredentialOffer400Response:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> GetCredentialOffer400Response:
        """Returns the object represented by the json string"""
        instance = GetCredentialOffer400Response.construct()
        error_messages = []
        match = 0

        # deserialize data into InvalidParameterError
        try:
            instance.actual_instance = InvalidParameterError.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ProjectCredentialConfigNotExistError
        try:
            instance.actual_instance = ProjectCredentialConfigNotExistError.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CredentialOfferExpiredError
        try:
            instance.actual_instance = CredentialOfferExpiredError.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CredentialOfferClaimedError
        try:
            instance.actual_instance = CredentialOfferClaimedError.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into VcClaimedError
        try:
            instance.actual_instance = VcClaimedError.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetCredentialOffer400Response with oneOf schemas: CredentialOfferClaimedError, CredentialOfferExpiredError, InvalidParameterError, ProjectCredentialConfigNotExistError, VcClaimedError. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetCredentialOffer400Response with oneOf schemas: CredentialOfferClaimedError, CredentialOfferExpiredError, InvalidParameterError, ProjectCredentialConfigNotExistError, VcClaimedError. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


