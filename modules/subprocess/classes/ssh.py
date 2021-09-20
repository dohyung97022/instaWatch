from subprocess import Popen


def connect_cmd(ip: str) -> list[str]:
    return ['ssh', '-o', 'StrictHostKeyChecking=no', '-i', r'pem\vpc.pem', 'ubuntu@' + ip, '-D', '4444']


def is_connected(subprocess: Popen) -> bool:
    if 'Welcome' in subprocess.stdout.readline().decode("utf-8").strip():
        return True
    return False
