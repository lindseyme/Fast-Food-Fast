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
                
    @token_required
    def post(current_user,self):
        """
        Method for creating the new order
        """
        if request.content_type == 'application/json':
            # if 'item_name' in request.json and 'quantity' in request.json:
            post_data = request.get_json()
            item_name = post_data.get('item_name')
            quantity = int(post_data.get('quantity'))
            
            if isinstance(item_name,str) and isinstance(quantity,int):
                if item_name and quantity > 0:
                    get_price = OrderMenu.check_item(item_name)
                    if get_price:
                        price = quantity * get_price
                        cur = conn.cursor()
                        sql1 = """
                            SELECT user_id FROM users WHERE email=%s 
                        """
                        cur.execute(sql1,(current_user,))
                        user = cur.fetchone()
                        user_id = user[0]
                        order = MakeOrder.get_by_name(user_id,item_name)
                        if not order:
                            MakeOrder(user_id,OrderMenu.get_item_id(item_name),item_name,quantity,price).save()
                            return response('success', 'Order made successfully', 201)
                        return response('failed', 'Failed, Order already exists, Please wait as they work on it', 400)
                    return response('failed', 'Failed, Item name does not exist on the menu, Please check on the menu again', 400)
                                    
                return response('failed', 'Failed, Item name cannot be empty or quantity should be  1 and above.', 400)                
            return response('failed', 'Item name and quantity should be a string and a non negative integer respectively', 400)
            # return response('failed', 'item_name or price is missing', 400)
        return response('failed', 'Content-type must be json', 202)                   

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
                cur = conn.cursor()
                sql1 = """
                    SELECT order_id FROM orders WHERE order_id=%s 
                """
                cur.execute(sql1,(order_id,))
                order = cur.fetchone()
                if order:
                    if request.content_type == 'application/json':
                        post_data = request.get_json()
                        order_status =  post_data.get('order_status')
                        if order_status:
                            if isinstance(order_status,str):
                                if order_status in ["New","Processing","Cancelled","Complete"]:
                                    MakeOrder.update(order_status,order_id)
                                    return response('success', 'Order Status successfully updated',201)
                                return response('failed', 'The Status of an order could either be New , Processing ,Cancelled or Complete .', 400)          
                            return response('failed', 'Order status should be a string', 400)
                        return response('failed', 'Order status cannot be empty', 400)
                    return response('failed', 'Content-type must be json', 202)
                return response('failed', 'The order with that id doesnt exist', 404)
        return response('failed', 'Sorry, this request requires administrative privileges to run', 401)

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
        