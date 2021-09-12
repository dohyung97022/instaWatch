from .event_action import event_action
from ..sql_alchemy import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Action(Base):
    __tablename__ = "action"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    events = relationship('Event', secondary=event_action, back_populates='actions')

    def __init__(self, name):
        self.name = name
