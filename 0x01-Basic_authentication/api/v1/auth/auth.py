#!/usr/bin/env python3
"""Module for API Authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Manages API Authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """"""
        return False

    def authorization_header(self, request=None) -> str:
        """"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """"""
        return None
