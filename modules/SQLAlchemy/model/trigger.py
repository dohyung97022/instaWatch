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

    def __init__(self, url):
        self.url = url
