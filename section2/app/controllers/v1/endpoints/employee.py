from app.schemas import NewEmployees, Employee
from app.models import EmployeeDB
from app.db import session
from app.controllers.v1 import responses
from fastapi import APIRouter
from typing import Any

employee_router = APIRouter()


@employee_router.post(
    '/',
    responses=responses.responses,
    summary='create new employees',
    status_code=200
)
async def employee_post(employees: NewEmployees) -> Any:
    employees = list(
        map(lambda x: EmployeeDB(**x.dict()), employees.employees)
    )
    for employee in employees:
        session.add(employee)

    session.commit()
    return ({'message': 'success'})


@employee_router.put(
    '/{id}',
    responses=responses.responses,
    summary='update a registered employee',
    status_code=200
)
async def employee_post(employee: Employee) -> Any:
    pass
