import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import base64
st.set_page_config(layout="wide")

LOGO_IMAGE = 'images/logo.png'

st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #f9a01b !important;
        padding-top: 75px !important;
        padding-left: 75px
    }
    .logo-img {
        float:right;
    }
    .message {
        font-weight: 100;
        font-size: 25px;
        color: #FBF9F1;
        padding-top: 75px;
        text-alight: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">Access Best Insight ?</p>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <div class="container">
         <p class="message"> We are a team of passionate individuals who believe in the power of technology to change the world. Our mission is to create innovative products that make people’s lives easier and more fulfilling. We strive to build a culture of inclusivity and diversity, where everyone feels valued and respected. Our goal is to create a positive impact on society and the environment, and we are committed to making a difference in the world. </p>
    </div>
    """,
    unsafe_allow_html=True)

df_topic = pd.read_csv("topics.csv")
# 1. as sidebar menu
icons_list = ['person-gear', 'folder-x', 'option']
with st.sidebar:
    selected = option_menu('Main Menu', ['Home', 'Our Team', df_topic["topic"][0], df_topic["topic"][1], df_topic["topic"][2]], 
                           icons=['house', 'people-fill', icons_list[0], icons_list[1], icons_list[2]], menu_icon="cast", default_index=1)
    selected




