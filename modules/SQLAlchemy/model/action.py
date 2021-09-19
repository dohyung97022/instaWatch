from .event_action import event_action
from ..sql_alchemy import Base
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship
import enum


class Type(enum.Enum):
    click = 'click'
    hover = 'hover'
    type = 'type'
    macro = 'macro'


class Action(Base):
    __tablename__ = "action"
    id = Column(Integer, primary_key=True)
    type = Column(Enum(Type))
    events = relationship('Event', secondary=event_action, back_populates='actions')

    def __init__(self, name):
        self.name = name
