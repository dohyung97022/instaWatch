from ..Active import Active, State
from modules.subprocess import sub_process

firefox_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
firefox_profile_option = '-P'
firefox_process_name = 'firefox.exe'


def run_init():
    sub_process.start([firefox_location, firefox_profile_option, '1'])
    Active.state = State.trigger
