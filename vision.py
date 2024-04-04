from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('google_gemini_api'))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input,image])
        return response.text
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo", page_icon="🔮")
st.header("Gemini LLM Application")

input = st.text_input("Input: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"], key="image")
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Submit")

if submit:
    response = get_gemini_response(input, image)
    st.header("The Response is:")
    st.write(response)