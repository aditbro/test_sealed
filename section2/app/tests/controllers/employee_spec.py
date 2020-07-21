import random
from app.models import EmployeeDB
from app.schemas import Employee
from app.tests import client, clear_db, session
from app.tests.factories import EmployeeFactory
from expects import expect, equal, be_none
from mamba import description, context, it, before, after


with description('POST /v1/employee'):
    with context('given valid employees attributes') as self:
        with before.each:
            n_employee = random.randint(1, 10)
            self.employees = EmployeeFactory.build_batch(n_employee)
            self.employees = list(map(Employee.from_orm, self.employees))

        with after.each:
            clear_db()

        with it('creates new user and return status 200'):
            data = {
                'employees': list(map(lambda x: x.dict(), self.employees))
            }
            response = client.post('/v1/employee/',
                                   json=data)
            expect(response.status_code).to(equal(200))

            employees = session.query(EmployeeDB)\
                               .all()
            expect(employees).not_to(be_none)
            employees = list(map(Employee.from_orm, employees))

            for i in range(len(employees)):
                expect(employees[i].dict()).to(equal(self.employees[i].dict()))
