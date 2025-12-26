"""
Раздел FAQ
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.keyboars.reply import FAQ_BUTTON_TEXT
from app.keyboars.inline import (
    faq_keyboard,
    answers,
)

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
    router.callback_query(F.data == question)(
        make_handler(answer)
    )
