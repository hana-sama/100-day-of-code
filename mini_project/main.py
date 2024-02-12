import pandas as pd
import streamlit as st


# Import CSV data
df = pd.read_csv('happy.csv')

# sorted_df = df.sort_values(by="corruption", ascending=False)
# for index, row in sorted_df.iterrows():
#     print(row['country'], row['corruption'])
# Exolore data
print(df.head())

st.markdown("""
# In Search for Happiness
""")
st.text("")         
st.image("happiness.jpg")
st.text("")

option_x = st.selectbox(label="Select the data for the X-axis:", options=('GDP', 'Happiness', 'Generosity', 'Corruption', 'Life Expectancy', 'Freedom to Make Life Choices', 'Social Support'), key="option_x")
option_y = st.selectbox(label="Select the data for the X-axis:", options=('GDP', 'Happiness', 'Generosity', 'Corruption', 'Life Expectancy', 'Freedom to Make Life Choices', 'Social_support'), key="option_y")


st.markdown(f"## {option_x} and {option_y}")

# Create scatter chart based on selected items
import plotly.express as px

match option_x:
    case "GDP":
        x_array = df['gdp']
    case "Happiness":
        x_array = df['happiness']
    case "Corruption":
        x_array = df['corruption']
    case "Generosity":
        x_array = df['generosity']
    case " Life Expectancy":
        x_array = df['life_expectancy']
    case "Social Support":
        x_array = df['social_support']
    case "Freedom to Make Life Choices":
        x_array = df['freedom_to_make_life_choices']

match option_y:
    case "GDP":
        y_array = df['gdp']
    case "Happiness":
        y_array = df['happiness']
    case "Corruption":
        y_array = df['corruption']
    case "Generosity":
        y_array = df['generosity']
    case " Life Expectancy":
        y_array = df['life_expectancy']
    case "Social Support":
        y_array = df['social_support']
    case "Freedom to Make Life Choices":
        y_array = df['freedom_to_make_life_choices']

figure = px.scatter(x=x_array, y=y_array, labels={"x": option_x, "y": option_y})
st.plotly_chart(figure)