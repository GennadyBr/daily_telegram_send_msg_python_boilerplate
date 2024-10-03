from src.core.logger import logger


def send_msg(nice_weather):
    """Send message"""
    logger.info(f'{nice_weather=}')
