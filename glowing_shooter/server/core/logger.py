import logging
import sys
from config.default import BASE_LOGGER_NAME, BASE_LOGGER_LEVEL


def configure_logger():
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
