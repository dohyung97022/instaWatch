from .runnable.action_runnable import run_action
from .runnable.check_runnable import run_check
from .runnable.event_runnable import run_event
from .runnable.init_runnable import run_init
from .runnable.trigger_runnable import run_trigger
from .runnable.exit_runnable import run_exit
from .Active import Active, State


def run():
    if Active.state == State.trigger:
        run_trigger()
    elif Active.state == State.event:
        run_event()
    elif Active.state == State.action:
        run_action()
    elif Active.state == State.check:
        Active.loop -= 1
        run_check()


def run_loops():
    run_init()
    while Active.loop > 0:
        run()
    run_exit()
