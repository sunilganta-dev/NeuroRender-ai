# agents/prompt_refiner.py

import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# Load OpenAI API Key from .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create LangChain chat model instance (use GPT-4 or GPT-3.5)
llm = ChatOpenAI(model_name="gpt-4", temperature=0.7, openai_api_key=OPENAI_API_KEY)

def refine_prompt(prompt: str) -> str:
    """
    Uses GPT-4 to refine and expand a user prompt for image generation.
    """
    message = HumanMessage(content=f"Improve the following prompt to generate a high-quality AI image. Include style, lighting, and detail: \"{prompt}\"")

    try:
        response = llm([message])
        return response.content.strip()
    except Exception as e:
        print("Error refining prompt:", e)
        return prompt
