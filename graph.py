from langgraph.graph import StateGraph, END

from state import AgentState

from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.calculator import calculator_agent
from agents.datetime import datetime_agent
from agents.critic import critic_agent
from agents.answer import answer_agent

builder = StateGraph(AgentState)

builder.add_node("Planner", planner_agent)
builder.add_node("Research", research_agent)
builder.add_node("Calculator", calculator_agent)
builder.add_node("Datetime", datetime_agent)
builder.add_node("Critic", critic_agent)
builder.add_node("Answer", answer_agent)

builder.set_entry_point("Planner")

def planner_route(state):

    print(state)

    if state["tool"] == "calculator":
        return "Calculator"

    elif state["tool"] == "datetime":
        return "Datetime"

    return "Research"

def critic_route(state):

    if state["critic_checker_result"] == "BAD":
        return "Research"

    return "Answer"

builder.add_conditional_edges(
    "Planner",
    planner_route,
    {
        "Research": "Research",
        "Calculator": "Calculator",
        "Datetime": "Datetime",
    },
)

builder.add_edge("Research", "Critic")
builder.add_edge("Calculator", "Critic")
builder.add_edge("Datetime", "Critic")

builder.add_conditional_edges(
    "Critic",
    critic_route,
    {
        "Research": "Research",
        "Answer": "Answer"
    }
)

builder.add_edge("Answer", END)

graph = builder.compile()