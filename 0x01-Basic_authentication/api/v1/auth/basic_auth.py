#!/usr/bin/env python3
"""
    Basic Auth Mmdule
"""

from auth import Auth


class BasicAuth(Auth):
    """ BasicAuth Class"""

    def __init__(self) -> None:
        """ initalize BaseAuth class"""
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract Base64 part of the Authorization header"""
        if (authorization_header is None
                or type(authorization_header) is not str
                or not authorization_header.startswith('Basic ')):
            return None

        return authorization_header[6:]
