"""
This script contains the different routes for the api methods.
"""
from api.views import Order

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
        app.add_url_rule('/api/v1/orders/', defaults={'order_id': None},
                         view_func=order_view, methods=['GET',])
        app.add_url_rule('/api/v1/orders', view_func=order_view, methods=['POST',])
        app.add_url_rule('/api/v1/orders/<int:order_id>', view_func=order_view,
                         methods=['GET', 'PUT'])
