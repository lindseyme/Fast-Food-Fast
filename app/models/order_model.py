from app import conn

cur = conn.cursor()

class MakeOrder():
     
    cur.execute("""CREATE TABLE IF NOT EXISTS orders (
                order_id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                item_id INTEGER NOT NULL,
                item_name VARCHAR(100) NOT NULL,
                price BIGINT NOT NULL,
                quantity INTEGER NOT NULL,
                order_status VARCHAR(100)  DEFAULT 'New',
                created_at TIMESTAMP DEFAULT NOW(),
                FOREIGN KEY (user_id)
                    REFERENCES users (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (item_id)
                    REFERENCES menu (item_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """)
    def __init__(self, user_id, item_id, item_name, quantity, price):
        self.user_id = user_id
        self.item_id = item_id
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def save(self):
        cur = conn.cursor()
        sql = """
            INSERT INTO orders (user_id,item_id,item_name,quantity,price) 
                    VALUES (%s,%s,%s,%s,%s)
        """
        cur.execute(sql,(self.user_id,self.item_id,self.item_name,self.quantity,self.price,))
        conn.commit()
        
    @staticmethod
    def update(order_status,order_id):
        cur = conn.cursor()
        sql = """
            UPDATE orders set order_status = %s WHERE order_id = %s
            """
        cur.execute(sql,(order_status,order_id,))
        conn.commit()
    @staticmethod
    def get_by_name(user_id,item_name):
        """
        Filter a order by name.
        :param item_name:
        :return: User or None
        """
        cur = conn.cursor()
        sql1 = """
             SELECT * FROM orders WHERE user_id=%s AND item_name=%s AND order_status=%s
        """
        cur.execute(sql1,(user_id,item_name,"New",))
        order = cur.fetchone()
        return order


