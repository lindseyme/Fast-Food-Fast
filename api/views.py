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
    order_1 = MakeOrder(1, "Ayesiga", [{"item_id": 1, "item_name":"Burger", "quantity":2,
                                        "price":30000}], None)
    order_2 = MakeOrder(2, "Patra", [{"item_id": 1, "item_name":"Pizza", "quantity":1,
                                      "price":10000}, {"item_id": 2, "item_name":"Sandwich",
                                                       "quantity":1, "price":10000}], None)
    order_3 = MakeOrder(3, "Lindsey", [{"item_id": 1, "item_name":"Chips", "quantity":3,
                                        "price":30000}, {"item_id": 2, "item_name":"Sandwich",
                                                         "quantity":3, "price":30000}], None)

    orders = [order_1, order_2, order_3]

    def get(self, order_id):
        """
         Method that retrieves a list of orders and a specific order.
        """
        if order_id is None:
            # return a list of users
            return jsonify({"List of all orders": [order.__dict__ for order in self.orders]})
        if isinstance(order_id, int):
            if not isinstance(order_id, bool):
                if order_id > 0:
                #expose a single order
                    single_order = [order.__dict__ for order in self.orders
                                    if order.__dict__['order_id'] == order_id]
                    if single_order:
                        return jsonify({'Specific order': single_order[0]})
                    raise ValueError("The order with that id doesn't exist.")
                raise ValueError('Please provide a non negative integer argument')
            raise TypeError('Please provide a non negative integer argument')
        raise TypeError('Please provide a non negative integer argument')

    def post(self):
        """
        Method for creating the new order
        """
        if 'order_list' in request.json and 'username' in request.json:
            if isinstance(request.json['username'], str):
                new_order = MakeOrder(len(self.orders) + 1,
                                      request.json['username'], request.json['order_list'], None)
                self.orders.append(new_order)
                return jsonify({'new_order': new_order.__dict__}), 200
            raise ValueError("order_list should be a str")
        raise ValueError("order_list and username keys should be defined in json structure")

    def put(self, order_id):
        """
        Method for updating the data structure
        """
        if isinstance(order_id, int):
            if not isinstance(order_id, bool):
                if order_id > 0:
                   # return 200
                    single_order = [order.__dict__ for order in self.orders
                                    if order.__dict__['order_id'] == order_id]
                    if single_order:
                        if 'order_status' in request.json and isinstance(request.json
                                                                         ['order_status'], str):
                            for order in self.orders:
                                if order.__dict__['order_id'] == order_id:
                                    order_json = request.get_json()
                                    order.__dict__['order_status'] = order_json['order_status']
                                    return jsonify({'updated order':
                                                    [order.__dict__ for order in self.orders]})
                        return "A string order_status should be defined"
                    raise ValueError("The order with that id doesn't exist.")
                raise ValueError("order_id should be greater than 0")
            raise TypeError("Please provide a non negative integer argument")
        raise TypeError("Please provide a non negative integer argument")
