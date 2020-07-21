from app.controllers.v1 import responses
from app.models import UserDB
from app.db import session
from app.schemas import UserGet
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from uuid import uuid4

auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/token")


class Token(BaseModel):
    access_token: str
    token_type: str


@auth_router.post(
    '/token',
    response_model=Token,
    responses=responses.responses,
    summary='get user authentication token',
    status_code=200
)
async def token_post(
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Token:
    user = session.query(UserDB) \
                  .filter(UserDB.username == form_data.username) \
                  .filter(UserDB.password == form_data.password) \
                  .one()

    user.login_token = str(uuid4())
    session.commit()

    return Token(access_token=user.login_token, token_type='bearer')


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserGet:
    user = session.query(UserDB) \
                  .filter(UserDB.login_token == token) \
                  .one()
    user = UserGet.from_orm(user)
    return user
