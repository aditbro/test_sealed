import factory
from app.db import session
from app.models import EmployeeDB
from uuid import uuid4


class EmployeeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = EmployeeDB
        sqlalchemy_session = session

    id = factory.LazyAttribute(lambda x: str(uuid4()))
    login = factory.Faker('user_name')
    name = factory.Faker('name')
