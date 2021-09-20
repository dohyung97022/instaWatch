from subprocess import Popen, call


def start(cmd: list[str]) -> Popen:
    return Popen(cmd)


def kill(subprocess: Popen):
    subprocess.terminate()
    subprocess.kill()


def kill_all(process_name: str):
    call(['taskKill', '/IM', process_name, '/F'])
