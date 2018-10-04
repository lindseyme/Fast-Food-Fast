from tests.base import BaseTestCase
import unittest
import json


class TestMainAppCase(BaseTestCase):
    def test_page_not_found(self):
        """
        Test that a given route does not exist in the application
        :return:
        """
        with self.client:
            response = self.client.get("/home", headers={'x-access-token': self.get_user_token()})
            self.assert404(response)
           

    def test_http_method_not_found(self):
        with self.client:
            response = self.client.delete(
                'orders/1',
                headers={'x-access-token': self.get_user_token()})
            self.assert405(response)
            

    