from app.schemas import Employees, Employee
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
async def employee_post(employees: Employees) -> Any:
    employees = list(
        map(lambda x: EmployeeDB(**x.dict()), employees.employees)
    )
    for employee in employees:
        session.add(employee)

    session.commit()
    return ({'message': 'success'})


@employee_router.get(
    '/',
    responses=responses.responses,
    status_code=200
)
async def employee_get(
    offset: int = 0, limit: int = 10, sort: str = '+id'
) -> Employees:
    sort_field = sort[1:]
    sort_dir = sort[0]
    sort_obj = getattr(EmployeeDB, sort_field)

    if sort_dir == '-':
        sort_obj = sort_obj.desc()

    employees = session.query(EmployeeDB) \
                       .order_by(sort_obj) \
                       .offset(offset) \
                       .limit(limit) \
                       .all()

    employees = Employees(**{'employees': employees})
    return employees


@employee_router.put(
    '/{id}',
    responses=responses.responses,
    summary='update a registered employee',
    status_code=200
)
async def employee_put(id: str, employee: Employee) -> Any:
    curr_empl = session.query(EmployeeDB) \
        .filter(EmployeeDB.id == id) \
        .one()
    for key, value in employee.dict().items():
        setattr(curr_empl, key, value)
    session.commit()

    return ({'message': 'success'})
