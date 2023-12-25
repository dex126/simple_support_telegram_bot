from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from support_bot import config, bot
from support_bot.modules import base, utils
from support_bot.states import question, answer
from support_bot.handlers.main import send_menu

router = Router()


@router.message(question.GetQuestion.waiting_for_question)
async def get_question(message: types.Message):
    if base.db.contains(base.Users.id == message.from_user.id):
        await message.answer('<b>Пожалуйста, дождитесь ответа</b>')
    
    else:
        if not base.db.contains(base.Users.blacklist == message.from_user.id):
            await message.answer('<b>Ваше сообщение отправлено оператору.</b>')

            buttons = await utils.create_buttons(message.from_user.id)
            await bot.bot.send_message(config.ADMIN, f'{message.from_user.first_name} '
                                    f'(@{message.from_user.username}):\n\n{message.text}',
                                    reply_markup=buttons)
            
            base.db.insert({"id": message.from_user.id})
        else:
            await message.answer('Go away!')


@router.message(answer.GetAnswer.waiting_for_answer)
async def get_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer('<b>Ваш ответ отправлен юзеру</b>')

    markup = await utils.answer_button()

    await bot.bot.send_message(data["id"], message.text, reply_markup=markup)
    
    base.db.remove(base.Users.id == data["id"])
    await state.clear()
