from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os                        

load_dotenv()
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.5)

def refine_prompts(segments):    
    refined_prompts = []  

    template = PromptTemplate.from_template(
        "You are a visual storyteller. Convert this text into a clear, vivid, kid-friendly image prompt. Keep it simple and happy.\n\nText: {text}"
    )
    chain = template | llm  

    for seg in segments:
        result = chain.invoke({"text": seg})  
        refined_prompts.append(result.content.strip())

    return refined_prompts
