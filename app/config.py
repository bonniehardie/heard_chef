import os

class Configuration:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "postgresql://heard_chef:password@localhost/heard_chef"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
