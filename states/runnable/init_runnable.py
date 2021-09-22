from ..Active import Active, State
from modules.subprocess import sub_process
from modules.subprocess.classes import firefox, ssh, registry, set_default_browser
from modules.aws.classes.ec2 import EC2



def execute_firefox(profile: str, url: str):
    return sub_process.start(firefox.execute_cmd(profile, url))


def connect_ssh(ip: str, retry: int = 50):
    connected_process = None
    for x in range(retry):
        process = sub_process.start(ssh.connect_cmd(ip))
        if ssh.is_connected(sub_process.read(process)):
            connected_process = process
            break
        sub_process.kill(process)

    if connected_process is None:
        # TODO : Exception 으로 따로 빼내기
        print('connecting to ssh has failed')
        exit()
    return connected_process


def set_proxy_enable(enable: bool):
    return sub_process.start(registry.InternetSetting.set_proxy_enable_cmd(enable))


def set_proxy_server():
    return sub_process.start(registry.InternetSetting.set_proxy_server_cmd())


def set_default_browser_firefox():
    cmd = set_default_browser.read_all_browser_info_cmd()
    process = sub_process.start(cmd)
    sub_process.wait_until_finished(process)
    all_browser_info = sub_process.read(process)
    sub_process.kill(process)
    firefox_hklm = set_default_browser.read_firefox_hklm_cmd(all_browser_info)
    cmd = set_default_browser.set_default_browser_cmd(firefox_hklm)
    return sub_process.start(cmd)


def set_default_browser_chrome():
    cmd = set_default_browser.set_default_browser_cmd(set_default_browser.chrome_hklm)
    return sub_process.start(cmd)


def run_init():
    Active.state = State.init

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
