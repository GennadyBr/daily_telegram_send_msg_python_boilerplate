import openmeteo_requests
import requests_cache
from retry_requests import retry

from src.core.logger import logger


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

    responses = None
    try:
        responses = openmeteo.weather_api(url, params=params)
        logger.info(f'Open-Meteo API response: {responses}')
    except Exception as e:
        logger.error(f'Open-Meteo API error: {e}')

    return responses
