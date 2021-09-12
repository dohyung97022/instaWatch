from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..dotenv.classes.database import Database

engine = create_engine(
    f'{Database.name}'
    f'://{Database.username}'
    f':{Database.password}'
    f'@{Database.endpoint}'
    f':{Database.port}'
    f'/{Database.schema}'
    f'?charset=utf8', echo=True)

session = sessionmaker(engine)()
Base = declarative_base()


def init_setup():
    from .model import action, event, event_action
    Base.metadata.create_all(engine)
