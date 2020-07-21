from pydantic import BaseModel, Field
from typing import List
from uuid import uuid4


class Employee(BaseModel):
    id: str = Field(default_factory=uuid4)
    login: str
    name: str

    class Config:
        orm_mode = True


class NewEmployees(BaseModel):
    employees: List[Employee]
