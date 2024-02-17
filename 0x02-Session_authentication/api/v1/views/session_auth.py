#!/usr/bin/env python3
""" Module of session_auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def user_login_session() -> str:
    """ POST /auth_session/login
    Return:
      - User object JSON represented
      - error if can't login the User
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    if password is None or len(password) == 0:
        return jsonify({"error": "password  missing"}), 400

    user = User().search({'email': email})[0]

    if user is None:
        return jsonify({"error": "no user found for this email"}), 404

    is_valid_pwd = user.is_valid_password(password)

    if not is_valid_pwd:
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        SESSION_NAME = getenv('SESSION_NAME')

        res = jsonify(user.to_json())
        res.set_cookie(SESSION_NAME, session_id)
        return res


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def user_delete_session() -> str:
    """ DELETE /api/v1/auth_session/logout
    Return:
      - empty object JSON represented
      - error if there's no session
    """

    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    else:
        return jsonify({}), 200
