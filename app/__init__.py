import os
from flask import Flask, jsonify
import psycopg2
from flask_bcrypt import Bcrypt


# Initialize application
app = Flask(__name__)

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
conn = psycopg2.connect(database = "testdb", user="postgres", password = "Ayesiga96", host ="localhost", port= 5432)

# Import the application views
from app.views.user_views import GetAuthUrls
from app.views.menu_views import GetMenuUrls
from app.views.order_views import GetOrderUrls
GetAuthUrls.fetch_urls(app)
GetMenuUrls.fetch_urls(app)
GetOrderUrls.fetch_urls(app)