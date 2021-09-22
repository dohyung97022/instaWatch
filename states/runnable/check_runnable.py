from ..Active import Active, State


def run_check():
    Active.state = State.check

    Active.state = State.trigger
