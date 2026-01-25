"""
Раздел о нас
"""

from aiogram import F, Router
from aiogram.types import Message

from app.keyboars.reply import ABOUT_BUTTON_TEXT

router = Router()


@router.message(F.text == ABOUT_BUTTON_TEXT)
async def about_text_handler(message: Message) -> None:
    """
    Обработчик ввода "О нас"
    """
    text = '<i>Этот</i> бот был создан для домашнего задания курса <b>OTUS.</b>'
    await message.answer(text, parse_mode='HTML')
