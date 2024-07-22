import requests
import streamlit as st



def get_openai_response(input_text):
    response = requests.post(
        "http://localhost:8000/ensayo/invoke",
        json={"input": {"tema": input_text}},
    )
    return response.json()['output']['content']


def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poema/invoke",
        json={"input": {"tema": input_text}},
    )
    respuesta = response.json()['output']
    return respuesta



st.title("LangChain API")
input_text = st.text_input("Escribir un ensayo")
input_text2 = st.text_input("Escribir un poema")


if input_text:
    response = get_openai_response(input_text)
    st.write(response)

if input_text2:
    response = get_ollama_response(input_text2)
    st.write(response)
