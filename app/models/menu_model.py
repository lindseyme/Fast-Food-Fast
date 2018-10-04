from app import conn

cur = conn.cursor()

class OrderMenu:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS menu (
                item_id SERIAL PRIMARY KEY,
                item_name VARCHAR(255) NOT NULL,
                price BIGINT NOT NULL
        )
        """)
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price

    def save(self):
        cur = conn.cursor()
        sql = """
            INSERT INTO menu (item_name,price) 
                    VALUES (%s,%s)
        """
        cur.execute(sql,(self.item_name,self.price,))
        conn.commit()

    @staticmethod
    def check_item(item_name):
        cur = conn.cursor()
        sql1 = """
             SELECT * FROM menu WHERE item_name=%s
        """
        cur.execute(sql1,(item_name,))
        item = cur.fetchone()
        if item:
            item_price = item[2]
            return item_price
        return item
    
    @staticmethod
    def get_item_id(item_name):
        cur = conn.cursor()
        sql1 = """
             SELECT item_id FROM menu WHERE item_name=%s
        """
        cur.execute(sql1,(item_name,))
        item = cur.fetchone()
        return item[0]
