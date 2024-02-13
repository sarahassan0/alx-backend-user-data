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
        if path and excluded_paths and len(excluded_paths) > 0:
            if path in excluded_paths or path + "/" in excluded_paths or path[0:-1] in excluded_paths:
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


a = Auth()

print(a.require_auth(None, None))
print(a.require_auth(None, []))
print(a.require_auth("/api/v1/status/", []))
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
