from utils.llm import ask_llm
from prompts.planner_prompt import PLANNER_PROMPT

def planner_agent(state):
    question = state["question"]

    prompt = f"""
{PLANNER_PROMPT}

Question:
{question}
"""

    tool = ask_llm(prompt).strip().lower()

    if tool not in ["research", "calculator", "datetime"]:
        tool = "research"

    print("Planner selected:", tool)

    return {
        **state,
        "tool": tool
    }