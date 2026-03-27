from typing import Any

from langgraph.graph import (
    END,
    START,
    StateGraph,
)
from langgraph.graph.state import CompiledStateGraph

from .answer_directly import answer_directly
from .fixed_answers import fixed_answers
from .results import finalize, handle_error
from .route_question import after_route, route_question
from .trace import save_trace
from .validate_input import after_validate, validate_input


def build_graph() -> CompiledStateGraph[Any, Any, Any, Any]:
    """
    Строим Граф для маршрутов
    :return:
    """
    graph = StateGraph(dict)
    graph.add_node("validate_input", validate_input)
    graph.add_node("answer_directly", answer_directly)
    graph.add_node("fixed_answers", fixed_answers)
    graph.add_node("route_question", route_question)
    graph.add_node("handle_error", handle_error)
    graph.add_node("finalize", finalize)

    graph.add_edge(START, "validate_input")

    graph.add_conditional_edges("validate_input", after_validate)
    graph.add_conditional_edges("route_question", after_route)

    graph.add_edge("answer_directly", "finalize")
    graph.add_edge("fixed_answers", "finalize")
    graph.add_edge("handle_error", END)
    graph.add_edge("finalize", END)

    return graph.compile()


compiled_graph = build_graph()


async def get_initial_state(question: str) -> dict:
    initial_state = {
        "question": question,
        "route": None,
        "answer": "",
        "error": "",
        "trace": [],
    }
    return initial_state


async def ask(question: str) -> str:
    state = await get_initial_state(question)
    result = await compiled_graph.ainvoke(state)
    save_trace(result)
    answer = result['answer']
    return answer
