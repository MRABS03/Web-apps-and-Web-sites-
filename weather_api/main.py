from flask import Flask, render_template
import pandas as pd


app = Flask("Weather Report")
stations=pd.read_csv("stations/stations.txt",skiprows=17)

@app.route("/")
def home():
    return render_template('home.html',data=stations.to_html())


@app.route("/api/<station>/<date>")
def weather(station, date):
    df = pd.read_csv(fr"stations/TG_STAID{str(station).zfill(6)}.txt", skiprows=20, parse_dates=["    DATE"])
    formatted_date = pd.to_datetime(date, format="%Y%m%d").strftime("%Y-%m-%d")
    req_station = df.loc[df['    DATE'] == formatted_date]
    required_info = {
        'Station': station,
        'Date': formatted_date,
        'Temprature': float(req_station['   TG']) / 10
    }
    return required_info


app.run(debug=True, port=5001)
