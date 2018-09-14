"""
This script contains the different urls.
"""
from place_a_new_order_for_food_api.views import Order

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
        app.add_url_rule('/api/v1/orders', view_func=order_view, methods=['POST',])
