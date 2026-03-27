from .trace import append_trace


def finalize(state):
    return {
        **state,
        "trace": append_trace(state, "finalize"),
    }


def handle_error(state):
    answer = state['error']
    return {
        **state,
        "answer": answer,
        "trace": append_trace(state, "handle_error"),
    }
