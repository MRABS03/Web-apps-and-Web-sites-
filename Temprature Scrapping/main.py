import requests, selectorlib
from datetime import datetime as dt
import time
import sqlite3

connection = sqlite3.connect("temp.db")
cursor = connection.cursor()

URL = "https://programmer100.pythonanywhere.com/"


def request_web(url):
    data = requests.get(url)
    data = data.text
    return data


def scrap_web(data):
    extracted = selectorlib.Extractor.from_yaml_file("extractor.yaml")
    value = extracted.extract(data)["temp"]
    return value


def write(timestamp, entry):
    with open("Temperature.txt", "a") as file:
        file.write(fr"{timestamp} - {entry}" + "\n")


def write_sql_data(data):
    cursor.execute("INSERT INTO temp VALUES(?,?)", data)
    connection.commit()


def read_sql_data():
    cursor.execute("SELECT * FROM temp")
    data = cursor.fetchall()
    return data


while True:
    current_time = dt.now()
    current_timestamp = current_time.strftime("%H:%M:%S")
    eb_data = request_web(URL)
    temp = scrap_web(eb_data)
    print(fr"Data from Web: {current_timestamp} - {temp}")
    write(current_timestamp, temp)
    temp_tuple = (current_timestamp, temp)
    write_sql_data(temp_tuple)

    data_from_sql = read_sql_data()
    print(f"Data from SQL: {data_from_sql}")
    time.sleep(3)
