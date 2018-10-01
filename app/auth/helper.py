from flask import request, make_response, jsonify
from app.models import User
from functools import wraps
from app import app, conn
import jwt

# app.config['SECRET_KEY'] = "thisissecret"

cur = conn.cursor()
def token_required(f):
    """
    Decorator function to ensure that a resource is access by only authenticated users`
    provided their auth tokens are valid
    :param f:
    :return:
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return make_response(jsonify({
                'status': 'failed',
                'message': 'Token is missing'
            })), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            
            sql1 = """
                SELECT email FROM Users WHERE id=%s
            """
            cur.execute(sql1,(data['user_id'],))
            current_user = cur.fetchone()
            
        
        except:
            message = 'Invalid token'
            return make_response(jsonify({
                'status': 'failed',
                'message': message
            })), 401

        return f(current_user, *args, **kwargs)

    return decorated_function


def response(status, message, status_code):
    """
    Helper method to make an Http response
    :param status: Status
    :param message: Message
    :param status_code: Http status code
    :return:
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code


def response_auth(status, message, token, status_code):
    """
    Make a Http response to send the auth token
    :param status: Status
    :param message: Message
    :param token: Authorization Token
    :param status_code: Http status code
    :return: Http Json response
    """
    return make_response(jsonify({
        'status': status,
        'message': message,
        'auth_token': token.decode("utf-8")
    })), status_code
