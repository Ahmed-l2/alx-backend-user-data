#!/usr/bin/env python3
"""Module for the Auth"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


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


def _generate_uuid() -> str:
    """Returns a string representation of a new UUID"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers new user to the DB"""
        try:
            if self._db.find_user_by(email=email):
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validates the if the user exists"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        encoded_password = password.encode('UTF-8')
        if bcrypt.checkpw(encoded_password, user.hashed_password):
            return True
        return False
