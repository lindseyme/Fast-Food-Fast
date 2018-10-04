from flask.views import MethodView
from flask import request,jsonify
from app.views.helper import response, response_for_user_order,response_for_user_orders,token_required
from app.models.order_model import MakeOrder
from app.models.menu_model import OrderMenu
from app import conn

cur = conn.cursor()

class Order(MethodView):
    """
    Class order defines the restApi methods.
    """             
    @token_required   
    def put(current_user, self, order_id):
        """
        Method for updating the order status
        """
        if current_user == "admin@admin.com":
            try:
                int(order_id)
            except ValueError:
                return response('failed', 'Please provide a valid Order Id', 400)
            else:
                if request.content_type == 'application/json':
                    post_data = request.get_json()
                    order_status =  post_data.get('order_status')
                    if order_status:
                        if isinstance(order_status,str):
                            if order_status in ["New","Processing","Cancelled","Complete"]:
                                MakeOrder.update(order_status,order_id)
                                return response('success', 'Order Status successfully updated',200)
                            return response('failed', 'The Status of an order could either be New , Processing ,Cancelled or Complete .', 400)          
                        return response('failed', 'Order status should be a string', 400)
                    return response('failed', 'Order status cannot be empty', 400)
                return response('failed', 'Content-type must be json', 400)
        return response('failed', 'Sorry, this request requires administrative privileges to run', 401)




class GetOrderUrls:
    @staticmethod
    def fetch_urls(app):
        # Register classes as views
        order_view = Order.as_view('order_api')
        order_history = OrderHistory.as_view('order_history')
        app.add_url_rule('/orders/', defaults={'order_id': None},
                         view_func=order_view, methods=['GET',])
        app.add_url_rule('/users/orders', view_func=order_view, methods=['POST',])
        app.add_url_rule('/users/orders', view_func=order_history, methods=['GET',])
        app.add_url_rule('/orders/', view_func=order_view,defaults={'order_id': None}, methods=['GET',])
        app.add_url_rule('/orders/<order_id>', view_func=order_view, methods=['GET', 'PUT'])
        