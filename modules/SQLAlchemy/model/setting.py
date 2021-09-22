from ..sql_alchemy import Base
from sqlalchemy import Column, Integer, Interval, Enum
from datetime import timedelta
import enum


class Type(enum.Enum):
    instagram = 'instagram'


class Setting(Base):
    __tablename__ = "setting"
    id = Column(Integer, primary_key=True)
    type = Column(Enum(Type))
    account_run_interval = Column(Interval)
    account_next_interval = Column(Interval)

    def __init__(self, email: str, type: Type, account_run_interval: timedelta, account_next_interval: timedelta):
        self.email = email
        self.type = type
        self.account_run_interval = account_run_interval
        self.account_next_interval = account_next_interval
