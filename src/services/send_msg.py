from typing import Union

from pandas import DataFrame

from src.core.logger import logger


def send_msg(nice_weather: Union[None, DataFrame]) -> None:
    """Send message"""
    logger.info(f'{nice_weather=}')
