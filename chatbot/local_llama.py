import os

import streamlit as st
from dotenv import load_dotenv
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Eres un asistente virtual que ayuda a los usuarios a encontrar información sobre desarrollo de software.",
        ),
        ("user", "Pregunta: {pregunta}"),
    ]
)

## streamlit framework
st.title("Chatbot de desarrollo de software")
input_text = st.text_input("Pregunta")


## Ollama LLM

llm = OllamaLLM(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"pregunta": input_text}))