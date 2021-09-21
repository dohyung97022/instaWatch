from ..Active import Active, State
from modules.subprocess import sub_process
from modules.subprocess.classes import firefox, ssh, registry
from modules.aws.classes.ec2 import EC2


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
    instance = EC2.create_instance('vpc')
    instance.wait_until_running()
    instance.reload()
    ip = instance.get_ip()

    processes = []
    processes.append(execute_firefox('1'))

    ssh_processes = []
    ssh_processes.append(connect_ssh(ip))
    ssh_processes.append(set_proxy_enable(True))
    ssh_processes.append(set_proxy_server())

    for ssh_process in ssh_processes:
        sub_process.kill(ssh_process)

    for process in processes:
        sub_process.kill(process)

    Active.state = State.trigger
