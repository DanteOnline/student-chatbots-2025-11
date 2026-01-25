"""
Entrypoint для запуска бота
"""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from app.db import init_db
from app.handlers import (
    about,
    common,
    errors,
    faq,
    form,
)
from app.middlewares.logging import LoggingMiddleware

logging.basicConfig(
    level=logging.INFO,
    format=('%(asctime)s | %(levelname)s | %(name)s | %(message)s'),
)

logger = logging.getLogger('bot')


async def main() -> None:
    """
    Запуск бота
    """
    await init_db()

    dp = Dispatcher()
    # middlewares
    dp.message.middleware(LoggingMiddleware())
    dp.callback_query.middleware(LoggingMiddleware())

    # routers
    # для ошибок
    dp.include_router(errors.router)
    # основные
    dp.include_router(common.router)
    dp.include_router(about.router)
    dp.include_router(faq.router)
    dp.include_router(form.router)

    # запуск бота
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
