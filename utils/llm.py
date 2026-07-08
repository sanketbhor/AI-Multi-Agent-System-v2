from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL")
)

MODEL = os.getenv("LLM_MODEL")


def ask_llm(prompt):
    response = client.chat.completions.create(
        model = MODEL ,
        messages=[
            {
            "role":"user",
            "content":prompt
            }
        ]
    )

    return response.choices[0].message.content
