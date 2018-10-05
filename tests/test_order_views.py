from tests.base import BaseTestCase
from app.models.user_model import User
from app import conn
import unittest
import json


class TestOrdersBluePrint(BaseTestCase):
    def test_orders_creation(self):
        """
        Test an order is successfully created through the api
        :return:
        """
        with self.client:
            response = self.create_order()
            data = json.loads(response.data.decode('utf-8'))
            if data['status'] == 'success':
                self.assertTrue(data['status'] == 'success')
                self.assertTrue(data['message'] == 'Order made successfully')
                self.assertTrue(response.content_type == 'application/json')
                self.assertEqual(response.status_code, 201)
            elif data['message'] == 'Failed, Order already exists, Please wait as they work on it':
                self.assertTrue(data['status'] == 'failed')
                self.assertTrue(data['message'] == 'Failed, Order already exists, Please wait as they work on it')
                self.assertTrue(response.content_type == 'application/json')
                self.assertEqual(response.status_code, 400)
    
    def test_get_orders(self):
        """
        Helper function to create a menu
        :return:
        """
        token = self.get_user_token()
        response = self.client.get('orders/',headers={"x-access-token": token},content_type='application/json')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['status'], 'success')

    def test_get_specific_order(self):
        """
        Helper function to create a menu
        :return:
        """
        token = self.get_user_token()
        response = self.client.get('orders/1',headers={"x-access-token": token},content_type='application/json')
        data = json.loads(response.data.decode('utf-8'))
        if response.status_code == 404:
            self.assertEqual(data['status'], 'failed')
            self.assertEqual(data['message'], 'Order not found')
            self.assertEqual(response.status_code, 404)
        elif  response.status_code == 200:
            self.assertEqual(data['status'], 'success')
            self.assertEqual(response.status_code, 200)


    def test_get_order_history(self):
        """
        Helper function to create a menu
        :return:
        """
        token = self.get_user_token()
        response = self.client.get('/users/orders',headers={"x-access-token": token},content_type='application/json')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['status'], 'success')
        self.assertEqual(response.status_code, 200)
      
        
     
    
    def test_update_order_status(self):
        """
        Test function to update user order
        :return:
        """
        token = self.get_user_token()
        response = self.client.put('orders/1',headers={"x-access-token": token}, data=json.dumps({"order_status":"Complete"}), content_type='application/json')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['status'], 'success')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Order Status successfully updated')
        
        