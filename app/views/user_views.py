import re
from flask import request, jsonify, make_response
from flask.views import MethodView
from app import bcrypt, conn
from app.models.user_model import User, BlackListToken
from app.views.helper import response, response_auth,token_required

# from app.auth.helper import token_required


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




class GetAuthUrls:
    @staticmethod
    def fetch_urls(app):
        # Register classes as views
        registration_view = RegisterUser.as_view('register')


        # Add rules for the api Endpoints
        app.add_url_rule('/auth/signup', view_func=registration_view, methods=['POST'])
      
       
