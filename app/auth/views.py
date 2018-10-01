from app import app, bcrypt, conn
from flask import Blueprint, request, jsonify, make_response
from flask.views import MethodView
from app.models import User
from app.auth.helper import response, response_auth,token_required
import jwt
import datetime
# from app.auth.helper import token_required
import re

cur = conn.cursor()



class RegisterUser(MethodView):
    """
    View function to register a user via the api
    """

    def post(self):
        """
        Register a user, generate their token and add them to the database
        :return: Json Response with the user`s token
        """
        if request.content_type == 'application/json':
            post_data = request.get_json()
            email = post_data.get('email')
            password = post_data.get('password')
            
            if re.match(r"[^@]+@[^@]+\.[^@]+", email) and len(password) > 4:
                user = User.get_by_email(email)
                if not user:
                    User(email=email, password=password).save()
                    return response('success', 'Successfully registered', 201)
                else:
                    return response('failed', 'Failed, User already exists, Please sign In', 400)
            return response('failed', 'Missing or wrong email format or password is less than four characters', 400)
        return response('failed', 'Content-type must be json', 400)


class LoginUser(MethodView):
    def post(self):
        """
        Login a user if the supplied credentials are correct.
        :return: Http Json response
        """
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return response('failed', {"WWW-Authenticate":"Basic realm='Login Required'"}, 401)
        
        if re.match(r"[^@]+@[^@]+\.[^@]+", auth.username) and len(auth.password) > 4:
            sql1 = """
                SELECT * FROM Users WHERE email=%s
            """
            cur.execute(sql1,(auth.username,))
            user = cur.fetchone()
            if user and bcrypt.check_password_hash(user[2], auth.password):
                token = jwt.encode({'user_id': user[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)},app.config['SECRET_KEY'])
                return response_auth('success', 'Successfully logged In', token, 200)
            return response('failed', 'User does not exist or password is incorrect', 401)
        return response('failed', 'Missing or wrong email format or password is less than four characters', 401)
        # return response('failed', 'Content-type must be json', 202)


class LogOutUser(MethodView):
    """
    Class to log out a user
    """
    @token_required
    def post(self, current_user):
        """
        Try to logout a user using a token
        :return:
        """
        return 
        

class GetUrls:
    @staticmethod
    def fetch_urls(app):
        # Register classes as views
        registration_view = RegisterUser.as_view('register')
        login_view = LoginUser.as_view('login')
        logout_view = LogOutUser.as_view('logout')

        # Add rules for the api Endpoints
        app.add_url_rule('/auth/register', view_func=registration_view, methods=['POST'])
        app.add_url_rule('/auth/login', view_func=login_view, methods=['POST'])
        app.add_url_rule('/auth/logout', view_func=logout_view, methods=['POST'])
