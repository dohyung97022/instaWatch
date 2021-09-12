import modules.dotenv.dot_env
from os import environ

DATABASE_NAME = 'DATABASE_NAME'
DATABASE_USERNAME = 'DATABASE_USERNAME'
DATABASE_PASSWORD = 'DATABASE_PASSWORD'
DATABASE_ENDPOINT = 'DATABASE_ENDPOINT'
DATABASE_PORT = 'DATABASE_PORT'
DATABASE_SCHEMA = 'DATABASE_SCHEMA'


class Database:
    name = environ[DATABASE_NAME]
    username = environ[DATABASE_USERNAME]
    password = environ[DATABASE_PASSWORD]
    endpoint = environ[DATABASE_ENDPOINT]
    port = environ[DATABASE_PORT]
    schema = environ[DATABASE_SCHEMA]
