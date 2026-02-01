"""
Entrypoint для запуска бота
"""

import asyncio
import logging

from aiogram import Bot
from app import init_dispatcher
from app.config import BOT_TOKEN

logging.basicConfig(
    level=logging.INFO,
    format=('%(asctime)s | %(levelname)s | %(name)s | %(message)s'),
)

logger = logging.getLogger('bot')


async def main() -> None:
    """
    Запуск бота
    """
    dispatcher = await init_dispatcher()
    # запуск бота
    bot = Bot(token=BOT_TOKEN)
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
