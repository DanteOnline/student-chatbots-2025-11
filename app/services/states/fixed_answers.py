from .trace import append_trace

FIXED_ANSWERS_DICT = {
    'Деньги': "Чтобы заработать денег, учись в OTUS",
    'Политика': "Оно тебе надо?",
    'Религия': "Извини - религия, это дело каждого"
}


async def fixed_answers(state: dict) -> dict:
    """
    Получаем фиксированные ответы в формате json
    """
    keyword = state['keyword']
    answer = FIXED_ANSWERS_DICT[keyword]

    return {
        **state,
        "answer": answer,
        "trace": append_trace(state, "fixed_answers -> ok"),
    }
