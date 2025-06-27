from controllers import security
from database import db_users
from database.connection import client

def addUsers(user: dict) -> bool:
    del user["id"]
    user["password"] = security.hashPassword(user["password"])
    if db_users.addUsers(user):
        return True
    else:
        return False

def validUser(user: dict) -> bool:
    if db_users.validUser(user):
        return True
    else:
        return False