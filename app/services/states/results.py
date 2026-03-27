from .trace import append_trace


def finalize(state: dict) -> dict:
    """
    Возврат итогового (success) state
    """
    return {
        **state,
        "trace": append_trace(state, "finalize"),
    }


def handle_error(state: dict) -> dict:
    """
    Возврат state, когда была ошибка
    """
    answer = state['error']
    return {
        **state,
        "answer": answer,
        "trace": append_trace(state, "handle_error"),
    }
