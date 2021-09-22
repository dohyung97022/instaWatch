import enum


class State(enum.Enum):
    init = 'init'
    trigger = 'trigger'
    event = 'event'
    action = 'action'
    check = 'check'
    exit = 'exit'


class Active:
    state = State.init
    settings = None
    account = None
    loop = 0
    instance = None
    triggers = []
    events = []
    actions = []
    processes = []

    @classmethod
    def reset(cls):
        cls.state = State.init
        cls.settings = None
        cls.account = None
        cls.loop = 0
        cls.instance = None
        cls.triggers = []
        cls.events = []
        cls.actions = []
        cls.processes = []
