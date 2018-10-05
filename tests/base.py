from app import app, conn
from flask_testing import TestCase
import json
import string
import random

def item_name_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class BaseTestCase(TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        :return:
        """
        app.config.from_object('app.config.TestingConfig')
        return app

    def setUp(self):
        """
        Create a cursor for your database
        :return:
        """
        cur = conn.cursor()

    def tearDown(self):
        """
        Close connection after running database executions
        :return:
        """
        conn.commit()

    def register_user(self, email, password):
        """
        Helper method for registering a user with dummy data
        :return:
        """
        return self.client.post(
            'auth/signup',
            content_type='application/json',
            data=json.dumps(dict(email=email, password=password)))

    def login_user(self, email, password):
        """
        Helper method for registering a user with dummy data
        :return:
        """
        response = self.register_user('admin@admin.com', '12345')
        return self.client.post(
            'auth/login',
            content_type='application/json',
            data=json.dumps(dict(email=email, password=password)))


    def create_menu(self):
        """
        Helper function to create a menu
        :return:
        """
        token = self.get_user_token()
        response = self.client.post(
            '/menu',
            data=json.dumps({"item_name":"Pizza","price":25000}),
            headers={"x-access-token": token},
            content_type='application/json'
        )
        return response
        

    def create_order(self):
        """
        Helper function to create a menu
        :return:
        """
        token = self.get_user_token()
        results = self.client.post('users/orders',data=json.dumps({"item_name":"Pizza","quantity":2}),headers={"x-access-token": token},content_type='application/json')
        return results
    
    def get_user_token(self):
        """
        Get a user token
        :return:
        """
        auth_res = self.login_user('admin@admin.com', '12345')
        return json.loads(auth_res.data.decode())['auth_token']