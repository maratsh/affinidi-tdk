# coding: utf-8

"""
    CredentialIssuanceService

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



from pydantic import BaseModel, Field
from affinidi_tdk_credential_issuance_client.models.credential_offer_response_grants_urn_ietf_params_oauth_grant_type_pre_authorized_code import CredentialOfferResponseGrantsUrnIetfParamsOauthGrantTypePreAuthorizedCode

class CredentialOfferResponseGrants(BaseModel):
    """
    Object indicating to the Wallet the Grant Types the Credential Issuer's Authorization Server is prepared to process for this Credential Offer.  # noqa: E501
    """
    urnietfparamsoauthgrant_typepre_authorized_code: CredentialOfferResponseGrantsUrnIetfParamsOauthGrantTypePreAuthorizedCode = Field(default=..., alias="urn:ietf:params:oauth:grant-type:pre-authorized_code")
    __properties = ["urn:ietf:params:oauth:grant-type:pre-authorized_code"]

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
    def from_json(cls, json_str: str) -> CredentialOfferResponseGrants:
        """Create an instance of CredentialOfferResponseGrants from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of urnietfparamsoauthgrant_typepre_authorized_code
        if self.urnietfparamsoauthgrant_typepre_authorized_code:
            _dict['urn:ietf:params:oauth:grant-type:pre-authorized_code'] = self.urnietfparamsoauthgrant_typepre_authorized_code.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CredentialOfferResponseGrants:
        """Create an instance of CredentialOfferResponseGrants from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CredentialOfferResponseGrants.parse_obj(obj)

        _obj = CredentialOfferResponseGrants.parse_obj({
            "urnietfparamsoauthgrant_typepre_authorized_code": CredentialOfferResponseGrantsUrnIetfParamsOauthGrantTypePreAuthorizedCode.from_dict(obj.get("urn:ietf:params:oauth:grant-type:pre-authorized_code")) if obj.get("urn:ietf:params:oauth:grant-type:pre-authorized_code") is not None else None
        })
        return _obj


