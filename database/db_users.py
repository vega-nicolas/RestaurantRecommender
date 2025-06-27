from pymongo.errors import DuplicateKeyError
from database.connection import client
from controllers import security

userCollection = client.RestaurantRecommender.Users
tokenCollection = client.RestaurantRecommender.Tokens
def addUsers(user: dict) -> bool:
    try:
        userCollection.create_index([("username", 1)], unique=True)
        userCollection.create_index([("email", 1)], unique=True)
        if userCollection.find_one({"username": user.get("username")}):
            return False
        if userCollection.find_one({"email": user.get("email")}):
            return False
        userCollection.insert_one(user)
        return True

    except DuplicateKeyError:
        return False
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return False
    
def validUser(user: dict) -> bool:
    user_db = userCollection.find_one({"email": user["email"]})
    if not user_db:
        return False
    elif user_db["password"] == None:
        return False
    elif not security.checkPassword(user["password"], user_db['password']):
        return False
    else:
        return True
    
def addToken(token_data: dict) -> None:
    tokenCollection.create_index("token", unique=True)
    token_data["token"] = security.hashToken(token_data["token"])
    tokenCollection.insert_one(token_data)

def findToken(token: str) -> dict:
    return tokenCollection.find_one({"token": security.hashToken(token)})

def deleteToken(token: str) -> None:
    tokenCollection.delete_one({"token": security.hashToken(token)})