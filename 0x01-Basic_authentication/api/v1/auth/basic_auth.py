#!/usr/bin/env python3
"""
    Basic Auth Mmdule
"""

from .auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """decode base64 header"""
        if (base64_authorization_header is None
                or not isinstance(base64_authorization_header, str)):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """Extract username and password"""
        if (decoded_base64_authorization_header is None
                or not isinstance(decoded_base64_authorization_header, str)):
            return None, None

        user_credentials = decoded_base64_authorization_header.split(':', 1)

        if len(user_credentials) != 2:
            return None, None

        return tuple(user_credentials)
