"""
import logging
from logging import config as logging_config

LOG_FORMAT = ('%(asctime)s - %(name)s - %(levelname)s - '
              '%(filename)s:%(lineno)d - %(funcName)s - %(message)s')
# formatter = "%(asctime)s - %(name)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s"

LOG_DEFAULT_HANDLERS = ['console']


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': LOG_FORMAT,
        },
        'default': {
            '()': 'uvicorn.logging.DefaultFormatter',
            'fmt': '%(levelprefix)s %(message)s',
            'use_colors': None,
        },
        'access': {
            '()': 'uvicorn.logging.AccessFormatter',
            'fmt': '%(levelprefix)s %(client_addr)s '
                   '- "%(request_line)s" %(status_code)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'default': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'access': {
            'formatter': 'access',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {
            'handlers': LOG_DEFAULT_HANDLERS,
            'level': 'INFO',
        },
        'uvicorn.error': {
            'level': 'INFO',
        },
        'uvicorn.access': {
            'handlers': ['access'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    'root': {
        'level': 'INFO',# logging.getLogger('urllib3').setLevel(logging.INFO)
# logging.getLogger('requests_cache').setLevel(logging.INFO)
# logger.setLevel(0)
#
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(logging.Formatter(std_format))
# logger.addHandler(console_handler)
#
# file_handler = logging.FileHandler(f'{dir_name}/logs/logs.log')
# file_handler.setFormatter(logging.Formatter(std_format))
# logger.addHandler(file_handler)

        'formatter': 'verbose',
        'handlers': LOG_DEFAULT_HANDLERS,
    },
}

logging_config.dictConfig(LOGGING)
# logger = logging.getLogger(__name__)
logger = logging.getLogger()
"""

import logging.config
import os
import yaml

std_format = ('%(asctime)s - %(name)s - %(levelname)s '
              '- %(filename)s:%(lineno)d - %(funcName)s - %(message)s')

dir_name = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)),
    ),
)
#
# logger_config = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'default': {
#             'format': std_format,
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'level': 'DEBUG',
#             'formatter': 'default',
#         },
#         'file': {
#             'class': 'logging.FileHandler',
#             'level': 'DEBUG',
#             'filename': f'{dir_name}/logs/logs.log',
#             'formatter': 'default',
#         },
#     },
#     'loggers': {
#         '': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#         },
#     },
# }
#
# logging.config.dictConfig(logger_config)

with open('core/logger.yaml', 'r') as logger_yaml:
    logger_config = yaml.safe_load(logger_yaml)
    logger_config['handlers']['file']['filename'] = f'{dir_name}/logs/logs.log'
    logging.config.dictConfig(logger_config)


logger = logging.getLogger()

logging.getLogger('urllib3').setLevel(logging.INFO)
logging.getLogger('requests_cache').setLevel(logging.INFO)
# logger.setLevel(0)
#
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(logging.Formatter(std_format))
# logger.addHandler(console_handler)
#
# file_handler = logging.FileHandler(f'{dir_name}/logs/logs.log')
# file_handler.setFormatter(logging.Formatter(std_format))
# logger.addHandler(file_handler)

logger.info('X'*100)

