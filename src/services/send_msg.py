import requests

from src.core.config import TELEGRAM_BOT_TOKEN, TELEGRAM_MSG_RECEIVER
from src.core.logger import logger
from src.schemas.schema import DailyWeather


def send_msg(message: list[DailyWeather]) -> None:
    """Send message"""
    message_str: str = ''
    for weather in message:
        logger.info(f'{weather=}')
        message_str += weather.__str__() + '\n\n'

    logger.info(f'weather_str = {message_str}')
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': TELEGRAM_MSG_RECEIVER,
        'text': message_str,
    }
    response = requests.post(
        url,
        params=params,
    )
    logger.info(f'response = {response}')
    logger.info(f'response.text = {response.text}')
