import requests
import selectorlib
from sending_email import send_email
import sqlite3

connection = sqlite3.connect("events.db")
cursor = connection.cursor()

URL = "https://programmer100.pythonanywhere.com/tours/"


def scrape_data(url):
    """We're scrapping data from web"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extractor.yaml")
    value = extractor.extract(source)["tours"]
    return value


def write(event):
    with open("tours.txt", "a") as file:
        file.write(event + "\n")


def read():
    with open("tours.txt", "r") as file:
        data = file.read()
        return data


def get_sql_data():
    cursor.execute("SELECT * FROM events")
    Data = cursor.fetchall()
    return Data


def write_sql_data(data):
    cursor.execute("INSERT INTO events VALUES(?,?,?)", data)
    connection.commit()


if __name__ == "__main__":
    scraped = scrape_data(URL)
    extracted = extract(scraped)
    ex = extracted.split(",")
    tours = get_sql_data()
    tours = [item[0] for item in tours]

    if extracted != 'No upcoming tours' and ex[0] not in tours:
        extracted_tup = tuple(ex)
        write_sql_data(extracted_tup)
        print(extracted)
