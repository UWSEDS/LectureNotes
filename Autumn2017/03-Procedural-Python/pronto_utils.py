from urllib import request
import os
import pandas as pd


TRIP_DATA = "https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD"
TRIP_FILE = "pronto_trips.csv"

WEATHER_DATA = "http://uwseds.github.io/data/pronto_weather.csv"
WEATHER_FILE = "pronto_weather.csv"

def download_if_not_present(url, filename):
    """Download file from URL to filename
    If filename is present, then skip download.
    """
    if os.path.exists(filename):
        print("File already present")
    else:
        print("Downloading", filename)
        request.urlretrieve(url, filename)
        
def download_trips():
    """Download the pronto trip data unless already downloaded"""
    download_if_not_present(TRIP_DATA, TRIP_FILE)
    
def download_weather():
    download_if_not_present(WEATHER_DATA, WEATHER_FILE)
    
def load_weather_data():
    download_weather()
    return pd.read_csv('pronto_weather.csv',
                       parse_dates=['DATE'],
                       index_col='DATE')

def load_trip_data():
    download_trips()
    data = pd.read_csv('pronto_trips.csv')
    data['starttime'] = pd.to_datetime(data['starttime'], format="%m/%d/%Y %I:%M:%S %p")
    data['stoptime'] = pd.to_datetime(data['stoptime'], format="%m/%d/%Y %I:%M:%S %p")
    data['tripminutes'] = data['tripduration'] / 60
    return data


def join_trips_and_weather():
    """Group trips by day and join with the daily weather data
    Returns: pandas DataFrame
    """
    weather = load_weather_data()
    trips = load_trip_data()
    tripdates = pd.DatetimeIndex(trips['starttime']).date
    trips_by_day = pd.pivot_table(trips,
                                  values='trip_id',
                                  index=tripdates,
                                  columns='usertype',
                                  aggfunc='count')
    return trips_by_day.join(weather)