import os
from os import getenv

"""Application configuration"""
# system import
import os


class Config:
    """Base config class"""
    DEBUG = True
    SECRET = os.getenv('SECRET')


class Development(Config):
    """Development configurations"""
    DEBUG = True


class Testing(Config):
    """Testing configurations"""
    DEBUG = True
    TESTING = True
    SECRET_KEY = "SECRET"


configuration = {
    "development": Development,
    "testing": Testing
}
