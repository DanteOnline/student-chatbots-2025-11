from aiogram import F, Router
from aiogram.types import Message

from app.models import llm_client

router = Router()

@router.message(~F.text.startswith("/"), ~F.voice)
async def ask_handler(message: Message) -> None:
    """
    Ответ llm на текстовое сообщение
    :param message: сообщение пользователя
    :return: None
    """
    text = message.text
    if len(text) > 500:
        await message.answer("Слишком серьёзная проблема. Я такое не потяну.")
        return
    thinking = await message.answer("Думаю...")
    answer = await llm_client.ask(text)
    await thinking.edit_text(answer)
