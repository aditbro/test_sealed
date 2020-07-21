import json
from app.models import UserDB
from app.schemas import UserNew, UserGet
from app.tests import client, clear_db, session
from app.tests.factories import UserFactory
from expects import expect, equal, be_none, have_keys
from faker import Faker
from mamba import description, context, it, before, after


with description('POST /v1/user'):
    with context('given valid user attributes') as self:
        with before.each:
            faker = Faker()

            self.user = UserNew(
                username=faker.user_name(),
                password=faker.password(),
                name=faker.name(),
                email=faker.email(),
                telephone=faker.phone_number()
            )

        with after.each:
            clear_db()

        with it('creates new user and return status 201'):
            response = client.post('/v1/user/',
                                   json=self.user.dict())
            expect(response.status_code).to(equal(201))

            user = session.query(UserDB)\
                          .filter(UserDB.username == self.user.username)\
                          .first()
            expect(user).not_to(be_none)
            user = UserNew.from_orm(user)
            expect(user.dict()).to(have_keys(self.user.dict()))


with description('GET /v1/user/me'):
    with context('given request with valid token') as self:
        with before.each:
            self.user = UserFactory.create(logged_in=True)

        with after.each:
            clear_db()

        with it('returns logged in user with code 200'):
            headers = dict(Authorization='bearer ' + self.user.login_token)
            response = client.get('/v1/user/me', headers=headers)
            expect(response.status_code).to(equal(200))

            fetched_user = UserGet(**json.loads(response.text))
            saved_user = UserGet.from_orm(self.user)
            expect(fetched_user.dict()).to(equal(saved_user.dict()))
