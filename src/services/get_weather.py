from typing import Union

import openmeteo_requests
import requests_cache
from openmeteo_sdk.WeatherApiResponse import WeatherApiResponse
from requests_cache import CachedSession
from retry_requests import retry

from src.core.logger import logger


def get_weather() -> Union[None, list[WeatherApiResponse]]:
    """
    Get weather data from Open-Meteo
    """
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session: CachedSession = requests_cache.CachedSession(
        '.cache',
        expire_after=3600,
    )
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily to assign them correctly below
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': 55.687450,
        'longitude': 36.964410,
        'daily': [
            'temperature_2m_max',
            'temperature_2m_min',
            'precipitation_sum',
            'wind_speed_10m_max',
        ],
        'timeformat': 'unixtime',
        'timezone': 'Europe/Moscow',
        'forecast_days': 3,
    }

    responses: Union[None, list[WeatherApiResponse]] = None
    try:
        responses = openmeteo.weather_api(
            url,
            params=params,
        )
    except ConnectionError as my_error:
        logger.exception(f'Open-Meteo API error: {my_error}')

    return responses
