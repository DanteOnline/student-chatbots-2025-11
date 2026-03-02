import asyncio
import logging
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI, OpenAIError

logger = logging.getLogger(__name__)

load_dotenv()

class LLMClient:

    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.client = AsyncOpenAI(
            api_key=self.api_key,
            base_url="https://openrouter.ai/api/v1",
            timeout=20.0,
        )


    async def ask(self, messages) -> str:

        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.3,
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


async def get_llm_client() -> LLMClient:
    return LLMClient()
