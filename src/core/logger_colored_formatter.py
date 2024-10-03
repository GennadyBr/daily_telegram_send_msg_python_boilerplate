import logging


class ColoredFormatter(logging.Formatter):
    """Custom Color Formatter Class"""

    COLORS = {
        'DEBUG': '\033[94m',  # Blue
        'INFO': '\033[92m',  # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',  # Red
        'CRITICAL': '\033[95m',  # Magenta
    }
    RESET = '\033[0m'

    def format(self, record):
        """Add color to log levels"""
        log_level = record.levelname
        if log_level in self.COLORS:
            record.colorlevel = (
                f'{self.COLORS[log_level]}{log_level}{self.RESET}'
            )
        else:
            record.colorlevel = log_level
        return super().format(record)


colored_format = (
    '%(asctime)s - %(name)s - %(colorlevel)s '
    '- %(module)s:(%(funcName)s):%(lineno)d - %(message)s'
)
colored_formatter = ColoredFormatter(fmt=colored_format)
