from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.5)

def refine_prompts(segments):
    refined_prompts = []

    template = PromptTemplate.from_template(
        """You are a visual storyteller generating image prompts for an AI art model. 

Your goal is to create historically accurate, culturally appropriate, and child-friendly prompts based on the provided text.

Rules:
- Maintain historical accuracy (e.g., real clothing, setting, time period).
- Avoid fantasy/cartoon distortions.
- Describe key characters based on cultural/historical context.
- Make the prompt visually detailed but grounded in realism.

Text: {text}

Image Prompt:"""
    )

    chain = template | llm

    for seg in segments:
        result = chain.invoke({"text": seg})
        refined_prompts.append(result.content.strip())

    return refined_prompts
