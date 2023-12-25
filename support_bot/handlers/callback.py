from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from support_bot.bot import dp
from support_bot.modules import base
from support_bot.states import answer, question

router = Router()


@dp.callback_query()
async def process_callback(call: types.CallbackQuery, state: FSMContext):
    data = call.data.split('-')
    await call.answer()

    if data[0] == 'ban':
        base.db.remove(base.Users.id == int(data[1]))
        base.db.insert({'blacklist': int(data[1])})
        await call.message.edit_text(call.message.text + '\n\nЗаблокирован')
    
    if data[0] == 'answer':
        await call.message.answer('<b>Введите текст для ответа</b>')
        await state.set_state(answer.GetAnswer.waiting_for_answer)
        await state.set_data({'id': int(data[1])})
        await call.message.edit_text(call.message.text+'\n\nОтвечено')

    if data[0] == 'answer_user':
        await call.message.answer('<b>Введите текст для ответа</b>')
        await state.set_state(question.GetQuestion.waiting_for_question)
        await call.message.edit_text(call.message.text+'\n\nОтвечено')
