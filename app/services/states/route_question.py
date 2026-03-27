from .fixed_answers import FIXED_ANSWERS_DICT
from .trace import append_trace


def after_route(state):
    print('AFTER ROUTE')
    print(state['route'])
    return state['route']


def route_question(state: dict) -> dict:
    """
    Определение куда идти дальше
    """
    question: str = state['question']

    keywords = list(FIXED_ANSWERS_DICT.keys())

    keyword = None
    is_keyword_in_question = False

    for keyword in keywords:
        if keyword.lower() in question.lower():
            is_keyword_in_question = True
            keyword = keyword
            break

    route = "fixed_answers" if is_keyword_in_question else "answer_directly"
    return {
        **state,
        "route": route,  # записываем выбранный маршрут.
        "keyword": keyword,  # записываем ключевое слово
        "trace": append_trace(state, f"route_question -> {route}")
    }
