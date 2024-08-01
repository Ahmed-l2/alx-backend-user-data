#!/usr/bin/env python3
"""Module for filter_datum function"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Redacts specified fields in log message and formats the record"""
        log_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            log_message, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates log messages"""
    for field in fields:
        message = re.sub(fr"{field}=.+?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


PII_FIELDS = ('email', 'phone', 'ssn', 'password', 'ip')


def get_logger() -> logging.Logger:
    """Creates and configures a logger, then returns it"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()

    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
