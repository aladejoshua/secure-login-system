import os
from flask import Flask, render_template
from app.routes.auth import auth_bp
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp)
    app.config.from_object(Config)
    db.init_app(app)

    @app.route('/')
    def home():
        return render_template('register.html')
    
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    return app
