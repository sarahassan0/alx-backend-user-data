#!/usr/bin/env python3
"""
    SessionAuth Mmdule
"""

from .auth import Auth
import uuid
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            Creates a Session ID for a user_id
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
            Returns a User instance based on a cookie value
        """
        if request is None:
            return None

        SESSION_NAME = self.session_cookie(request)
        user_id = self.user_id_for_session_id(SESSION_NAME)

        if user_id is None:
            return None
        user = User.get(user_id)
        if user is None:
            return None

        return user
