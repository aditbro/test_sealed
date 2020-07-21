import random
from app.models import EmployeeDB
from app.schemas import Employee
from app.tests import client, clear_db, session
from app.tests.factories import EmployeeFactory
from expects import expect, equal, be_empty
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

            employees = session.query(EmployeeDB).all()
            expect(employees).not_to(be_empty)
            employees = list(map(Employee.from_orm, employees))

            for i in range(len(employees)):
                expect(employees[i].dict()).to(equal(self.employees[i].dict()))

    with context('given one of the employees is invalid') as self:
        with before.each:
            n_employee = random.randint(1, 9)
            self.employees = EmployeeFactory.build_batch(n_employee)
            faulty_employee = EmployeeFactory.build(login=self.employees[0].login)
            self.employees.append(faulty_employee)
            self.employees = list(map(Employee.from_orm, self.employees))

        with after.each:
            clear_db()

        with it('does not save employee data and returns 409'):
            data = {
                'employees': list(map(lambda x: x.dict(), self.employees))
            }
            response = client.post('/v1/employee/',
                                   json=data)
            expect(response.status_code).to(equal(409))

            employees = session.query(EmployeeDB).all()
            expect(employees).to(be_empty)


with description('PUT /v1/employee/{id}'):
    with context('given valid id and employees attributes') as self:
        with before.each:
            self.employee = EmployeeFactory.create()
            self.empl_update = EmployeeFactory.build()
            self.empl_update = Employee.from_orm(self.empl_update)

        with after.each:
            clear_db()

        with it('updates the current employee data'):
            data = self.empl_update.dict()
            response = client.put('/v1/employee/{}'.format(self.employee.id),
                                  json=data)
            expect(response.status_code).to(equal(200))

            employee = session.query(EmployeeDB).get(self.empl_update.id)
            employee = Employee.from_orm(employee)
            expect(employee.dict()).to(equal(self.empl_update.dict()))

    with context('employee id is invalid') as self:
        with before.each:
            self.employee = EmployeeFactory.create()
            self.empl_update = EmployeeFactory.build()
            self.empl_update = Employee.from_orm(self.empl_update)

        with after.each:
            clear_db()

        with it('do nothing and returns 404'):
            fault_id = self.employee.id + 'asdsad'
            data = self.empl_update.dict()
            response = client.put('/v1/employee/{}'.format(fault_id),
                                  json=data)
            expect(response.status_code).to(equal(404))

            old_employee = Employee.from_orm(self.employee)
            new_employee = session.query(EmployeeDB).get(self.employee.id)
            new_employee = Employee.from_orm(self.employee)
            expect(old_employee.dict()).to(equal(new_employee.dict()))
