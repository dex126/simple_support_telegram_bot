from aiogram import types


async def create_buttons(id: int) -> types.InlineKeyboardMarkup:
    buttons = types.InlineKeyboardMarkup(inline_keyboard=[
                [
                    types.InlineKeyboardButton(text='↖️ Ответить', callback_data=f'answer-{id}')
                ], [
                    types.InlineKeyboardButton(text='📛 Забанить', callback_data=f'ban-{id}')
                ],
            ]
        )
    
    return(buttons)


async def answer_button() -> types.InlineKeyboardMarkup:

    markup = types.InlineKeyboardMarkup(inline_keyboard=[
                [
                    types.InlineKeyboardButton(text='↖️ Ответить', callback_data=f'answer_user')
                ],
            ]
        )
    
    return(markup)