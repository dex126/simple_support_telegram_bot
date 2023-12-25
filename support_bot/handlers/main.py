from aiogram import Router, filters, types
from aiogram.fsm.context import FSMContext

from support_bot import config
from support_bot.modules import base
from support_bot.states import question

router = Router()


@router.message(filters.Command(commands='start'))
async def send_menu(message: types.Message, state: FSMContext):
    await state.clear()

    if message.from_user.id == config.ADMIN:
        await message.answer(text='<b>Support Bot</b>')

    else:
        if not base.db.contains(base.Users.blacklist == message.from_user.id):
            if not base.db.contains(base.Users.id == message.from_user.id):
                await message.answer('<b>Напишите ваш вопрос ниже, и мы постараемся ответить как можно скорее.</b>')
                await state.set_state(question.GetQuestion.waiting_for_question)
            else:
                await message.answer('<b>Пожалуйста, дождитесь ответа</b>')

        else:
            await message.answer('Go away!')
