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
    json_data = json.loads(result.data)
    #verify whether order was saved with the same attributes and values
    assert "new_order" in json_data
    assert json_data['new_order']['order_list'][0]['item_name'] == "Burger"
    assert json_data['new_order']['order_list'][0]['price'] == 30000
    assert json_data['new_order']['order_list'][0]['quantity'] == 2
    assert json_data['new_order']['username'] == "Patra"
    assert json_data['new_order']['order_status'] == None
    


####################### Tests for updating order status ########################################
def test_update_specific_order():
    """
    Method to update an order.
    """
    result = CLIENT().put('/api/v1/orders/1', content_type='application/json',
                          data=json.dumps({"order_status":"Accepted"}))
    assert result.status_code == 200
    #fetch the order  again to verify whether the order_status has changed to Accepted
    check_order = CLIENT().get('/api/v1/orders/1')
    assert check_order.status_code ==200
    json_data = json.loads(check_order.data)
    #order_status value should now be Accepted
    assert json_data['Specific order']['order_status'] == "Accepted"


########################## Tests for fetching all orders and a specific order###################################
@pytest.mark.parametrize("test_input, expected_output",
                        [
                            ('/api/v1/orders/',200),
                            ('/api/v1/orders/1',200),
                        ]
                        )
def test_get_all_orders_OR_specific_order(test_input, expected_output):
    """
    Method for fetching all the orders.
    """
    result = CLIENT().get(test_input)
    assert result.status_code == expected_output
    if test_input == '/api/v1/orders/':
        assert b"List of all orders" in result.data
    else:
        assert b"Specific order" in result.data
    
# check for the order_id's data type
@pytest.mark.parametrize("test_input, expected_output",
                        [
                            ('five','Please provide a non negative integer argument'),
                            (True,'Please provide a non negative integer argument'),
                            (2+3j,'Please provide a non negative integer argument')
                        ]
                        )
def test_if_parameter__is_of_wrong_type(test_input,expected_output):
    """
    Method to test if parameter is a string or boolean or complex number
    """
    with pytest.raises(TypeError):
        NEWORDER.get(test_input)




    