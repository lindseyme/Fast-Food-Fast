"""
A script that carries tests on the views.py file.
"""
import pytest
from flask import json
from update_the_order_status_api.views import Order
from runserver import APP
MYAPP = APP
CLIENT = MYAPP.test_client
NEWORDER = Order()

####################### Tests for updating order status #################################
def test_update_specific_order():
    """
    Method to update an order.
    """
    result = CLIENT().put('/api/v1/orders/2', content_type='application/json',
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
        