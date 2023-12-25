from aiogram.fsm.state import StatesGroup, State

class GetQuestion(StatesGroup):
    waiting_for_question = State()
