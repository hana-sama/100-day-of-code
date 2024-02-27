import requests
import selectorlib
from emailing import send_message
from datetime import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
import signal
URL = "http://programmer100.pythonanywhere.com/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# header = "date, temp"
# with open('temp_data.txt', 'w') as file:
#     file.write(f'{header}\n')
#temperatureId > b
def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def db_connect(db_path: str) -> sqlite3.Connection:
    connection = sqlite3.connect(db_path)
    return connection
    
local_db_path = './sqlite/database.db'
connection = db_connect(local_db_path)
def scrape_webpage(url):
    # Scrape the page source from the URL
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract_data(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['temp']
    return value

def store_data(extracted):
    date = datetime.now()
    date = date.strftime("%y-%m-%d-%H-%M-%S")
    db_cursor = connection.cursor()
    event = (date, extracted)
    sql = """INSERT INTO temp_data(date, temp)VALUES(?,?)"""
    db_cursor.execute(sql, event)
    connection.commit()
    

def read_data():
    db_cursor = connection.cursor()
    query = db_cursor.execute("SELECT * FROM temp_data")
    cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    return results


def create_chart():
    result = read_data()
    chart_data = {
        'x': result['date'],
        'y': result['temp']
    }
    figure = px.line(x=chart_data['x'], y=chart_data['y'], labels={"x": "date", "y": "temperature in ℃"})
    st.plotly_chart(figure)

# interrupted = False
# signal.signal(signal.SIGINT, signal_handler)
 
if __name__ == "__main__":

    scraped = scrape_webpage(URL)
    extracted = extract_data(scraped)
    print(extracted)
    store_data(extracted)
    create_chart()
    send_message(message=f"Today, the average temperature across the globe is {extracted}℃ right now")

