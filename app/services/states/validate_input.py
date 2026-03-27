from .trace import append_trace


def is_too_short(question: str) -> bool:
    """
    Вопрос слишком короткий?
    """
    min_length = 5
    return len(question) < min_length


def is_too_long(question: str) -> bool:
    """
    Вопрос слишком длинный?
    """
    max_length = 500
    return len(question) > max_length


def validate_input(state: dict) -> dict:
    """
    Проверка воода пользователя
    """
    question = state["question"].strip()
    if not question:
        return {
            **state,
            "route": "error",
            "error": "Пустой вопрос - Пустой ответ!",
            "trace": append_trace(state, "validate_input -> error"),
        }
    if is_too_short(question):
        return {
            **state,
            "route": "error",
            "error": "Слишком короткий вопрос. Попробуй придумать что то поумнее.",
            "trace": append_trace(state, "validate_input -> error"),
        }
    if is_too_long(question):
        return {
            **state,
            "route": "error",
            "error": "Слишком серьёзная проблема. Я такое не потяну.",
            "trace": append_trace(state, "validate_input -> error"),
        }
    return {
        **state,
        "question": question,
        "trace": append_trace(state, "validate_input -> ok"),
    }


def after_validate(state: dict) -> str:
    return "handle_error" if state["route"] == "error" else "route_question"
