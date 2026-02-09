from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.models import LLMClient

router = Router()
llm_client = LLMClient()

@router.message(Command("ask"))
async def ask_handler(message: Message) -> None:
    text = message.text.replace("/ask", "").strip()
    if not text:
        await message.answer("Задайте вопрос после команды /ask")
        return
    if len(text) > 500:
        await message.answer("Слишком серьёзная проблема. Я такое не потяну.")
        return
    thinking = await message.answer("Думаю...")
    answer = await llm_client.ask(text)
    await thinking.edit_text(answer)
