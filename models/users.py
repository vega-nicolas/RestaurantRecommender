from pydantic import BaseModel

class User(BaseModel):
    id: str = None
    username: str = None
    email: str = None
    password: str = None
