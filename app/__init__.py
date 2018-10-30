import os
from flask import Flask, jsonify
import psycopg2
from flask_bcrypt import Bcrypt
from flask_cors import CORS

# Initialize application
app = Flask(__name__,static_folder=None)

CORS(app)
# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)


# app.config['SECRET_KEY'] = "thisissecret"
# Initialize Bcrypt
bcrypt = Bcrypt(app)



# Initialize connections to  postgresql server
if os.getenv('db') == 'heroku':
    conn = psycopg2.connect(database = "d3jpf1e4bm92ff",user="jxboodptewpeaq",password="d5c8d9c2ab8aeff7fdb73701c1cacd3803d39f7c1320c21241824e85e3254091", host="ec2-174-129-32-37.compute-1.amazonaws.com",port=5432)
else:
    conn = psycopg2.connect(database = "testdb")

# Import the application views
from app.views.user_views import GetAuthUrls
from app.views.menu_views import GetMenuUrls
from app.views.order_views import GetOrderUrls
from app.docs.views import docs

app.register_blueprint(docs)
GetAuthUrls.fetch_urls(app)
GetMenuUrls.fetch_urls(app)
GetOrderUrls.fetch_urls(app)
