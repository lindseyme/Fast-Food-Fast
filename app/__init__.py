import os
from flask import Flask, jsonify
import psycopg2
from flask_bcrypt import Bcrypt


# Initialize application
app = Flask(__name__)

app.config['SECRET_KEY'] = "thisissecret"
# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Initialize connections to  postgresql server
conn = psycopg2.connect(database = "testdb", user="postgres", password = "Ayesiga", host ="127.0.0.1", port= 5432)

# Import the application views
from app.auth.views import GetUrls
GetUrls.fetch_urls(app)