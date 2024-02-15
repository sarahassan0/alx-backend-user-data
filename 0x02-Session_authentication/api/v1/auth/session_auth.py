#!/usr/bin/env python3
"""
    SessionAuth Mmdule
"""

from .auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth Class"""
    user_id_by_session_id = {}

    def __init__(self) -> None:
        """
            initalize SessionAuth class
        """

        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
            Creates a Session ID for a user_id:
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id
        return session_id
