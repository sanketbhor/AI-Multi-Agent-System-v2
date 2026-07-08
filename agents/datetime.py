from utils.tools import get_datetime

def datetime_agent(state):

    result = get_datetime()

    return {
        "tool_result": result
    }