import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
URL = "https://api.nasa.gov/planetary/apod"
NASA_API_KEY = os.environ.get("NASA_API_KEY")

nasa_params = {
    "api_key": NASA_API_KEY,
    "thumbs": False
}

response = requests.get(URL, params=nasa_params)

import streamlit as st
explanation = response.json()['explanation']
title = response.json()['title']
image_url = response.json()['url']

image_filepath = 'img.jpg'
img_response = requests.get(image_url)
with open("img.jpg", "wb") as file:
    file.write(img_response.content)
st.markdown(f"# {title}")
st.write("\n")
st.image(image_filepath)
st.write("\n")
st.write(explanation)