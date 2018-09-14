"""
This script contains the different urls.
"""
from update_the_order_status_api.views import Order

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
        app.add_url_rule('/api/v1/orders/<int:order_id>', view_func=order_view,
                         methods=['PUT',])

