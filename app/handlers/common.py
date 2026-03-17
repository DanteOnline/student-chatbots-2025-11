"""
Основные обработчики
"""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


async def info_handler(message: Message) -> None:
    """
    Информация о боте для пользователя
    """
    text = ('Тебя приветствует "Генератор тупых советов". '
            'Я могу решить любую твою проблему. '
            'Просто задай мне любой вопрос!?'
            'Например "Как мне построить дом?".'
            '\n'
            '\n'
            'Можешь писать текстом, а можешь и голосом ;)')
    await message.answer(text)

@router.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    """
    Обработчик команды /start
    """
    await info_handler(message)


@router.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    """
    Обработчик команды /help
    """
    await info_handler(message)
