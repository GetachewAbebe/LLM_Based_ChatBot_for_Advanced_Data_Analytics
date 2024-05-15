import os

class Config:
    SECRET_KEY = os.urandom(24)
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()
