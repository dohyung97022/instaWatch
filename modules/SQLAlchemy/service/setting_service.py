from ..sql_alchemy import session
from ..model.setting import Setting, Type


def find_by_type(type: Type) -> Setting:
    return session.query(Setting).filter(Setting.type == type).one()
