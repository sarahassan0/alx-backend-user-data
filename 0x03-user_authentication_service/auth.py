#!/usr/bin/env python3
"""Auth module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes user's password """
    password_bytes = password.encode('utf-8')
    hashed_pass = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_pass
