from . import (
    # dummy,
    llm_direct,
)


async def search(question, strategy):
    return await strategy(question)


async def get_strategy():
    # return dummy.always_down_know
    return llm_direct.ask_llm
