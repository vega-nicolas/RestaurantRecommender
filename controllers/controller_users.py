from controllers import security
from database import db_users
import re

formatUsername = r'^[a-zA-Z0-9]+$'
formatEmail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def addUsers(user: dict) -> bool:
    try:
        if matchNewUser(user):
            user["username"] = user["username"].strip().lower()
            user["email"] = user["email"].strip().lower()
            user["password"] = security.hashPassword(user["password"])
            user.pop("id", None)
            return db_users.addUsers(user)
        return False
    except Exception:
        return False

def validUser(user: dict) -> bool:
    try:
        if not matchLogin(user):
            return False
        return db_users.validUser(user)
    except Exception:
        return False
    
def matchNewUser(user: dict) -> bool:
    required_fields = ["username", "email", "password"]
    for field in required_fields:
        if field not in user or not isinstance(user[field], str):
            return False
    username = user["username"].strip().lower()
    email = user["email"].strip().lower()
    password = user["password"].strip()
    if not username or not email or not password:
        return False
    if not re.match(formatUsername, username) or '$' in username:
        return False
    if not re.match(formatEmail, email):
        return False
    if len(password) < 8:
        return False
    if not re.search(r'[A-Za-z]', password) or not re.search(r'[0-9]', password):
        return False
    return True

def matchLogin(user: dict) -> bool:
    required_fields = ["password"]
    if "username" not in user and "email" not in user:
        return False
    for field in required_fields:
        if field not in user or not isinstance(user[field], str):
            return False
    if "username" in user and not isinstance(user["username"], str):
        return False
    if "email" in user and not isinstance(user["email"], str):
        return False
    username = user.get("username", "").strip()
    email = user.get("email", "").strip()
    password = user["password"].strip()
    if not password or (username == "" and email == ""):
        return False
    if username and not re.match(formatUsername, username):
        return False
    if email and not re.match(formatEmail, email):
        return False
    if len(password) < 8:
        return False
    if not re.search(r'[A-Za-z]', password) or not re.search(r'[0-9]', password):
        return False
    return True