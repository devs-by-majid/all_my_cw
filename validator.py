import re


def validate_username(username):

    pattern = r"^[A-Za-z][A-Za-z0-9_]{7,11}$"
    data = re.match(pattern, username)

    return bool(data)


def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
    data = re.match(pattern, password)
    return bool(data)


def validate_phone(phone):
    phone_pattern = r"^\+?[0-9]\d{7,13}$"
    data = re.match(phone_pattern, phone)
    return bool(data)


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    data = re.match(pattern, email)
    return bool(data)
