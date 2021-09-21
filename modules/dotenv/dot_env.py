from dotenv import load_dotenv

DATABASE_ENV_PATH = './env/database.env'
AWS_ENV_PATH = './env/aws.env'

load_dotenv(dotenv_path=DATABASE_ENV_PATH)
load_dotenv(dotenv_path=AWS_ENV_PATH)