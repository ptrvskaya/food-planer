from aiogram.fsm.state import State, StatesGroup


class MyFSMStates(StatesGroup):
    DELETE = State()
    ADD = State()
