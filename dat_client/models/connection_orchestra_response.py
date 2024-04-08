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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from dat_client.models.configuration import Configuration
from dat_client.models.connection_orchestra_response_catalog import ConnectionOrchestraResponseCatalog
from dat_client.models.connection_orchestra_response_schedule import ConnectionOrchestraResponseSchedule
from dat_client.models.connector_specification import ConnectorSpecification
from dat_client.models.prefix import Prefix
from dat_client.models.schedule_type import ScheduleType
from dat_client.models.status import Status
from typing import Optional, Set
from typing_extensions import Self

class ConnectionOrchestraResponse(BaseModel):
    """
    ConnectionOrchestraResponse
    """ # noqa: E501
    name: Optional[Any]
    namespace_format: Optional[Any] = None
    prefix: Optional[Prefix] = None
    catalog: Optional[ConnectionOrchestraResponseCatalog] = None
    source: ConnectorSpecification = Field(description="The source connector specification.")
    generator: ConnectorSpecification = Field(description="The generator connector specification.")
    destination: ConnectorSpecification = Field(description="The destination connector specification.")
    source_instance_id: Optional[Any]
    generator_instance_id: Optional[Any]
    destination_instance_id: Optional[Any]
    workspace_id: Optional[Any]
    configuration: Optional[Configuration] = None
    schedule: Optional[ConnectionOrchestraResponseSchedule] = None
    schedule_type: Optional[ScheduleType] = None
    status: Optional[Status] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["name", "namespace_format", "prefix", "catalog", "source", "generator", "destination", "source_instance_id", "generator_instance_id", "destination_instance_id", "workspace_id", "configuration", "schedule", "schedule_type", "status"]

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
        """Create an instance of ConnectionOrchestraResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of prefix
        if self.prefix:
            _dict['prefix'] = self.prefix.to_dict()
        # override the default output from pydantic by calling `to_dict()` of catalog
        if self.catalog:
            _dict['catalog'] = self.catalog.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generator
        if self.generator:
            _dict['generator'] = self.generator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule_type
        if self.schedule_type:
            _dict['schedule_type'] = self.schedule_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if namespace_format (nullable) is None
        # and model_fields_set contains the field
        if self.namespace_format is None and "namespace_format" in self.model_fields_set:
            _dict['namespace_format'] = None

        # set to None if source_instance_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_instance_id is None and "source_instance_id" in self.model_fields_set:
            _dict['source_instance_id'] = None

        # set to None if generator_instance_id (nullable) is None
        # and model_fields_set contains the field
        if self.generator_instance_id is None and "generator_instance_id" in self.model_fields_set:
            _dict['generator_instance_id'] = None

        # set to None if destination_instance_id (nullable) is None
        # and model_fields_set contains the field
        if self.destination_instance_id is None and "destination_instance_id" in self.model_fields_set:
            _dict['destination_instance_id'] = None

        # set to None if workspace_id (nullable) is None
        # and model_fields_set contains the field
        if self.workspace_id is None and "workspace_id" in self.model_fields_set:
            _dict['workspace_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectionOrchestraResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "namespace_format": obj.get("namespace_format"),
            "prefix": Prefix.from_dict(obj["prefix"]) if obj.get("prefix") is not None else None,
            "catalog": ConnectionOrchestraResponseCatalog.from_dict(obj["catalog"]) if obj.get("catalog") is not None else None,
            "source": ConnectorSpecification.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "generator": ConnectorSpecification.from_dict(obj["generator"]) if obj.get("generator") is not None else None,
            "destination": ConnectorSpecification.from_dict(obj["destination"]) if obj.get("destination") is not None else None,
            "source_instance_id": obj.get("source_instance_id"),
            "generator_instance_id": obj.get("generator_instance_id"),
            "destination_instance_id": obj.get("destination_instance_id"),
            "workspace_id": obj.get("workspace_id"),
            "configuration": Configuration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "schedule": ConnectionOrchestraResponseSchedule.from_dict(obj["schedule"]) if obj.get("schedule") is not None else None,
            "schedule_type": ScheduleType.from_dict(obj["schedule_type"]) if obj.get("schedule_type") is not None else None,
            "status": Status.from_dict(obj["status"]) if obj.get("status") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


