from ..Active import Active, State
from modules.aws.classes.ec2 import EC2
from modules.SQLAlchemy.service import setting_service
from modules.SQLAlchemy.service import account_service
from modules.SQLAlchemy.model.setting import Type
from datetime import datetime
from ..service.init_service import *


def run_init():
    Active.state = State.init

    Active.settings = setting_service.find_by_type(Type.instagram)
    Active.account = account_service.find_by_loop_ran_at_before(datetime.now() - Active.settings.account_run_interval)
    if Active.account is None:
        Active.loop = 0
        return
    Active.loop = Active.account.loop
    account_service.update_loop_ran_at(datetime.now(), Active.account)

    Active.instance = EC2.create_instance('vpc')
    Active.instance.wait_until_running()
    Active.instance.reload()

    Active.processes.append(connect_ssh(Active.instance.get_ip()))
    Active.processes.append(set_proxy_enable(True))
    Active.processes.append(set_proxy_server())
    Active.processes.append(set_default_browser_firefox())
    Active.processes.append(execute_firefox(str(Active.account.id), 'https://api.ipify.org'))

    Active.state = State.trigger
