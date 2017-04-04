import requests
import os
import zipfile
import pandas as pd
import matplotlib.pyplot as plt


URL = "https://s3.amazonaws.com/pronto-data/open_data_year_two.zip"


def download_if_needed(url, outfile):
    """
    Download data from url and save to outfile
    If outfile already exists, then do nothing
    """
    if os.path.exists(outfile):
        pass
    else:
        req = requests.get(url)
        assert req.status_code == 200
        with open(outfile, 'wb') as f:
            f.write(req.content)


def get_trip_data():
    download_if_needed(URL, 'pronto_data.zip')
    zf = zipfile.ZipFile('pronto_data.zip')
    return pd.read_csv(zf.open('2016_trip_data.csv'))


def plot_daily_rides():
    """Plot ride count vs time for members and day users"""
    plt.style.use('ggplot')

    data = get_trip_data()
    start_time = pd.DatetimeIndex(pd.to_datetime(data.starttime,
                                                 infer_datetime_format=True))
    groups = data.groupby([start_time.date, 'usertype'])
    grouped_data = groups.trip_id.count().unstack()

    fig, ax = plt.subplots(2, figsize=(12, 6), sharex=True)
    grouped_data['Member'].plot(ax=ax[0])
    grouped_data['Short-Term Pass Holder'].plot(ax=ax[1])

    ax[0].set_title('Annual Members')
    ax[1].set_title('Short-term Pass Users')

    ax[0].set_ylabel('Number of riders')
    ax[1].set_ylabel('Number of riders')
