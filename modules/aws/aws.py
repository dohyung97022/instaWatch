import boto3
from modules.dotenv.classes.aws_credentials import AWSCredentials


class AWS:
    session = boto3.Session(
        aws_access_key_id=AWSCredentials.access_key_id,
        aws_secret_access_key=AWSCredentials.secret_access_key,
    )

    class Settings:
        region = 'ap-northeast-2'
