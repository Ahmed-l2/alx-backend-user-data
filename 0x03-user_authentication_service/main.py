#!/usr/bin/env python3
"""
Main file
"""
import requests


def register_user(email: str, password: str) -> None:
    """Test for registering a new user and handling duplicate registration."""
    url = "http://0.0.0.0:5000/users"
    data = {"email": email, "password": password}

    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}

    response = requests.post(url, data=data)
    assert response.status_code == 400
    assert response.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """"""
    url = "http://0.0.0.0:5000/sessions"
    data = {"email": email, "password": password}

    response = requests.post(url, data=data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """"""
    url = "http://0.0.0.0:5000/sessions"
    data = {"email": email, "password": password}

    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}

    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """"""
    response = requests.get('http://127.0.0.1:5000/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """"""
    url = "http://0.0.0.0:5000/profile"
    data = {"session_id": session_id}
    response = requests.get(url, cookies=data)
    assert response.status_code == 200
    response.json() == {"email": EMAIL}


def log_out(session_id: str) -> None:
    """"""
    url = "http://0.0.0.0:5000/profile"
    data = {"session_id": session_id}
    response = requests.get(url, cookies=data)
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """"""
    url = "http://0.0.0.0:5000/reset_password"
    data = {"email": email}

    response = requests.post(url, data=data)

    assert response.status_code == 200
    reset_token = response.json().get('reset_token')
    assert response.json() == {"email": email, "reset_token": reset_token}
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """"""
    url = "http://0.0.0.0:5000/reset_password"
    data = {"email": email, "reset_token": reset_token,
            "new_password": new_password}

    response = requests.put(url, data=data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


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
