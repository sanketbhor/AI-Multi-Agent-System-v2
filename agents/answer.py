from utils.llm import ask_llm
from prompts.answer_prompt import ANSWER_PROMPT

def answer_agent(state):    

    prompt=f"""

{ANSWER_PROMPT}

Question:
{state["question"]}

Tool Output:
{state["tool_result"]}

Critic Checker:
{state["critic_checker_result"]}

"""

    answer = ask_llm(prompt)

    return{
        "final_answer": answer
    }