import json
from app.tests import client, clear_db, session
from app.tests.factories import UserFactory
from expects import expect, equal
from mamba import description, context, it, before, after

with description('POST /v1/auth/token'):
    with context('given valid username and password') as self:
        with before.each:
            self.user = UserFactory.create()

        with after.each:
            clear_db()

        with it('returns user token with code 200'):
            data = dict(username=self.user.username,
                        password=self.user.password)

            response = client.post('/v1/auth/token', data=data)
            expect(response.status_code).to(equal(200))

            token = json.loads(response.text)['access_token']
            session.refresh(self.user)
            expect(token).to(equal(self.user.login_token))

    with context('given wrong password') as self:
        with before.each:
            self.user = UserFactory.create()

        with after.each:
            clear_db()

        with it('returns error 404'):
            data = dict(username=self.user.username,
                        password='wrong password')

            response = client.post('/v1/auth/token', data=data)
            expect(response.status_code).to(equal(404))
