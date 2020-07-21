import factory
from app.db import session
from app.models import UserDB


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = UserDB
        sqlalchemy_session = session

    id = factory.Sequence(lambda n: n)
    username = factory.Faker('user_name')
    password = factory.Faker('password')
    name = factory.Faker('name')
    email = factory.Faker('email')
    is_email_verified = factory.Faker('pybool')
    telephone = factory.Faker('phone_number')
    created = factory.Faker('date_time')
    updated = factory.lazy_attribute(lambda n: n.created)

    class Params:
        logged_in = factory.Trait(
            login_token=factory.Faker('pystr')
        )
