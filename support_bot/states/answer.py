from aiogram.fsm.state import StatesGroup, State

class GetAnswer(StatesGroup):
    waiting_for_answer = State()
