from .runnable.action_runnable import run_action
from .runnable.check_runnable import run_check
from .runnable.event_runnable import run_event
from .runnable.init_runnable import run_init
from .runnable.trigger_runnable import run_trigger
from .Active import Active, State


def run():
    if Active.state == State.init:
        run_init()
    elif Active.state == State.trigger:
        run_trigger()
    elif Active.state == State.event:
        run_event()
    elif Active.state == State.action:
        run_action()
    elif Active.state == State.check:
        run_check()
