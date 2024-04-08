# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dat_client.models.connection_post_request import ConnectionPostRequest

class TestConnectionPostRequest(unittest.TestCase):
    """ConnectionPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectionPostRequest:
        """Test ConnectionPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectionPostRequest`
        """
        model = ConnectionPostRequest()
        if include_optional:
            return ConnectionPostRequest(
                source_instance_id = '',
                generator_instance_id = '',
                destination_instance_id = '',
                workspace_id = '',
                name = '',
                namespace_format = '${SOURCE_NAMESPACE}',
                prefix = '',
                configuration = None,
                catalog = dat_client.models.dat_catalog.DatCatalog(
                    document_streams = [
                        dat_client.models.dat_document_stream.DatDocumentStream(
                            name = '', 
                            namespace = '', 
                            json_schema = dat_client.models.json_schema.json_schema(), 
                            read_sync_mode = 'FULL_REFRESH', 
                            write_sync_mode = 'APPEND', 
                            cursor_field = '', )
                        ], ),
                schedule = dat_client.models.schedule.Schedule(
                    cron = dat_client.models.cron.Cron(
                        cron_expression = '', 
                        timezone = '', ), ),
                schedule_type = '',
                status = ''
            )
        else:
            return ConnectionPostRequest(
                source_instance_id = '',
                generator_instance_id = '',
                destination_instance_id = '',
                workspace_id = '',
                name = '',
        )
        """

    def testConnectionPostRequest(self):
        """Test ConnectionPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
