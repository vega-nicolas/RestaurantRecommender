from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: str = None
    username: str = None
    email: str = None
    password: str = None
    created_at: datetime = datetime.now()
