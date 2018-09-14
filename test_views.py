"""
A script that carries tests on the views.py file.
"""
from flask import json
from place_a_new_order_for_food_api.views import Order
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
