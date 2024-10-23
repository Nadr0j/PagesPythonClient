# coding: utf-8

"""
    Pages

    The control plane for Pages

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pages_client.models.page import Page

class TestPage(unittest.TestCase):
    """Page unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Page:
        """Test Page
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Page`
        """
        model = Page()
        if include_optional:
            return Page(
                user = '',
                namespace = '',
                name = '',
                content = ''
            )
        else:
            return Page(
                user = '',
                namespace = '',
                name = '',
                content = '',
        )
        """

    def testPage(self):
        """Test Page"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
