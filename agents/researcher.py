from utils.tools import search_web

def research_agent(state):

    result= search_web(
            state["question"]
    )

    return {
        "tool_result": result
    }