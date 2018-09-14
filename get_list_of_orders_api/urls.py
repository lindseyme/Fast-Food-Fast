"""
This script contains the different urls.
"""
from get_list_of_orders_api.views import Order

class Urls():
    """
     This class fetches urls.
    """
    @staticmethod
    def fetch_urls(app):
        """
         Method that fetches
        """
        order_view = Order.as_view('order_api')
        app.add_url_rule('/api/v1/orders/',
                         view_func=order_view, methods=['GET',])
