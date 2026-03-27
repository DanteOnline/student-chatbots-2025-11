from aiogram import F, Router
from aiogram.types import Message

from app.services.states import ask

router = Router()

@router.message(~F.text.startswith("/"), ~F.voice)
async def ask_handler(message: Message) -> None:
    """
    Ответ на текстовое сообщение (вопрос пользователя)
    :param message: сообщение пользователя
    :return: None
    """
    text = message.text
    thinking = await message.answer("Думаю...")
    answer = await ask(text)
    await thinking.edit_text(answer)
