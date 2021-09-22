from subprocess import Popen, call, PIPE


def start(cmd: list[str]) -> Popen:
    return Popen(cmd, stdout=PIPE, stderr=PIPE)


def read(subprocess: Popen) -> str:
    result = ''
    lines = subprocess.stdout.readlines()
    for line in lines:
        result += line.decode('utf-8').strip() + '\n'
    return result


def kill(subprocess: Popen):
    subprocess.terminate()
    subprocess.kill()


def kill_all(process_name: str):
    call(['taskKill', '/IM', process_name, '/F'])
