from pymongo.errors import DuplicateKeyError
from database.connection import client
from controllers import security

collection = client.RestaurantRecommender.Users
def addUsers(user: dict) -> bool:
    try:
        collection.create_index([("username", 1)], unique=True)
        collection.create_index([("email", 1)], unique=True)
        if collection.find_one({"username": user.get("username")}):
            return False
        if collection.find_one({"email": user.get("email")}):
            return False
        collection.insert_one(user)
        return True

    except DuplicateKeyError:
        return False
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return False
    
def validUser(user: dict) -> bool:
    user_db = collection.find_one({"email": user["email"]})
    if not user_db:
        return False
    elif user_db["password"] == None:
        return False
    elif not security.checkPassword(user["password"], user_db['password']):
        return False
    else:
        return True