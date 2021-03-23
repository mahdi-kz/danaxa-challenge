from os import environ
from os.path import (
    abspath,
    dirname,
)

service_status = {'running': 'running', 'idle': 'idle', 'to stop': 'to stop', 'stopped': 'stopped'}


class Environment:
    service_status = service_status['stopped']


class Config:
    from dotenv import load_dotenv
    load_dotenv()
    DEBUG = True
    TESTING = True
    SERVER_NAME = environ.get("SERVER_NAME")
    SECRET_KEY = environ.get("SECRET_KEY")
    BASE_DIR = abspath(dirname(__file__))
    # REDIS_URL = "redis://redis:6379/0"
    # RQ_REDIS_URL = "redis://redis:6379/0"
