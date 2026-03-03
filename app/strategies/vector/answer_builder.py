"""Сборка ответа по контексту через LLM с цитатой."""
from __future__ import annotations

from app.llm_client import get_llm_client

SYSTEM_PROMPT = """Ты отвечаешь только на основе приведённого контекста.
Если в контексте нет ответа — напиши «Не знаю»."""

TEMPLATE = "Контекст:\n{context}\n\nВопрос: {question}\n\nОтвет:"


async def get_answer_with_citation(
        chunks: list[dict],
        question: str, max_retries: int = 3
) -> tuple[str, str | None, str]:
    """Возвращает (ответ, источник — имя файла, текст чанка для вывода внизу)."""

    context = "\n\n".join(
        f"[Чанк {c.get('chunk_id', '?')}]\n{c.get('text', '')}" for c in chunks
    )
    user_content = TEMPLATE.format(context=context, question=question)

    llm_client = await get_llm_client()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
    ]

    content = await llm_client.ask(
        messages
    )

    source = None
    cited_chunk = None
    for c in chunks:
        cid = c.get("chunk_id")
        if cid and f"чанк {cid}" in content.lower():
            source = c.get("source") or f"Чанк {cid}"
            cited_chunk = c
            break
    if source is None and chunks:
        first = chunks[0]
        source = first.get("source") or f"Чанк {first.get('chunk_id', '?')}"
        cited_chunk = first
    chunk_text = (cited_chunk.get("text", "") if cited_chunk else "").strip()
    return content, source, chunk_text
