#!/usr/bin/env python3
"""Implements End-to-end integration test
"""

import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
HOST_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """Test register user scenario"""


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login user with wrong password scenario"""


def log_in(email: str, password: str) -> str:
    """Test user login scenario """


def profile_unlogged() -> None:
    """Test accessibility of unlogged user to /profile page date"""


def profile_logged(session_id: str) -> None:
    """Test accessibility of logged user to /profile page date"""


def log_out(session_id: str) -> None:
    """Test user logout scenario"""


def reset_password_token(email: str) -> str:
    """Test getting user reset token"""


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test update password scenario"""


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
