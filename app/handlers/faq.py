"""
Раздел FAQ
"""

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from app.keyboars.inline import (
    answers,
    faq_keyboard,
)
from app.keyboars.reply import FAQ_BUTTON_TEXT

router = Router()


@router.message(F.text == FAQ_BUTTON_TEXT)
async def faq_text_handler(message: Message) -> None:
    """
    Обработчик ввода "FAQ"
    """
    text = 'Часто задаваемые вопросы:'
    await message.answer(text, reply_markup=faq_keyboard)


def make_handler(answer_: str):
    """
    Создание обработчика для одного FAQ
    """

    async def handler(callback: CallbackQuery):
        await callback.message.answer(answer_)

    return handler


for question, answer in answers.items():
    router.callback_query(F.data == question)(make_handler(answer))
