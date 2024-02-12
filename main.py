import streamlit as st
import plotly.express as px
from backend import get_data

st.markdown("""
# Weather Forecast for the Next Days
""")
st.text("")         
st.image("./images/weather.jpg")
st.text("")
place = st.text_input("Location:", value="Tirana")
st.text("")
days = st.slider(label="Forecast Days", min_value=1, max_value=5)
option = st.selectbox(label="Select data to view:", options=('Temperature', 'Sky'))
st.markdown(f"## {option} for the next {days} days in {place}")


if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temepature in (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {"Clear": "./images/clear.png", "Clouds": "./images/cloud.png", "Rain": "./images/rain.png", "Snow": "./images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)

    except KeyError as e:
        st.write(f"{place} does not exist!")