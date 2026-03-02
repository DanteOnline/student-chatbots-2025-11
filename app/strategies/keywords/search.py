"""
Демо RAG-лайт: один документ (из файла или строка) -> чанки в памяти ->
по запросу поиск по ключевым словам -> сборка ответа через ChatGPT с цитатой.
"""
from .answer_builder import get_answer_with_citation
from .chunking import chunk_file
from .keyword_search import search_chunks


async def run_askdoc(question: str, doc_source: str) -> str:
    """
    Загружает документ в чанки, в цикле принимает вопросы и выводит ответ с цитатой.

    :param doc_source: путь к файлу или сам текст документа
    :param is_path: True если doc_source — путь к файлу
    """

    chunks = chunk_file(doc_source)

    if not chunks:
        return 'В базе нет документов'

    found = search_chunks(chunks, question, top_n=5)
    answer, source = await get_answer_with_citation(found, question)
    return f'{answer} {source}'


async def keywords_strategy(question):
    return await run_askdoc(question, './docs/2_Garri_Potter_i_Taynaya_komnata.txt')
    # return await run_askdoc(question, './docs/1_Filosofskiy_kamen.txt')
    return run_askdoc(question, '../docs/1_Filosofskiy_kamen.txt')
