from .auth import get_current_user
from app.schemas import UserNew, UserGet
from app.models import UserDB
from app.db import session
from app.controllers.v1 import responses
from fastapi import APIRouter, Depends
from typing import Any

user_router = APIRouter()


@user_router.post(
    '/',
    responses=responses.responses,
    summary='create new user',
    status_code=201
)
async def user_post(user: UserNew) -> Any:
    new_user = UserDB(**user.dict())
    session.add(new_user)
    session.commit()
    return ({'message': 'success'})


@user_router.get(
    '/me',
    responses=responses.responses,
    summary='get currently logged in user',
    status_code=200
)
async def user_get(user: UserGet = Depends(get_current_user)) -> UserGet:
    user = UserGet.from_orm(user)
    return user
