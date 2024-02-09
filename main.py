import streamlit as st



st.markdown("""
# Weather Forecast for the Next Days
""")
st.text("")         
st.image("weather.jpg")
st.text("")
place = st.text_input("Location:")
st.text("")
days = st.slider(label="Forecast Days", min_value=1, max_value=5)
option = st.selectbox(label="Select data to view:", options=('Temperature', 'sky'))
st.markdown(f"## {option} for the next {days} days in {place}")