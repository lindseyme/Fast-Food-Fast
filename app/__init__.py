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
conn = psycopg2.connect(database = "testdb", user="postgres", password = "admin", host ="localhost", port= 5555)

# Import the application views
from app.views.menu_views import GetMenuUrls
GetMenuUrls.fetch_urls(app)
