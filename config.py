import secrets


class Config(object):
    """
    Base configuration class for flask application
    """

    # Debug mode set to false
    DEBUG = False

    # Generate secret key with secure random algorithm
    SECRET_KEY = secrets.token_hex(16)

    # Database configs
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Location for client csv
    CLIENT_CSV = "static/client/csv/"


class Production(Config):
    """
    Configurations used for production, inherited from Config class 
    """

    # Protect cookies
    SESSION_COOKIE_SECURE = True,
    SESSION_COOKIE_HTTPONLY = True


class Development(Config):
    """
    Configurations used for development, inherited from Config class
    """

    # Debug mode set to true
    DEBUG = True
