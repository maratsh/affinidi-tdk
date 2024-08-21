# coding: utf-8

"""
    CloudWalletEssentials

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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator
from affinidi_tdk_wallets_client.models.sign_credential_input_dto_unsigned_credential_params import SignCredentialInputDtoUnsignedCredentialParams

class SignCredentialInputDto(BaseModel):
    """
    DTO contains params to sign credential  # noqa: E501
    """
    unsigned_credential: Optional[Dict[str, Any]] = Field(default=None, alias="unsignedCredential", description="Unsigned Credential. If provided \"unsignedCredentialParams\" is not accepted")
    revocable: Optional[StrictBool] = None
    credential_format: Optional[StrictStr] = Field(default=None, alias="credentialFormat")
    unsigned_credential_params: Optional[SignCredentialInputDtoUnsignedCredentialParams] = Field(default=None, alias="unsignedCredentialParams")
    __properties = ["unsignedCredential", "revocable", "credentialFormat", "unsignedCredentialParams"]

    @validator('credential_format')
    def credential_format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ldp_vc', 'jwt_vc_json-ld'):
            raise ValueError("must be one of enum values ('ldp_vc', 'jwt_vc_json-ld')")
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
    def from_json(cls, json_str: str) -> SignCredentialInputDto:
        """Create an instance of SignCredentialInputDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of unsigned_credential_params
        if self.unsigned_credential_params:
            _dict['unsignedCredentialParams'] = self.unsigned_credential_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SignCredentialInputDto:
        """Create an instance of SignCredentialInputDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SignCredentialInputDto.parse_obj(obj)

        _obj = SignCredentialInputDto.parse_obj({
            "unsigned_credential": obj.get("unsignedCredential"),
            "revocable": obj.get("revocable"),
            "credential_format": obj.get("credentialFormat"),
            "unsigned_credential_params": SignCredentialInputDtoUnsignedCredentialParams.from_dict(obj.get("unsignedCredentialParams")) if obj.get("unsignedCredentialParams") is not None else None
        })
        return _obj


