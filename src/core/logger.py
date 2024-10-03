"""Logger"""

import logging.config
import os

import yaml

from src.core.logger_colored_formatter import colored_formatter

dir_name = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)),
    ),
)


with open('core/logger.yaml', 'r') as logger_yaml:
    logger_config = yaml.safe_load(logger_yaml)

    # replace filename to one with current folder
    # because I can't put current folder inside yaml file
    logger_config['handlers']['file']['filename'] = f'{dir_name}/logs/logs.log'
    logging.config.dictConfig(logger_config)


logger = logging.getLogger()

logging.getLogger('urllib3').setLevel(logging.INFO)
logging.getLogger('requests_cache').setLevel(logging.INFO)

# Replace str_formatter with colored_formatter
# because I can't put class ColoredFormatter inside yaml file
logger.handlers[0].setFormatter(colored_formatter)

logger.info('X' * 100)

# Test the color handler
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
