from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.strategies import get_strategy, search

router = Router()

@router.message(Command("ask"))
async def ask_handler(message: Message) -> None:
    question = message.text.replace("/ask", "").strip()
    if not question:
        await message.answer("Задайте вопрос после команды /ask")
        return
    if len(question) > 500:
        await message.answer("Слишком серьёзная проблема. Я такое не потяну.")
        return
    thinking = await message.answer("Думаю...")
    # answer = await llm_client.ask(text)
    # await thinking.edit_text(answer)
    search_strategy = await get_strategy()
    answer = await search(question, search_strategy)
    await thinking.edit_text(answer)
