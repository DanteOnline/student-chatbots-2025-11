"""
Поиск по ключевым словам среди чанков.
Запрос пользователя нормализуется (нижний регистр, разбиение на слова),
подсчитываются совпадения с текстом чанка, возвращаются top-N чанков.
"""
import re


def normalize_query(query: str) -> list[str]:
    """
    Нормализация запроса: нижний регистр, разбиение на слова (без пунктуации).

    :param query: строка запроса от пользователя
    :return: список слов для поиска
    """
    if not query or not query.strip():
        return []
    text = query.lower().strip()
    words = re.findall(r"[а-яёa-z0-9]+", text, re.IGNORECASE)
    return [w for w in words if len(w) > 1]


def score_chunk(chunk_text: str, words: list[str]) -> int:
    """
    Подсчёт совпадений: сколько слов из запроса встречается в чанке.

    :param chunk_text: текст чанка (нормализованный к нижнему регистру)
    :param words: список слов запроса
    :return: количество совпадающих слов
    """
    if not words:
        return 0
    lower = chunk_text.lower()
    return sum(1 for w in words if w in lower)


def search_chunks(
    chunks: list[dict],
    query: str,
    top_n: int = 5,
) -> list[dict]:
    """
    Поиск наиболее релевантных чанков по ключевым словам.

    :param chunks: список чанков с ключом "text" (и опционально "chunk_id")
    :param query: запрос пользователя
    :param top_n: сколько чанков вернуть
    :return: список чанков с добавленным полем "score", отсортированный по score
    """
    words = normalize_query(query)
    if not words:
        return []

    scored: list[dict] = []
    for ch in chunks:
        text = ch.get("text", "")
        score = score_chunk(text, words)
        if score > 0:
            scored.append({**ch, "score": score})

    scored.sort(key=lambda x: x["score"], reverse=True)

    result = scored[:top_n]

    print('START')
    for item in result:
        print(item['text'])
        print(item['score'])
        print(item['chunk_id'])
        print(len(item['text']))

    print('END')

    return scored[:top_n]
