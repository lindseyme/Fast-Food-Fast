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
    def get(current_user,self, order_id):
        """
        Return all orders if order id is None or return an order with the supplied order Id.
        :param current_user: User
        :param order_id: 
        :return:
        """
        if current_user == "admin@admin.com":
            if order_id is None:
                cur = conn.cursor()
                sql = """
                    SELECT * FROM orders 
                """
                cur.execute(sql)
                rows = cur.fetchall()
                all_orders = []
                if rows:
                    for row in rows:
                        order = {
                            'order_id': row[0],
                            'user_id': row[1],
                            'item_id':row[2],
                            'item_name':row[3],
                            'quantity':row[4],
                            'price':row[5],
                            'order_status':row[6],
                            'created_at':row[7]
                        }
                        all_orders.append(order)

                    return response_for_user_orders('success', all_orders, 200)
                return response('success', "There are no orders yet", 200)
            

            try:
                int(order_id)
            except ValueError:
                return response('failed', 'Please provide a valid Order Id', 400)
            else:
                # user_bucket = User.get_by_id(current_user.id).buckets.filter_by(id=bucket_id).first()
                cur = conn.cursor()
                sql = """
                    SELECT * FROM orders WHERE order_id=%s
                """
                cur.execute(sql,(order_id,))
                row = cur.fetchone()
                if row:
                    user_order = order = {
                            'order_id': row[0],
                            'user_id': row[1],
                            'item_id':row[2],
                            'item_name':row[3],
                            'quantity':row[4],
                            'price':row[5],
                            'order_status':row[6],
                            'created_at':row[7]
                        }

                    return response_for_user_order('success', user_order, 200)
                return response('failed', "Order not found", 404) 
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
        