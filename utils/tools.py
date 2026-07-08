from ddgs import DDGS
import numexpr
from datetime import datetime

def search_web(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query,max_results=3))

        if not results:
            return " No Result Found. "
        
        output =""

        for result in results:
            output+=f"Title: {result['title']}\n"
            output+=f"Snippet: {result['body']}\n\n"

        return output
    
    except Exception as e:
        return f"Search Error: {e}"

def calculator(expression):
    try:
        result = numexpr.evaluate(expression)
        return str(result.item())
    except Exception:
        return "Invalid Expression"
    
def get_datetime():
    return datetime.now().strftime(
        "%d%m%Y %H%M%S"
    )