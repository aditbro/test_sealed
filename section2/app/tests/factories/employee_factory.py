import factory
from app.tests import session
from app.models import EmployeeDB
from faker import Faker
from uuid import uuid4

faker = Faker('zh_CN')


class EmployeeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = EmployeeDB
        sqlalchemy_session = session

    id = factory.LazyAttribute(lambda x: str(uuid4()))
    login = factory.Faker('user_name')
    name = factory.LazyAttribute(lambda x: faker.name())
