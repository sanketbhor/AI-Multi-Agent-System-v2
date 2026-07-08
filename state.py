from typing import TypedDict

class AgentState(TypedDict):

    question: str

    tool: str

    tool_result: str

    critic_checker_result: str

    final_answer: str