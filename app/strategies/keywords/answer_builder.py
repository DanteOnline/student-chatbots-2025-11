"""
Сборка ответа с цитатой: контекст (найденные чанки)
+ вопрос -> промпт -> GhatGPT -> ответ + источник.
Правило: отвечай только по контексту;
если ответа нет — скажи «не знаю».
"""
from dotenv import load_dotenv

from app.llm_client import get_llm_client

load_dotenv()

SYSTEM_PROMPT = """Ты отвечаешь только на основе приведённого ниже контекста.
Если в контексте нет ответа на вопрос — напиши
«Не знаю» или «В контексте нет информации».
В конце ответа обязательно укажи источник: номер фрагмента из контекста
в формате [Источник: чанк N]."""

USER_PROMPT_TEMPLATE = """Контекст:
{context}

Вопрос: {question}

Ответ (с указанием источника в конце):"""


def build_prompt(context: str, question: str) -> str:
    """Формирует пользовательский промпт с контекстом и вопросом."""
    return USER_PROMPT_TEMPLATE.format(
        context=context.strip(),
        question=question.strip()
    )


async def get_answer_with_citation(
    chunks: list[dict],
    question: str,
) -> tuple[str, str | None]:
    """
    Отправляет контекст и вопрос в ChatGPT, возвращает ответ и источник (цитату).

    :param chunks: список чанков с ключами text, chunk_id
    :param question: вопрос пользователя
    :param max_retries: число повторов при 429
    :return: (текст ответа, источник — например "чанк 1" или None)
    """

    context_parts = []
    for c in chunks:
        cid = c.get("chunk_id", "?")
        context_parts.append(f"[Чанк {cid}]\n{c.get('text', '')}")
    context = "\n\n".join(context_parts)

    user_content = build_prompt(context, question)
    llm_client = await get_llm_client()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
    ]

    content = await llm_client.ask(messages)
    source = None
    if "[Источник:" in content or "чанк" in content.lower():
        for c in chunks:
            cid = c.get("chunk_id")
            if cid and f"чанк {cid}" in content.lower():
                source = f"Чанк {cid}"
                break
    return content, source
