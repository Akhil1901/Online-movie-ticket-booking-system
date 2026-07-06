import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Base Configuration
    """

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "movie_ticket_secret_key"
    )

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "movie_ticket_jwt_secret"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JSON_SORT_KEYS = False

    PROPAGATE_EXCEPTIONS = True

    DEBUG = False

    TESTING = False