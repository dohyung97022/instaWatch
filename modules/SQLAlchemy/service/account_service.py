from ..sql_alchemy import session
from ..model.account import Account
from datetime import datetime


def find_by_loop_ran_at_before(before: datetime) -> Account:
    return session.query(Account).filter(Account.loop_ran_at < before).first()


def update_loop_ran_at(loop_ran_at: datetime, account: Account):
    account.loop_ran_at = loop_ran_at
    session.commit()
