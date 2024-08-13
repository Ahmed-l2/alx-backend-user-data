#!/usr/bin/env python3
"""Module for the Auth"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Returns a salted hash of the input password, hashed with bcrypt
    """
    if not password:
        return
    encoded_password = password.encode('UTF-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password
