import bcrypt
import hashlib

def hashPassword(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def checkPassword(password: str, hash: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))

def hashToken(input: str) -> str:
    if input == None:
        return None
    elif input == "":
        return None
    else:
        return hashlib.sha256(input.encode()).hexdigest()