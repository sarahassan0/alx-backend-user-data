#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', strict_slashes=False)
def index() -> str:
    """ main route
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
