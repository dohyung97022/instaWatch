from ..Active import Active, State


def run_action():
    Active.state = State.action

    Active.state = State.check
