#!/usr/bin/env python3
"""Module for filter_datum function"""
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscates log messages"""
    for field in fields:
        pattern = rf'{field}=([^ {separator}]*)'
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message
