from fastapi import APIRouter
from .v1 import api_router

v1_router = APIRouter()
v1_router.include_router(api_router, prefix='/v1')
