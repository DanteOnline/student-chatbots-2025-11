"""
Основные обработчики
"""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, User
from users.models import create_user
from .fetch_capitals import get_capital



router = Router()


async def info_handler(message: Message) -> None:
    """
    Информация о боте для пользователя
    """
    text = ('Привет. Я бот - географ. '
            'Я могу найти сказать столицу любой страны. '
            'Напиши название страны после команды /capital. '
            'Например "/capital Russia".')
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


@router.message(Command("capital"))
async def get_capital_handler(message: Message) -> None:
    """
    Находим столицу страны
    :param message: сообщение пользователя
    :return: None
    """
    # сохраняем пользователя
    await save_user(message.from_user)
    country_name = message.text.replace("/capital", "").strip()
    if not country_name:
        await message.answer("Задайте вопрос после команды /capital")
        return
    thinking = await message.answer("Ищу информацию...")
    answer = await get_capital(country_name)
    await thinking.edit_text(answer)


async def save_user(from_user: User) -> None:
    """
    Сохраняем пользователя
    :param from_user: Пользователь telegram
    :return:
    """
    await create_user(
        from_user.id,
        from_user.first_name,
        from_user.last_name
    )
