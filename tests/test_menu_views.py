from tests.base import BaseTestCase
from app.models.user_model import User
from app import conn
import unittest
import json
import time
import string
import random

def item_name_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class TestAuthBluePrint(BaseTestCase):
    def test_create_menu(self):
        """
        Test a user is successfully created through the api
        :return:
        """
        with self.client:
            response = self.create_menu()
            data = json.loads(response.data.decode())
            if data['status'] == "success":
                self.assertEqual(response.status_code, 201)
                self.assertTrue(data['status'], 'success')
                self.assertTrue(data['message'], 'Successfully registered')
            else:
                token = self.get_user_token()
                response = self.client.post('/menu', data=json.dumps({"item_name":item_name_generator(),"price":25000}),
                                            headers={"x-access-token": token},
                                            content_type='application/json')
                data = json.loads(response.data.decode())
                self.assertEqual(response.status_code, 201)
                self.assertTrue(data['status'], 'success')
                self.assertTrue(data['message'], 'Successfully registered')
        