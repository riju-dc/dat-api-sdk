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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dat_client.models.connector_specification import ConnectorSpecification
from typing import Optional, Set
from typing_extensions import Self

class ActorInstanceOutput(BaseModel):
    """
    ActorInstanceOutput
    """ # noqa: E501
    uuid: Optional[StrictStr] = 'd565b077-029b-4cab-acdd-f2a5c2298cd3'
    name: StrictStr
    workspace_id: Optional[StrictStr] = 'wkspc-uuid'
    actor_id: Optional[StrictStr] = 'gdrive-uuid'
    user_id: Optional[StrictStr] = '09922bd9-7872-4664-99d0-08eae42fb554'
    configuration: ConnectorSpecification
    __properties: ClassVar[List[str]] = ["uuid", "name", "workspace_id", "actor_id", "user_id", "configuration"]

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
        """Create an instance of ActorInstanceOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActorInstanceOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid") if obj.get("uuid") is not None else 'd565b077-029b-4cab-acdd-f2a5c2298cd3',
            "name": obj.get("name"),
            "workspace_id": obj.get("workspace_id") if obj.get("workspace_id") is not None else 'wkspc-uuid',
            "actor_id": obj.get("actor_id") if obj.get("actor_id") is not None else 'gdrive-uuid',
            "user_id": obj.get("user_id") if obj.get("user_id") is not None else '09922bd9-7872-4664-99d0-08eae42fb554',
            "configuration": ConnectorSpecification.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None
        })
        return _obj


