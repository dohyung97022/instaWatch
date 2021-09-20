from ..Active import Active, State
from modules.subprocess import sub_process
from modules.subprocess.classes import firefox, ssh, registry


def execute_firefox(profile: str):
    return sub_process.start(firefox.execute_cmd(profile))


def connect_ssh(ip: str):
    process = sub_process.start(ssh.connect_cmd(ip))
    if not ssh.is_connected(process):
        # TODO : 다른 exception 을 만들어 log 로 핸들하기
        print('ssh is not connected')
    return process


def set_proxy_enable(enable: bool):
    return sub_process.start(registry.InternetSetting.set_proxy_enable_cmd(enable))


def set_proxy_server():
    return sub_process.start(registry.InternetSetting.set_proxy_server_cmd())


def run_init():
    processes = []
    processes.append(execute_firefox('1'))
    processes.append(connect_ssh('3.35.131.60'))
    processes.append(set_proxy_enable(True))
    processes.append(set_proxy_server())

    for process in processes:
        sub_process.kill(process)

    Active.state = State.trigger
