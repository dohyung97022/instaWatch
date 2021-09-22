from ..Active import Active, State
from modules.subprocess import sub_process
from modules.subprocess.classes import registry


def set_proxy_enable(enable: bool):
    return sub_process.start(registry.InternetSetting.set_proxy_enable_cmd(enable))


def run_exit():
    Active.state = State.exit

    Active.processes.append(set_proxy_enable(False))
    for process in Active.processes:
        sub_process.kill(process)
    Active.instance.terminate()

    Active.reset()
