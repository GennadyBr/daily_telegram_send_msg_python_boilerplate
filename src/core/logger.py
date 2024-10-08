"""Logger"""

import logging.config

import yaml

from src.core.colored_formatter import replace_formatter_4_all_loggers
from src.core.config import log_config_filename, log_rotation_filename

with open(log_config_filename, 'r') as file:
    logger_config = yaml.safe_load(file)
    logger_config['handlers']['file_rotation_handler'][
        'filename'
    ] = log_rotation_filename
    logging.config.dictConfig(logger_config)

logger = logging.getLogger()

# Replace root_formatter with colored_formatter
replace_formatter_4_all_loggers()

# Test the color handler
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
