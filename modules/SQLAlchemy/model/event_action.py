from ..sql_alchemy import Base
from sqlalchemy import Column, ForeignKey, Table

event_action = Table(
    'event_action',
    Base.metadata,
    Column('action_id', ForeignKey('action.id'), primary_key=True),
    Column('event_id', ForeignKey('event.id'), primary_key=True)
)
