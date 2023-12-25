from loguru import logger
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from support_bot import config

bot = Bot(token=config.SUPPORT_BOTAPI_TOKEN, parse_mode='html')
dp = Dispatcher(storage=MemoryStorage())


class InterceptHandler(logging.Handler):
    def emit(self, record):
        level = logger.level(record.levelname).name
        logger.log(level, record.getMessage())


async def bot_entrypoint() -> None:
    # avoid a circular import
    from support_bot.handlers import main, dialog, callback

    dp.include_routers(
        main.router,
        dialog.router,
        callback.router,
    )

    logging.getLogger('aiogram').setLevel(logging.DEBUG)
    logging.getLogger('aiogram').addHandler(InterceptHandler())

    logging.getLogger('asyncio').setLevel(logging.DEBUG)
    logging.getLogger('asyncio').addHandler(InterceptHandler())

    await dp.start_polling(bot)
