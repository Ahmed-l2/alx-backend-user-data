#!/usr/bin/env python3
"""Module for Flask APP"""
from flask import Flask, request, jsonify
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def main():
    """Basic route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Registers a new user"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        new_user = AUTH.register_user(email, password)
        return jsonify({"email": new_user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
