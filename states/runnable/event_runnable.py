from ..Active import Active, State


def run_event():
    Active.state = State.event

    Active.state = State.action

