from fastapi import APIRouter
from models.users import User
from controllers import controller_users
router = APIRouter()

@router.post("/api/adduser/")
async def newUser(user: User):
    if controller_users.addUsers(dict(user)):
        return {"Registration":"Valid"}
    else:
        return {"Registration":"Error"}
    
@router.post("/api/login/")
async def login(user: User):
    if controller_users.validUser(dict(user)):
        return {"Login":"Valid"}
    else:
        return {"Login":"Error"}