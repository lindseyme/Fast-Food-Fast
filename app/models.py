from app import app, conn, bcrypt
from flask import jsonify
import datetime
import jwt

cur = conn.cursor()

class User:
    """
    Table schema
    """

    cur.execute('''CREATE TABLE IF NOT EXISTS Users
            ( id SERIAL PRIMARY KEY    NOT NULL,
            email             VARCHAR(255)     NOT NULL,
            password          VARCHAR(255)     NOT NULL,
            registered_on     DATE     NOT NULL );''')

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS')) \
            .decode('utf-8')
        self.registered_on = str(datetime.datetime.now())

    def save(self):
        """
        Persist the user in the database
        :param user:
        :return:
        """
        cur = conn.cursor()
        sql = """
            INSERT INTO Users (email,password,registered_on) 
                    VALUES (%s,%s,%s)
        """
        cur.execute(sql,(self.email,self.password,self.registered_on,))
        conn.commit()
        return jsonify({'message' : 'User created successfully!'})

    @staticmethod
    def get_by_email(user_email):
        """
        Filter a user by email.
        :param user_id:
        :return: User or None
        """
        cur = conn.cursor()
        sql1 = """
             SELECT * FROM Users WHERE email=%s
        """
        cur.execute(sql1,(user_email,))
        user = cur.fetchone()
        return user


    