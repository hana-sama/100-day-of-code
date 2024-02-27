import requests
import selectorlib
import pandas as pd
import sqlite3
import datetime
import time
import signal
from emailing import send_message
URL = "http://programmer100.pythonanywhere.com/tours/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def convert_date(input_date):
    # Split the input date into day, month, and year
    day, month, year = input_date.split('.')

    # Map month abbreviations to numeric values
    # Create a datetime object
    formatted_date = datetime.datetime(int(year), int(month), int(day))

    # Format the datetime as YYYY-MM-DD
    formatted_string = formatted_date.strftime('%Y-%m-%d')
    return formatted_string


def scrape_webpage(url):
    # Scrape the page source from the URL
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extrace_data(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value

def db_connect(db_path: str) -> sqlite3.Connection:
    connection = sqlite3.connect(db_path)
    return connection
    
local_db_path = './sqlite/sqlite_database.db'
connection = db_connect(local_db_path)

def store_data(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    date = convert_date(date)
    db_cursor = connection.cursor()
    event = (band, city, date)
    sql = """INSERT INTO events(band, city, date)VALUES(?,?,?)"""
    db_cursor.execute(sql, event)
    connection.commit()
    
def read_data(extracted):
    row = extracted.split(",") 
    row = [item.strip() for item in row]
    band, city, date = row
    db_cursor = connection.cursor()
    db_cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = db_cursor.fetchall()
    print(rows)
    return rows

def get_data_in_dataframe():
    df = pd.read_csv('data.txt', sep=",", header=None, names=['band', 'city', 'date'])
    return df


# def db_connect(db_path: str) -> sqlite3.Connection:
#     path_to_db = pathlib.Path(db_path).absolute().as_uri()
#     print(path_to_db)
#     connection = None
#     try:
#         connection = sqlite3.connect(f'{path_to_db}?mode=rw', uri=True)
#     except:
#         print(f'Error, trying to open database. Please check that file exists: {path_to_db}')
#         os.sys.exit(1)
#     return connection

interrupted = False
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    while True:
        scraped = scrape_webpage(URL)
        extracted = extrace_data(scraped)
        if extracted != "No upcoming tours":
            row = read_data(extracted)
            if not row:
                store_data(extracted)
                send_message(message=f"Hey, new event was found! Check out the following.\n{extracted}")
        time.sleep(2)
        if interrupted:
            print("Gotta go")
            break