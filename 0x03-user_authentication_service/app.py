#!/usr/bin/env python3
"""Module for Flask APP"""
from flask import Flask, request, jsonify, abort
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=["GET"])
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
        return jsonify({"email": new_user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Retrieves a session for user or creates a new one"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
