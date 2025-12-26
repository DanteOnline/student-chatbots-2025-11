"""
Entrypoint для запуска бота
"""
import logging
import asyncio

from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from app.handlers import (
    common,
    about,
    faq,
    form,
)

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

async def main() -> None:
    """
    Запуск бота
    """
    dp.include_router(common.router)
    dp.include_router(about.router)
    dp.include_router(faq.router)
    dp.include_router(form.router)
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
