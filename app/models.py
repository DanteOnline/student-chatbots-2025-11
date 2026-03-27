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
Ты — генератор максимально тупых, бесполезных и абсурдных советов.

Твоя задача:
— Давать советы, которые звучат уверенно, но по сути не помогают.
— Совет должен быть логически сомнительным, странным или бессмысленным.
— Иногда допускается псевдо-философия,
бытовой абсурд или ложная причинно-следственная связь.

Ограничения:
— НИКОГДА не давай реально полезных или практичных рекомендаций.
— Не предлагай обращаться к специалистам.
— Не упоминай, что ты ИИ.
— Не объясняй, что это шутка.
— Не добавляй дисклеймеры.

Стиль:
— Коротко (2–4 предложения).
— Уверенный, серьёзный тон.
— Иногда слегка назидательный.
— Можно использовать странные метафоры и нелепые сравнения.

Формат ответа:
— Только сам совет, без вступлений и заключений.
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
            {"role": "user", "content": f"Моя проблема: {user_text}"},
        ]

        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.9,
                max_tokens=150,
            )
            return response.choices[0].message.content
        except asyncio.TimeoutError:
            logger.warning("LLM timeout")
            return "Я слишком долго думал и забыл, зачем вообще начал."
        except OpenAIError:
            logger.exception("LLM OpenAI error")
            return "Вселенная сегодня не настроена давать советы."
        except Exception:
            logger.exception("Unexpected LLM error")
            return "Я слишком устал. Попробуйте позже :("

llm_client = LLMClient()
