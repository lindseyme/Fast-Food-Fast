"""
In this script, we implement three restApi methods which are: GET,POST and PULL
"""
from flask import jsonify, request
from flask.views import MethodView
from place_a_new_order_for_food_api.order_class import MakeOrder


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
