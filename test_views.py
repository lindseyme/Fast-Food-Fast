"""
A script that carries tests on the views.py file.
"""
import pytest
from fetch_a_specific_order_api.views import Order
from runserver import APP
MYAPP = APP
CLIENT = MYAPP.test_client
NEWORDER = Order()

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
