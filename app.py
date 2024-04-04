from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('google_gemini_api'))

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="QnA Demo", page_icon="🔮")
st.header("Gemini LLM Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Submit")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)

