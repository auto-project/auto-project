import logging
import sys
import time
from logging.handlers import RotatingFileHandler

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FORMAT = "%(asctime)s.%(msecs)03d{time_zone} %(levelname)-8s %(message)s"


def get_logger(name='dtc_manager', max_bytes=200000000, backup_count=5):
    if logging.getLogger(name).handlers:
        return logging.getLogger(name)
    time_zone = time.strftime('%z')
    fmt = LOG_FORMAT.format(time_zone=time_zone)
    formatter = logging.Formatter(fmt=fmt, datefmt=DATE_FORMAT)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(create_file_handler(name + ".log", formatter, max_bytes, backup_count))
    logger.addHandler(create_stdout_handler(formatter))
    return logger


def create_stdout_handler(formatter):
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    screen_handler.setLevel(logging.INFO)
    return screen_handler


def create_file_handler(path, formatter, max_bytes, backup_count):
    file_handler = RotatingFileHandler(path,
                                       maxBytes=max_bytes,
                                       backupCount=backup_count,
                                       encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    return file_handler
