import logging
import sys
from config.default import BASE_LOGGER_NAME, BASE_LOGGER_LEVEL, WERKZEUG_LOGGER_ENABLED


class Loggable:
    def __init__(self):
        self.logger = None

    def set_logger(self, logger: logging.Logger) -> None:
        self.logger = logger

    def get_logger(self) -> logging.Logger:
        return self.logger if self.logger else logging.getLogger(__name__)


def configure_logger():
    if not WERKZEUG_LOGGER_ENABLED:
        werkzeug_logger = logging.getLogger("werkzeug")
        werkzeug_logger.disabled = True
        werkzeug_logger.propagate = False
    logger = logging.getLogger(BASE_LOGGER_NAME)
    # format = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
    format = "[%(asctime)s] %(levelname)s %(message)s"
    formatter = logging.Formatter(format)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(BASE_LOGGER_LEVEL)
    handler.setFormatter(formatter)

    logger.setLevel(BASE_LOGGER_LEVEL)
    logger.addHandler(handler)
    return logger
