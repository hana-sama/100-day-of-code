import streamlit as st
import pandas as pd
st.write("# Our Team")
df = pd.read_csv("data.csv", sep=",")
df_topic = pd.read_csv("topics.csv")


col1, col2, col3 = st.columns(3)

import time
from PIL import Image
with col1:
    for index, row in df[0:4].iterrows():
        st.write(f'## {row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image(f"images/{row['image']}")
with col2:
    for index, row in df[4:8].iterrows():
        st.write(f'## {row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image(f"images/{row['image']}")
with col3:
    for index, row in df[8:].iterrows():
        st.write(f'## {row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image(f"images/{row['image']}")


with st.form("Contact Us", clear_on_submit=True):
    name = st.text_input("Your name: ")
    email = st.text_input("Your Email Address: ")
    topic = st.selectbox("What topic do you want to discuss? ",
                         (df_topic['topic']))
    free_text = st.text_input("Text:")
    submitted = st.form_submit_button("Send")

if submitted:
    if name != "" and email != "" and free_text != "":
        with st.spinner("Checking our staff who can best serve your needs..."):
            time.sleep(3)
            my_image = Image.open("images/me.jpg")
            message = st.subheader(f"Hello {name.capitalize()}, I am Angela Yu, expert on {topic}. May I help You?")
            my_photo = st.image(my_image)
            time.sleep(10)
            message.empty()
            my_photo.empty()
    else:
        st.warning("Please fill in all of the required fields above!")