from ..sql_alchemy import Base
from sqlalchemy import Column, Integer, Time
from datetime import time


class Setting(Base):
    __tablename__ = "setting"
    id = Column(Integer, primary_key=True)
    account_run_loop_interval = Column(Time)
    account_next_interval = Column(Time)

    def __init__(self, email: str, account_run_loop_interval: time, account_next_interval: time):
        self.email = email
        self.account_run_loop_interval = account_run_loop_interval
        self.account_next_interval = account_next_interval
