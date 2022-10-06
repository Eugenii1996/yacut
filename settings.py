import os
from string import ascii_letters, digits


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', '1234567890')
    VALID_SYMBOLS = ascii_letters + digits
    ORIGINAL_LEGTH = 2000
    SHORT_LENGTH = 16
    RANDOM_SHORT_LENGTH = 6
