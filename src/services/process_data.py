import pandas as pd

from src.core.logger import logger


def process_data(responses):
    """ Process weather data """
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

    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(3).ValuesAsNumpy()

    daily_data = {
        'date': pd.date_range(
            start=pd.to_datetime(daily.Time(), unit='s', utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit='s', utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive='left',
        ),
    }

    logger.info(f'{daily_data=}')

    daily_data['temperature_2m_max'] = daily_temperature_2m_max
    daily_data['temperature_2m_min'] = daily_temperature_2m_min
    daily_data['precipitation_sum'] = daily_precipitation_sum
    daily_data['wind_speed_10m_max'] = daily_wind_speed_10m_max

    daily_dataframe = None
    try:
        daily_dataframe = pd.DataFrame(data=daily_data)
    except Exception as e:
        logger.error(f'TypeError: {type(e)}')
        logger.error(f'Value: {daily_data}')
        logger.exception('METHOD EXCEPTION')

    logger.info(f'{type(daily_dataframe)=}')
    logger.info(f'{daily_dataframe=}')

    return daily_dataframe
