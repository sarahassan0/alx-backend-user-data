#!/usr/bin/env python3
"""Auth module
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Hashes user's password """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email=email,
                                     hashed_password=hashed_password)
            return user


def _hash_password(password: str) -> bytes:
    """Hashes user's password """
    password_bytes = password.encode('utf-8')
    hashed_pass = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_pass
