#!/usr/bin/env python3
"""
    Auth Mmdule
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ "Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            require_auth method
            returns true if path requires authentication else false.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
            authorization header method
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):  # type: ignore
        """
            get current_user method
        """
        return None
