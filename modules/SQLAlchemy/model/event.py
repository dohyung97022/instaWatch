from .event_action import event_action
from ..sql_alchemy import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    triggers = relationship("Trigger")
    actions = relationship('Action', secondary=event_action, back_populates='events')

    def __init__(self, name):
        self.name = name
