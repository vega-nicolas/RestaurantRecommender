from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.users import User
from controllers import controller_users

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login/")

@router.post("/api/adduser/", status_code=status.HTTP_201_CREATED)
async def new_user(user: User):
    if controller_users.addUsers(dict(user)):
        return {"message": "User registered successfully"}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User registration failed")

@router.post("/api/login/", status_code=status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if controller_users.validUser(dict({"email": form_data.username, "password": form_data.password})):
        token = controller_users.generate_token(form_data.username)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@router.get("/api/protected/", status_code=status.HTTP_202_ACCEPTED)
async def protected_endpoint(token: str = Depends(oauth2_scheme)):
    email = controller_users.validate_token(token)
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    return {"detail": "Valid Token"}