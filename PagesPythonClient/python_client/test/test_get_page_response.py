# coding: utf-8

"""
    Pages

    The control plane for Pages

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pages_client.models.get_page_response import GetPageResponse

class TestGetPageResponse(unittest.TestCase):
    """GetPageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPageResponse:
        """Test GetPageResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPageResponse`
        """
        model = GetPageResponse()
        if include_optional:
            return GetPageResponse(
                page = pages_client.models.page.Page(
                    user = '', 
                    namespace = '', 
                    name = '', 
                    content = '', )
            )
        else:
            return GetPageResponse(
                page = pages_client.models.page.Page(
                    user = '', 
                    namespace = '', 
                    name = '', 
                    content = '', ),
        )
        """

    def testGetPageResponse(self):
        """Test GetPageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
