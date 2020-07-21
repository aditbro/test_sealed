from .endpoints import user_router, auth_router
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(user_router, tags=['user'], prefix='/user')
api_router.include_router(auth_router, tags=['user'], prefix='/auth')
