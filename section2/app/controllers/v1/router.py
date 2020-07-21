from .endpoints import employee_router
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(employee_router, tags=['user'], prefix='/employee')
