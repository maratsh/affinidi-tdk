# coding: utf-8

"""
    Iam

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from affinidi_tdk_iam_client.models.token_private_key_authentication_method_dto_public_key_info import TokenPrivateKeyAuthenticationMethodDtoPublicKeyInfo

class UpdateTokenPrivateKeyAuthenticationMethodDto(BaseModel):
    """
    Private Key JWT Authentication of Client with `private_key_jwt` oAuth Method  # noqa: E501
    """
    type: Optional[StrictStr] = None
    signing_algorithm: Optional[StrictStr] = Field(default=None, alias="signingAlgorithm")
    public_key_info: Optional[TokenPrivateKeyAuthenticationMethodDtoPublicKeyInfo] = Field(default=None, alias="publicKeyInfo")
    __properties = ["type", "signingAlgorithm", "publicKeyInfo"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PRIVATE_KEY'):
            raise ValueError("must be one of enum values ('PRIVATE_KEY')")
        return value

    @validator('signing_algorithm')
    def signing_algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('RS256', 'RS512', 'ES256', 'ES512'):
            raise ValueError("must be one of enum values ('RS256', 'RS512', 'ES256', 'ES512')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdateTokenPrivateKeyAuthenticationMethodDto:
        """Create an instance of UpdateTokenPrivateKeyAuthenticationMethodDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of public_key_info
        if self.public_key_info:
            _dict['publicKeyInfo'] = self.public_key_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateTokenPrivateKeyAuthenticationMethodDto:
        """Create an instance of UpdateTokenPrivateKeyAuthenticationMethodDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateTokenPrivateKeyAuthenticationMethodDto.parse_obj(obj)

        _obj = UpdateTokenPrivateKeyAuthenticationMethodDto.parse_obj({
            "type": obj.get("type"),
            "signing_algorithm": obj.get("signingAlgorithm"),
            "public_key_info": TokenPrivateKeyAuthenticationMethodDtoPublicKeyInfo.from_dict(obj.get("publicKeyInfo")) if obj.get("publicKeyInfo") is not None else None
        })
        return _obj


