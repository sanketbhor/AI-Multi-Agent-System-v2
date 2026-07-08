from utils.llm import ask_llm
from prompts.critic_prompt import CRITIC_PROMPT

def critic_agent(state):

    prompt = f"""
{CRITIC_PROMPT}

Question:
{state["question"]}

Research Result:
{state["tool_result"]}
"""

    result = ask_llm(prompt).strip().upper()

    if result not in ["GOOD", "BAD"]:
        result = "GOOD"

    return {
        "critic_checker_result": result
    }