"""
A script that carries tests on the views.py file.
"""
import pytest
from flask import json
from api.views import Order
from runserver import APP
MYAPP = APP
CLIENT = MYAPP.test_client
NEWORDER = Order()

########################## Tests for fetching all orders ###################################
def test_get_all_orders():
    """
    Method for fetching all the orders.
    """
    result = CLIENT().get('/api/v1/orders/')
    assert result.status_code == 200

######################### Tests for fetching a single order  ###############################
def test_get_one_order():
    """
    Method that fetches a single order.
    """
    result = CLIENT().get('/api/v1/orders/1')
    assert result.status_code == 200

def test_if_parameter_passed_to_function_is_a_string():
    """
    Method to test if parameter is a string
    """
    with pytest.raises(TypeError):
        NEWORDER.get("five")

def test_if_parameter_passed_is_a_boolean():
    """
    Method to test if the parameter is boolean.
    """
    with pytest.raises(TypeError):
        NEWORDER.get(True)

####################### Tests for updating order status #################################
def test_update_specific_order():
    """
    Method to update an order.
    """
    result = CLIENT().put('/api/v1/orders/1', content_type='application/json',
                          data=json.dumps({"order_status":"Accepted"}))
    assert result.status_code == 200

def test_if_parameter_passed_to_the_put_function_is_a_string():
    """
    Method to check if the parameter passed is a string.
    """
    with pytest.raises(TypeError):
        NEWORDER.put("ten")

def test_if_parameter_passed_to_the_put_function_is_a_number_less_than_a_zero():
    """
    Method to check if the parameter passed is a negative number.
    """
    with pytest.raises(ValueError):
        NEWORDER.put(-1)
def test_if_parameter_passed_to_the_put_function_is_a_boolean():
    """
    Method to check if the parameter passed is boolean.
    """
    with pytest.raises(TypeError):
        NEWORDER.put(True)

############################# Tests for addng a new order ######################################
def test_if_data_posted_is_in_form_of_json():
    """
    Method to check if the data is in json form.
    """
    result = CLIENT().post('/api/v1/orders', content_type='application/json',
                           data=json.dumps({"order_list":[{"item_id":1, "item_name":"Burger",
                                                           "price":30000, "quantity":2}],
                                            "username":"Patra"}))
    assert result.status_code == 200
               