import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
st.title("Home")
col1, col2, = st.columns(2)

with col1:
    st.image("images/my_photo_2.jpg")

with col2:
    st.title("Angela Yu")
    content = """
    Hi, I am journalist and communication consultant, focussing on solving problems and challenges that small- and medium-sized enterprises and start-ups face in the VUCA era. I graduated in 2013 with a Master of Commerce from Waseda University in Japan with a focus on global geopolitics and its impact on global trade, economy and politics. I have worked with various media firms such as Agence France Press, Reuters, and Bloomberg to cover business and financial journalism.
    """
    st.info(content)
content2 = "Below you can find some of the apps I have built in Python. Feel free to contact me!"
st.info(content2)

df = pd.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df.iterrows():
        if (index + 1) % 2 != 0:
            st.header(row["title"])
            st.write(row["description"])
            st.write(f'[Source Code]({row["url"]})')
            st.image(f"images/{row['image']}")

with col4:
    for index, row in df.iterrows():
        if (index + 1 ) % 2 == 0:
            st.header(row["title"])
            st.write(row["description"])
            st.write(f'[Source Code]({row["url"]})')
            st.image(f"images/{row['image']}")
