from subprocess import Popen, call, PIPE


def start(cmd: list[str]) -> Popen:
    return Popen(cmd, stdout=PIPE, stderr=PIPE)


def read(subprocess: Popen) -> str:
    return subprocess.stdout.readline().decode('utf-8').strip()


def kill(subprocess: Popen):
    subprocess.terminate()
    subprocess.kill()


def kill_all(process_name: str):
    call(['taskKill', '/IM', process_name, '/F'])
