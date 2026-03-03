from .answer_builder import get_answer_with_citation
from .vector_search import search


async def vector_strategy(question):
    chunks, no_answer = search(question, top_k=5)
    print(f"[RAG] Поиск: no_answer={no_answer}, найдено чанков={len(chunks)}")
    for i, c in enumerate(chunks):
        score = c.get("score")
        score_str = f"{score:.3f}" if isinstance(score, (int, float)) else str(score)
        src = c.get("source", "—")
        text_preview = (c.get("text", "") or "")[:60].replace("\n", " ")
        print(f"  [{i + 1}] score={score_str} source={src} | {text_preview}...")
    if no_answer or not chunks:
        return 'Не знаю'
    answer, source, _chunk_text = await get_answer_with_citation(chunks, question)
    print(f"[RAG] Источник: {source!r}")
    text = answer
    answer_lower = (answer or "").strip().lower()
    if source and not answer_lower.startswith("не знаю"):
        text += f"\n\n📎 Источник: {source}"
    return text
