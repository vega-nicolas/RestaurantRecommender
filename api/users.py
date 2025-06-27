from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
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
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if controller_users.validUser({"email": form_data.username, "password": form_data.password}):
        return {"Login":"Valid"}
    else:
        return {"Login":"Error"}