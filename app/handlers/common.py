"""
Основные обработчики
"""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.keyboars.reply import main_menu_keyboard

router = Router()


@router.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    """
    Обработчик команды /start
    """
    text = (
        'Привет, я бот - результат домашнего задания по курсу OTUS. '
        'Юзай меню внизу или команды /start, /help для навигации. '
    )
    await message.answer(text, reply_markup=main_menu_keyboard)


@router.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    """
    Обработчик команды /help
    """
    text = (
        'Привет, я бот - результат домашнего задания по курсу OTUS. '
        'Юзай меню внизу или команды /start, /help для навигации. '
    )
    await message.answer(text, reply_markup=main_menu_keyboard)
