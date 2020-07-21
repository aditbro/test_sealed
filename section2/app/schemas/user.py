from pydantic import BaseModel
from datetime import datetime


class BaseUser(BaseModel):
    username: str
    email: str
    name: str
    telephone: str

    class Config:
        orm_mode = True


class UserNew(BaseUser):
    password: str
    is_email_verified: bool = False


class UserGet(BaseUser):
    id: int = None
    created: datetime
    is_email_verified: bool
    updated: datetime


class UserInDB(UserNew, UserGet):
    pass
