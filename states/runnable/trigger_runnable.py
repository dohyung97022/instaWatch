from ..Active import Active, State


def run_trigger():
    Active.state = State.trigger

    Active.state = State.event
