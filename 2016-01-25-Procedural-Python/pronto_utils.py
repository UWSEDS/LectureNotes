"""pronto_utils.py"""

import wget
import os
import zipfile
import pandas as pd

import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # for plot stylings


def download_if_needed(URL, filename):
    """
    Download from URL to filename unless filename already exists
    """
    if os.path.exists(filename):
        print(filename, 'already exists')
        return
    else:
        print('downloading', filename)
        wget.download(URL)


def get_pronto_data():
    """
    Download pronto data, unless already downloaded
    """
    download_if_needed('https://s3.amazonaws.com/pronto-data/open_data_year_one.zip',
                       'open_data_year_one.zip')


def get_trip_data():
    """
    Fetch pronto data (if needed) and extract trips as dataframe
    """
    get_pronto_data()
    zf = zipfile.ZipFile('open_data_year_one.zip')
    file_handle = zf.open('2015_trip_data.csv')
    return pd.read_csv(file_handle)


def get_weather_data():
    """
    Fetch pronto data (if needed) and extract weather as dataframe
    """
    get_pronto_data()
    zf = zipfile.ZipFile('open_data_year_one.zip')
    file_handle = zf.open('2015_weather_data.csv')
    return pd.read_csv(file_handle)


def get_trips_and_weather():
    trips = get_trip_data()
    weather = get_weather_data()

    # This is a nice way to access date info in a column
    date = pd.DatetimeIndex(trips['starttime'])

    # pivot table = two-dimensional groupby
    trips_by_date = trips.pivot_table('trip_id', aggfunc='count',
                                      index=date.date, columns='usertype')

    weather = weather.set_index('Date')
    weather.index = pd.DatetimeIndex(weather.index)
    weather = weather.iloc[:-1]
    return weather.join(trips_by_date)


def plot_daily_totals():
    data = get_trips_and_weather()
    fig, ax = plt.subplots(2, figsize=(14, 6), sharex=True)
    data['Annual Member'].plot(ax=ax[0], title='Annual Member')
    data['Short-Term Pass Holder'].plot(ax=ax[1], title='Short-Term Pass Holder')
    fig.savefig('daily_totals.png')
