"""
In this script, we implement three restApi methods which are: GET,POST and PULL
"""
from flask import jsonify, request
from flask.views import MethodView
from api.order_class import MakeOrder


class Order(MethodView):
    """
    Class order defines the restApi methods.
    """
    # order_1 = MakeOrder(1, "Ayesiga", [{"item_id": 1, "item_name":"Burger", "quantity":2,
    #                                     "price":30000}], None)
    orders = []

    def get(self, order_id):
        """
         Method that retrieves a list of orders and a specific order.
        """
        if order_id is None:
            # return a list of users
            if not self.orders:
                return jsonify({"Message":"There are no orders yet. Please make your first order."})
            return jsonify({"List of all orders": [order.__dict__ for order in self.orders]})
        if isinstance(order_id, int):
            if not isinstance(order_id, bool):
                if order_id > 0:
                #expose a single order
                    single_order = [order.__dict__ for order in self.orders
                                    if order.__dict__['order_id'] == order_id]
                    if single_order:
                        return jsonify({'Specific order': single_order[0]})
                    return jsonify({"Error Message":"The order with that id doesn't exist."})
                raise ValueError('Please provide a non negative integer argument')
            raise TypeError('Please provide a non negative integer argument')
        raise TypeError('Please provide a non negative integer argument')

    def post(self):
        """
        Method for creating the new order
        """
        if 'order_list' in request.json and 'username' in request.json:
            if isinstance(request.json['username'], str):
                for order in self.orders:
                    if order.__dict__["username"] == request.json['username'] and order.__dict__['order_status'] is  None:
                        list_index = 0
                        for item in order.__dict__["order_list"]:
                            if  item["item_id"] == request.json['order_list'][list_index]["item_id"]:
                                item["quantity"] += request.json['order_list'][list_index]["quantity"]
                                item["price"] += request.json['order_list'][list_index]["price"]
                                return jsonify({'new_order':order.__dict__}), 201
                            list_index += 1
                new_order = MakeOrder(len(self.orders) + 1,
                                        request.json['username'], request.json['order_list'], None)
                self.orders.append(new_order)
                return jsonify({'new_order': new_order.__dict__}), 201
            return jsonify({"error message":"order_list should be a str"})
        return jsonify({"error message":"Define order_list and username keys in json structure"})

    def put(self, order_id):
        """
        Method for updating the data structure
        """
        if isinstance(order_id, int):
            if not isinstance(order_id, bool):
                if order_id > 0:
                    if 'order_status' in request.json and isinstance(request.json
                                                                    ['order_status'], str):
                        for order in self.orders:
                            if order.__dict__['order_id'] == order_id:
                                order_json = request.get_json()
                                order.__dict__['order_status'] = order_json['order_status']
                                return jsonify({'updated order':
                                                [order.__dict__ for order in self.orders]})
                        return jsonify({"Error Message":"The order with that id doesn't exist."})
                    return jsonify({"error message":"A string order_status should be defined"})
                raise ValueError("Please provide a non negative integer argument")   
            raise TypeError("Please provide a non negative integer argument")
        raise TypeError("Please provide a non negative integer argument")
