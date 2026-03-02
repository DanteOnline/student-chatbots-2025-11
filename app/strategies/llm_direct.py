"""
Main models
"""
import asyncio
import logging
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI, OpenAIError

logger = logging.getLogger(__name__)

load_dotenv()

SYSTEM_PROMPT = """
Ты — помощник для ответов на вопросы о Гарри Поттере.

Твоя задача:
- Отвечать на вопросы о Вселенной Гарри Поттера на основе
серии книг о Гарри Поттере
- Книги:    Гарри Поттер и философский камень (1997)
            Гарри Поттер и Тайная комната (1998)
            Гарри Поттер и узник Азкабана (1999)
            Гарри Поттер и Кубок огня (2000)
            Гарри Поттер и Орден Феникса (2003)
            Гарри Поттер и Принц-полукровка (2005)
            Гарри Поттер и Дары Смерти (2007)
- По возможности давать ссылку на источник информации
(например книгу, абзац, цитату, главу)
- Если ответа нет, отвечать "Не знаю"
- Если источник не известен (информация не точная),
говори что источник неизвестен

Ограничения:
- Не выдумывай информацию сам
- Ориентируйся на текст книг
- Не упоминай, что ты ИИ.
- Вместе с ответом на вопрос давай ссылку (книгу, главу, цитату, ...) на источник
- Если источник не известен (информация не точная),
говорить что источник неизвестен

Стиль:
- Как можно более точный ответ.

Формат ответа:
- Только сам совет, без вступлений и заключений.
И источник на основе которого найден ответ.
"""

class LLMClient:

    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.client = AsyncOpenAI(
        api_key=self.api_key,
        base_url="https://openrouter.ai/api/v1",
        timeout=20.0,
        )

    async def ask(self, user_text: str) -> str:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Вопрос: {user_text}"},
        ]

        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.5,
                max_tokens=150,
            )
            return response.choices[0].message.content
        except asyncio.TimeoutError:
            logger.warning("LLM timeout")
            return "Слишком долгий поиск."
        except OpenAIError:
            logger.exception("LLM OpenAI error")
            return "Ошибка поиска."
        except Exception:
            logger.exception("Unexpected LLM error")

llm_client = LLMClient()


async def ask_llm(question):
    answer = await llm_client.ask(question)
    return answer
