from ..sql_alchemy import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    loop = Column(Integer)
    loop_ran_at = Column(DateTime)

    def __init__(self, email: str, loop: int):
        self.email = email
        self.loop = loop
        self.loop_ran_at = datetime.now()
