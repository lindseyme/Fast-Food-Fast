"""
    Order class
"""
class MakeOrder():
    """
        Order constructor taking in 4 attributes i.e.  order_id,
         item_name, quantity, price
    """
    def __init__(self, order_id, username, order_list, order_status=None):
        self.order_id = order_id
        self.username = username
        self.order_list = order_list
        self.order_status = order_status
        