# Initialize Flask app, configure extensions
# app/__init__.py
import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Basic configuration (optional)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Replace with a secure key

    # Register routes (you can modularize this later)
    @app.route('/')
    def home():
        return 'Hello, Flask!'

    return app