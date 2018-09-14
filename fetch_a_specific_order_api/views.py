"""
In this script, we implement three restApi methods which are: GET,POST and PULL
"""
from flask import jsonify
from flask.views import MethodView
from fetch_a_specific_order_api.order_class import MakeOrder


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
         Method that retrieves a specific order.
        """
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
    