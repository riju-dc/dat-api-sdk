# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_api_sdk.models.connector_specification import ConnectorSpecification

class TestConnectorSpecification(unittest.TestCase):
    """ConnectorSpecification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectorSpecification:
        """Test ConnectorSpecification
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectorSpecification`
        """
        model = ConnectorSpecification()
        if include_optional:
            return ConnectorSpecification(
                protocol_version = None,
                documentation_url = None,
                changelog_url = None,
                name = None,
                connection_specification = None,
                supports_incremental = None,
                supported_destination_sync_modes = None
            )
        else:
            return ConnectorSpecification(
                name = None,
                connection_specification = None,
        )
        """

    def testConnectorSpecification(self):
        """Test ConnectorSpecification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
