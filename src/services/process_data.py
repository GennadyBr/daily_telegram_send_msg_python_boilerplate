from typing import Union

import pandas as pd
from openmeteo_sdk.VariablesWithTime import VariablesWithTime
from openmeteo_sdk.WeatherApiResponse import WeatherApiResponse

from src.core.logger import logger
from src.schemas.schema import DailyWeather


def _get_dates(
    raw_date: VariablesWithTime,
) -> Union[None, pd.DatetimeIndex]:
    """Extract date from response"""
    try:
        date = pd.date_range(
            start=pd.to_datetime(raw_date.Time(), unit='s', utc=True),
            end=pd.to_datetime(raw_date.TimeEnd(), unit='s', utc=True),
            freq=pd.Timedelta(seconds=raw_date.Interval()),
            inclusive='left',
        )
    except ValueError:
        logger.exception('Could not process response.Daily()')
        return None

    return date


def _get_weather_data(
    raw_daily_data: VariablesWithTime,
    date_list: pd.DatetimeIndex,
) -> list[DailyWeather]:
    """
    Process daily data.
    The order of variables needs to be the same as requested.
    """
    daily_weather: list = []
    tmp_dict: dict = {}
    tmp_list: list = [
        'temperature_2m_max',
        'temperature_2m_min',
        'precipitation_sum',
        'wind_speed_10m_max',
    ]
    date_count = 0
    for date in date_list:
        tmp_dict['date'] = date
        for item_count in range(raw_daily_data.VariablesLength()):
            try:
                item: float = round(
                    float(
                        raw_daily_data.Variables(item_count).ValuesAsNumpy()[
                            date_count
                        ],
                    ),
                    1,
                )
            except ValueError:
                logger.exception('Could not process daily.Variables()')
                item = 0.0
            tmp_dict[tmp_list[item_count]] = item
        daily_weather.append(DailyWeather(**tmp_dict))
        date_count += 1

    return daily_weather


def process_data(
    responses: Union[None, list[WeatherApiResponse]],
) -> list[DailyWeather]:
    """Process weather data"""
    response = responses[0] if isinstance(responses, list) else responses

    raw_daily_data: VariablesWithTime = response.Daily()
    date_list: pd.DatetimeIndex = _get_dates(raw_daily_data)

    return _get_weather_data(raw_daily_data, date_list)
