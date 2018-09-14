"""
A script that carries tests on the views.py file.
"""
from get_list_of_orders_api.views import Order
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
