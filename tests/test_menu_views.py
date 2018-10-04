from tests.base import BaseTestCase
from app.models.menu_model import OrderMenu
from app import conn
import unittest
import json

class TestMenuBluePrint(BaseTestCase):
    def test_get_menu_without_jwt(self):
            """
            Helper function to create a menu
            :return:
            """
            response = self.client.get('/menu')
            self.assertEqual(response.status_code, 401)

    def test_get_menu(self):
            """
            Helper function to create a menu
            :return:
            """
            token = self.get_user_token()
            response = self.client.get('/menu',headers={"x-access-token": token},content_type='application/json')
            data = json.loads(response.data.decode('utf-8'))
            #self.assertEqual(data['status'], 'success')
            self.assertEqual(response.status_code, 200)

    

