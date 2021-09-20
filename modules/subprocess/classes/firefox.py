location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
process_name = 'firefox.exe'


def execute_cmd(profile: str) -> list[str]:
    return [location, '-P', profile]
