""" Daily Send MSG to Telegram Python Boilerplate Library """
import os
import sys
from typing import Union

# Add the root directory of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.schemas.schema import DailyWeather
from src.services.get_weather import get_weather
from src.services.process_data import process_data
from src.services.send_msg import send_msg

if __name__ == '__main__':
    weather: Union[None, list] = get_weather()
    daily_weather: list[DailyWeather] = process_data(weather)
    send_msg(daily_weather)
