""" Daily Send MSG to Telegram Python Boilerplate Library """
import requests

from src.core.logger import logger
from src.services.get_weather import get_weather
from src.services.process_data import process_data
from src.services.send_msg import send_msg


def check_exc():
    my_list = [1, 2, 3, {'key': 'value'}]

    for i in my_list:
        try:
            i = i * i
        except Exception as e:
            logger.error(f'TypeError: {type(e)}')
            logger.error(f'Value: {i}')
            logger.exception('METHOD EXCEPTION')


if __name__ == '__main__':
    weather = get_weather()
    nice_weather = process_data(weather)
    send_msg(nice_weather)

    requests.get('https://yandex.ru/')

    check_exc()
