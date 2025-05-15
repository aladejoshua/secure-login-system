# Initialize Flask app, configure extensions
# app/__init__.py
import os
from flask import Flask, render_template, redirect, url_for, request
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)

    # Basic configuration (optional)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Replace with a secure key

    # Register routes (you can modularize this later)
    
    app.register_blueprint(auth_bp)
    @app.route('/')
    def home():
        return render_template('register.html')
     
    return app


