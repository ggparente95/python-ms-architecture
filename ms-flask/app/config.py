import os


SECRET_KEY = 'secretpass123'
ENVIRONMENT = os.getenv('FLASK_ENV')
MESSAGE_CERBERUS = "Invalid request parameters"


class ConfigDev(object):
    """Esta clase tiene las configuraciones necesarias para Desarrollo
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigTest(object):
    """Esta clase tiene las configuraciones necesarias para Desarrollo
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
