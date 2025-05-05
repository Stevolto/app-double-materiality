import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme')
    BABEL_DEFAULT_LOCALE = 'it'
    LANGUAGES = ['it', 'en', 'de']
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'data', 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
