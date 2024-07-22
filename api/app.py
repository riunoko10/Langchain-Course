from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_ollama.llms import OllamaLLM
import uvicorn



import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")



app = FastAPI(
    title="LangChain API",
    version="0.1.0",
    description="API for LangChain",
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
    )

model = ChatOpenAI()

### ollama LLama2
llm = OllamaLLM(model="llama2")
prompt1 = ChatPromptTemplate.from_template("escribe un ensayo sobre {tema} de 100 palabras")
prompt2 = ChatPromptTemplate.from_template("escribe un poema sobre {tema} de 100 palabras en español")


add_routes(
    app,
    prompt1 | model,
    path="/ensayo",
    )


add_routes(
    app,
    prompt2 | llm,
    path="/poema",
    )

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
