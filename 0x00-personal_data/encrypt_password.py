#!/usr/bin/env python3
"""Module for hash_password function"""
import bcrypt


def hash_password(password: str) -> bytes:
    """encrypts passwrd and returns a salted hashed password"""
    pw_encode = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pw_encode, salt)

    return hashed_password
