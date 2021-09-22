def connect_cmd(ip: str) -> list[str]:
    return ['ssh', '-o', 'StrictHostKeyChecking=no', '-i', r'pem\vpc.pem', 'ubuntu@' + ip, '-D', '4444']


def is_connected(process_read: str) -> bool:
    if 'Welcome' in process_read:
        return True
    return False
