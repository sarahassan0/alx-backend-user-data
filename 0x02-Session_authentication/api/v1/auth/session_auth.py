#!/usr/bin/env python3
"""
    SessionAuth Mmdule
"""

from .auth import Auth


class SessionAuth(Auth):
    """ SessionAuth Class"""
    def __init__(self) -> None:
        """ initalize SessionAuth class"""
        super().__init__()
