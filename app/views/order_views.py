from flask.views import MethodView
from flask import request,jsonify
from app.views.helper import response, response_for_user_order,response_for_user_orders,token_required
from app.models.order_model import MakeOrder
from app.models.menu_model import OrderMenu
from app import conn

cur = conn.cursor()


 
class OrderHistory(MethodView):
    @token_required
    def get(current_user,self):
        
        cur = conn.cursor()
        sql1 = """
            SELECT user_id FROM users WHERE email=%s 
        """
        cur.execute(sql1,(current_user,))
        user = cur.fetchone()
        user_id = user[0]

        sql2 = """
            SELECT * FROM orders WHERE user_id=%s 
        """
        cur.execute(sql2,(user_id,))
        orders = cur.fetchall()
        order_history = []
        if orders:
            for order in orders:
                order_details={
                   "order_id":order[0],
                   "item_name":order[3],
                   "quantity":order[5],
                   "price":order[4],
                   "order_status":order[6],
                   "created_at":order[7]
                }
                order_history.append(order_details)
                return response("success",order_history,200)
        return response('success', 'No order history', 200)



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
        