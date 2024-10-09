from src.core.logger import logger
from src.schemas.schema import DailyWeather


def send_msg(nice_weather: list[DailyWeather]) -> None:
    """Send message"""
    for weather in nice_weather:
        logger.info(f'{weather=}')
