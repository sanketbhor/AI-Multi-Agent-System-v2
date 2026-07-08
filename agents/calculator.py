from utils.tools import calculator

def calculator_agent(state):

    result = calculator(state["question"])

    return {
        "tool_result": result
    }