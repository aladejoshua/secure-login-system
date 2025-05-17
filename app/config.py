# Configuration settings (e.g., database URI, secret key)
import os

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../instance/database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False