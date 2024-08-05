#!/usr/bin/env python3
"""Module for API Authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Manages API Authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if authentication is required for a given path."""
        return False

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header from the request."""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user based on the request."""
        return request
