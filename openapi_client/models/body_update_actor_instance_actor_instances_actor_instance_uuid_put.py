# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from openapi_client.models.configured_document_stream import ConfiguredDocumentStream
from openapi_client.models.connector_specification import ConnectorSpecification
from typing import Optional, Set
from typing_extensions import Self

class BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut(BaseModel):
    """
    BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut
    """ # noqa: E501
    conn_spec: ConnectorSpecification
    configured_document_stream: ConfiguredDocumentStream
    __properties: ClassVar[List[str]] = ["conn_spec", "configured_document_stream"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of conn_spec
        if self.conn_spec:
            _dict['conn_spec'] = self.conn_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configured_document_stream
        if self.configured_document_stream:
            _dict['configured_document_stream'] = self.configured_document_stream.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BodyUpdateActorInstanceActorInstancesActorInstanceUuidPut from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conn_spec": ConnectorSpecification.from_dict(obj["conn_spec"]) if obj.get("conn_spec") is not None else None,
            "configured_document_stream": ConfiguredDocumentStream.from_dict(obj["configured_document_stream"]) if obj.get("configured_document_stream") is not None else None
        })
        return _obj

