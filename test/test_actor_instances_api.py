# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_api_sdk.api.actor_instances_api import ActorInstancesApi


class TestActorInstancesApi(unittest.TestCase):
    """ActorInstancesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ActorInstancesApi()

    def tearDown(self) -> None:
        pass

    def test_call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get(self) -> None:
        """Test case for call_actor_instance_discover_actor_instances_actor_instance_uuid_discover_get

        Call Actor Instance Discover
        """
        pass

    def test_create_actor_instance_actor_instances_post(self) -> None:
        """Test case for create_actor_instance_actor_instances_post

        Create Actor Instance
        """
        pass

    def test_delete_actor_instance_actor_instances_actor_instance_uuid_delete(self) -> None:
        """Test case for delete_actor_instance_actor_instances_actor_instance_uuid_delete

        Delete Actor Instance
        """
        pass

    def test_fetch_available_actor_instances_actor_instances_actor_type_list_get(self) -> None:
        """Test case for fetch_available_actor_instances_actor_instances_actor_type_list_get

        Fetch Available Actor Instances
        """
        pass

    def test_read_actor_instance_actor_instances_actor_instance_uuid_get(self) -> None:
        """Test case for read_actor_instance_actor_instances_actor_instance_uuid_get

        Read Actor Instance
        """
        pass

    def test_update_actor_instance_actor_instances_actor_instance_uuid_put(self) -> None:
        """Test case for update_actor_instance_actor_instances_actor_instance_uuid_put

        Update Actor Instance
        """
        pass


if __name__ == '__main__':
    unittest.main()
