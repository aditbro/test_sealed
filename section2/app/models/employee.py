from sqlalchemy import (
    Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class EmployeeDB(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    name = Column(String)
