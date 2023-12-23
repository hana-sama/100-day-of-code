import streamlit as st
from PIL import Image
import os

st.title("Image Uploader")
file_path = st.file_uploader("", type=["png", "jpg", "jpeg"])
if file_path:
    img = Image.open(file_path)
    gray_img = img.convert("L")
    st.image(gray_img, caption="my_photo", use_column_width=True)
