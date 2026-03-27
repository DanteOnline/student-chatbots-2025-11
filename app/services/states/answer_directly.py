from app.models import llm_client

from .trace import append_trace


async def answer_directly(state):
    text = state['question']

    # Ошибку не обрабатываем, потому что она обработана в ask методе
    answer = await llm_client.ask(text)

    return {
        **state,
        "answer": answer,
        "trace": append_trace(state, "answer_directly -> ok"),
    }
