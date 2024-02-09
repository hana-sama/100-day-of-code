from flask import Flask, render_template
import pandas as pd
import glob
from dateutil.parser import parse
path = './data/'
all_files = glob.glob(path + '/*.txt')

app = Flask(__name__)

@app.route("/")
def index():
    stations = pd.read_csv('./data/stations.txt', skiprows=17)
    return render_template("index.html", data=stations)

@app.route("/api/v1/<station>/<date>")
def weather_data_api(station, date):
    filename = f'./data/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == f'{ parse(str(date))}']['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature
            }

@app.route('/api/v1/<station>')
def all_data(station):
    filename = f'./data/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result

@app.route('/api/v1/annual/<station>/<year>')
def yearly_data(station, year):
    filename = f'./data/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))]
    return result.to_dict(orient="records")
    
@app.route("/contact/")
def contact():
    data = pd.read_csv('./data/stations.txt', skiprows=17)
    return render_template("contact.html", data=data)

@app.route("/pricing/")
def pricing():
    data = pd.read_csv('./data/stations.txt', skiprows=17)
    return render_template("pricing.html", data=data)

@app.route("/features/")
def features():
    data = pd.read_csv('./data/stations.txt', skiprows=17)
    return render_template("features.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)


