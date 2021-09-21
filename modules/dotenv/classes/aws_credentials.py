import modules.dotenv.dot_env
from os import environ

AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'


class AWSCredentials:
    access_key_id = environ[AWS_ACCESS_KEY_ID]
    secret_access_key = environ[AWS_SECRET_ACCESS_KEY]
