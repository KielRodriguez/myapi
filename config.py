import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class DevelpmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    DEBUG = False
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

