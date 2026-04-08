import asyncio
from aiogram import Bot
from django.conf import settings
from django.core.management.base import BaseCommand
from capitals.init_dispatcher import init_dispatcher



async def run_bot() -> None:
    """
    Запуск бота
    """
    dispatcher = await init_dispatcher()
    # запуск бота
    bot = Bot(token=settings.BOT_TOKEN)
    await dispatcher.start_polling(bot)


class Command(BaseCommand):
    """
    Запуск бота
    """
    help = "Closes the specified poll for voting"


    def handle(self, *args, **options):
        asyncio.run(run_bot())
