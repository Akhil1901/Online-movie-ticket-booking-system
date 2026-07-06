from .config import Config


class TestingConfig(Config):

    TESTING = True

    DEBUG = True

    ENV = "testing"