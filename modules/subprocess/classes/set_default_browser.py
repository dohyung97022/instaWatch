import re

location = r'exe\SetDefaultBrowser.exe'
chrome_hklm = 'Google Chrome'


def read_all_browser_info_cmd() -> list[str]:
    return [location]


def read_firefox_hklm_cmd(all_browser_info: str) -> str:
    return re.search('Firefox-[^\n]+', all_browser_info).group(0)


def set_default_browser_cmd(hklm: str) -> list[str]:
    return [location, 'HKLM', hklm]
