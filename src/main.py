""" Daily Send MSG to Telegram Python Boilerplate Library """
from typing import Union

from pandas import DataFrame

from src.services.get_weather import get_weather
from src.services.process_data import process_data
from src.services.send_msg import send_msg

if __name__ == '__main__':
    weather: Union[None, list] = get_weather()
    nice_weather: Union[None, DataFrame] = process_data(weather)
    send_msg(nice_weather)
