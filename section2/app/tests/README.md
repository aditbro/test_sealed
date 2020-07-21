# Testing

## What tests are available
- behaviour test using `mamba`
- code style test using `flake8`

## Test environment dependency
The program uses redis and postgresql to store data. To run those programs in your testing environment, a docker-compose file has been provided

## How to run the tests
### Behaviour test
install mamba and coverage first
```
pip install mamba coverage
```
then run mamba from project root
```
mamba tests/ --enable-coverage
```
then check how much code has been covered by the test
```
coverage report -m
```
the ideal case is 100% of the program is covered by the tests

### Code style check
install flake8 first
```
pip install flake8
```
then run flake8 from project's root
```
flake8
```
ideally there should be no violation of the code style approved by flake8

## Basic Test Structure
The idea of the test is to test the program behaviour. given this is an api program, the main focus is to test the behaviour of every endpoint. </br>
every block of test define the behaviour of the tested program in such format:
```
#http_verb #endpoint : given #params it #does_something
```
for example:
```
POST /auth/register : given correct user params, it creates new user, send confirmation email, and return success
```
the sample function description translates to the program structure as below:
```python
with description('POST /auth/register'):
    with context('given correct user params') as self:
        with it('creates new user, send email to user, and return success'):
```
the description block defines what endpoint with what http verb is being tested. </br>
the context block defines the condition of which the endpoint is going to be tested, e.g the params, the database status, the data status, etc. </br>
the it block defines the desired behaviour given the context.