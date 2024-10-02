""" Daily Send MSG to Telegram Python Boilerplate Library """
import logging
import sys

import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


def get_weather():
    """
    Get weather data from Open-Meteo
    """
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily to assign them correctly below
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': 55.69019,
        'longitude': 36.98053,
        'daily': [
            'temperature_2m_max',
            'temperature_2m_min',
            'precipitation_sum',
            'wind_speed_10m_max',
        ],
        'timezone': 'Europe/Moscow',
        'forecast_days': 1,
    }

    responses = openmeteo.weather_api(url, params=params)

    # Process first location.
    # Add a for-loop for multiple locations or weather models
    response = responses[0]
    logger.info(
        f'Coordinates {response.Latitude()}°N {response.Longitude()}°E',
    )
    logger.info(f'Elevation {response.Elevation()} m asl')
    logger.info(
        f'Timezone {response.Timezone()} {response.TimezoneAbbreviation()}',
    )
    logger.info(
        f'Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s',
    )

    # Process daily data.
    # The order of variables needs to be the same as requested.
    daily = response.Daily()
    logger.info(f'{daily=}')
    logger.info(f'{dir(daily)=}')
    logger.info(f'{daily.Variables()=}')

    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(3).ValuesAsNumpy()

    daily_data = {'date': pd.date_range(
        start=pd.to_datetime(daily.Time(), unit='s', utc=True),
        end=pd.to_datetime(daily.TimeEnd(), unit='s', utc=True),
        freq=pd.Timedelta(seconds=daily.Interval()),
        inclusive='left',
    )}
    daily_data['temperature_2m_max'] = daily_temperature_2m_max
    daily_data['temperature_2m_min'] = daily_temperature_2m_min
    daily_data['precipitation_sum'] = daily_precipitation_sum
    daily_data['wind_speed_10m_max'] = daily_wind_speed_10m_max

    daily_dataframe = pd.DataFrame(data=daily_data)
    logger.info(f'{type(daily_dataframe)=}')
    logger.info(f'{daily_dataframe=}')


def get_nice_weather(weather):
    return weather


def send_msg(nice_weather):
    pass


if __name__ == '__main__':
    weather = get_weather()

    nice_weather = get_nice_weather(weather)

    send_msg(nice_weather)
