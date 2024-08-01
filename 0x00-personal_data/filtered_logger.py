#!/usr/bin/env python3
"""Module for filter_datum function"""
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscates log messages"""
    for field in fields:
        message = re.sub(rf'{field}=([^ {separator}]*)',
                         f"{field}={redaction}", message)
    return message
