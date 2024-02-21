#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
