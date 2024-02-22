#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, redirect
from flask_cors import (CORS, cross_origin)
from auth import Auth


AUTH = Auth()


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', strict_slashes=False)
def index() -> str:
    """ main route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ Register a user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Login a user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie("session_id", session_id)
    return res


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ Logout a user
    """
    session_id = request.cookies.get('session_id')

    user = AUTH.get_user_from_session_id(session_id)

    if not user or AUTH.destroy_session(user.id):
        abort(403)

    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """Gets the user profile"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403)

    return jsonify({"email": user.email})


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """-Reset password- endpoint"""
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """Update password endpint"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
