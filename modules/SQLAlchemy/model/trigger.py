from ..sql_alchemy import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Trigger(Base):
    __tablename__ = 'trigger'
    id = Column(Integer, primary_key=True)
    url = Column(String(100))
    relative_x = Column(Integer)
    relative_y = Column(Integer)
    relative_w = Column(Integer)
    relative_h = Column(Integer)
    event_id = Column(Integer, ForeignKey('event.id'))

    def __init__(self, url: str, relative_x: int, relative_y: int, relative_w: int, relative_h: int):
        self.url = url
        self.relative_x = relative_x
        self.relative_y = relative_y
        self.relative_w = relative_w
        self.relative_h = relative_h
