from langchain_openai import ChatOpenAI 
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7)

def extract_segments(blog_text):
    prompt = ChatPromptTemplate.from_template(
        "You are an assistant. Given a blog post, extract 3–4 key visual moments that can be illustrated. Respond in bullet points.\n\nBlog:\n{blog_text}"
    )
    chain = prompt | llm
    response = chain.invoke({"blog_text": blog_text[:3000]})  
    return response.content.strip().split("\n")
