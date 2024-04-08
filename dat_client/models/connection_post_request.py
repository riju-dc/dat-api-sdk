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
from dat_client.models.dat_catalog_input import DatCatalogInput
from dat_client.models.schedule import Schedule
from typing import Optional, Set
from typing_extensions import Self

class ConnectionPostRequest(BaseModel):
    """
    ConnectionPostRequest
    """ # noqa: E501
    source_instance_id: StrictStr
    generator_instance_id: StrictStr
    destination_instance_id: StrictStr
    workspace_id: StrictStr
    name: StrictStr
    namespace_format: Optional[StrictStr] = '${SOURCE_NAMESPACE}'
    prefix: Optional[StrictStr] = None
    configuration: Optional[Dict[str, Any]] = None
    catalog: Optional[DatCatalogInput] = None
    schedule: Optional[Schedule] = None
    schedule_type: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["source_instance_id", "generator_instance_id", "destination_instance_id", "workspace_id", "name", "namespace_format", "prefix", "configuration", "catalog", "schedule", "schedule_type", "status"]

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
        """Create an instance of ConnectionPostRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of catalog
        if self.catalog:
            _dict['catalog'] = self.catalog.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # set to None if prefix (nullable) is None
        # and model_fields_set contains the field
        if self.prefix is None and "prefix" in self.model_fields_set:
            _dict['prefix'] = None

        # set to None if configuration (nullable) is None
        # and model_fields_set contains the field
        if self.configuration is None and "configuration" in self.model_fields_set:
            _dict['configuration'] = None

        # set to None if catalog (nullable) is None
        # and model_fields_set contains the field
        if self.catalog is None and "catalog" in self.model_fields_set:
            _dict['catalog'] = None

        # set to None if schedule (nullable) is None
        # and model_fields_set contains the field
        if self.schedule is None and "schedule" in self.model_fields_set:
            _dict['schedule'] = None

        # set to None if schedule_type (nullable) is None
        # and model_fields_set contains the field
        if self.schedule_type is None and "schedule_type" in self.model_fields_set:
            _dict['schedule_type'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectionPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "source_instance_id": obj.get("source_instance_id"),
            "generator_instance_id": obj.get("generator_instance_id"),
            "destination_instance_id": obj.get("destination_instance_id"),
            "workspace_id": obj.get("workspace_id"),
            "name": obj.get("name"),
            "namespace_format": obj.get("namespace_format") if obj.get("namespace_format") is not None else '${SOURCE_NAMESPACE}',
            "prefix": obj.get("prefix"),
            "configuration": obj.get("configuration"),
            "catalog": DatCatalogInput.from_dict(obj["catalog"]) if obj.get("catalog") is not None else None,
            "schedule": Schedule.from_dict(obj["schedule"]) if obj.get("schedule") is not None else None,
            "schedule_type": obj.get("schedule_type"),
            "status": obj.get("status")
        })
        return _obj


