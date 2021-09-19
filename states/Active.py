import enum


class State(enum.Enum):
    init = 'init'
    trigger = 'trigger'
    event = 'event'
    action = 'action'
    check = 'check'


class Active:
    state = State.init
    account = ''
    triggers = []
    events = []
    actions = []
