import asyncio

from aiogram import Bot
from app import config


async def delete_webhook():
    async with Bot(token=config.BOT_TOKEN) as bot:
        await bot.delete_webhook(drop_pending_updates=True)

if __name__ == '__main__':
    asyncio.run(delete_webhook())
