#!/usr/bin/env python3
"""
    Auth Mmdule
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            require_auth method
            returns true if path requires authentication else false.
        """
        if path and excluded_paths and len(excluded_paths) > 0:
            if (path in excluded_paths or path + "/" in excluded_paths
                    or path[0:-1] in excluded_paths):
                return False

            for ex_path in excluded_paths:
                if (ex_path.endswith('*') and path.startswith(ex_path[:-1])):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
            authorization header method
        """
        if request and "Authorization" in request.headers:
            return request.headers["Authorization"]
        return None

    def current_user(self, request=None) -> TypeVar("User"):  # type: ignore
        """
            get current_user method
        """
        return None

    def session_cookie(self, request=None):
        """
            Returns a cookie value from a request:
        """
        if request is None:
            return None

        SESSION_NAME = getenv("SESSION_NAME")

        return request.cookies.get(SESSION_NAME)
