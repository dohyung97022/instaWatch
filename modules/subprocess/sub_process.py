from subprocess import Popen, call, PIPE


def start(cmd: list[str]) -> Popen:
    return Popen(cmd, stdout=PIPE, stderr=PIPE)


def read(subprocess: Popen) -> str:
    result = ''
    if is_finished(subprocess):
        lines = subprocess.stdout.readlines()
        for line in lines:
            result += line.decode('utf-8').strip() + '\n'
    else:
        result = subprocess.stdout.readline().decode('utf-8').strip()
    return result


def is_finished(subprocess: Popen) -> bool:
    return subprocess.poll() is not None


def wait_until_finished(subprocess: Popen):
    while not is_finished(subprocess):
        continue


def kill(subprocess: Popen):
    subprocess.terminate()
    subprocess.kill()


def kill_all(process_name: str):
    call(['taskKill', '/IM', process_name, '/F'])
