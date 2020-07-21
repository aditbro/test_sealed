# FastAPI Project Template
Is this solution overengineered for the problem given? yes, it kinda is. But I've been working on this fastapi template for any backend projects in the future and it would be a waste if I don't use it. This template also has a rather clean structure.

## Requirements
* Python 3.8
* Poetry for Python package and environment management. (not mandatory)
### If you want to use docker
* Docker
* Docker Compose
### If not
* Latest Postgresql

## How to run the app
### With Poetry
1. run `poetry use env python3.8`
2. run `poetry install`
3. run `poetry shell`

### Without Poetry
1. run pip3 install -r requierements.txt

### Then

1. run postgresql, either with or without docker
2. change config.yaml setting to the matching db setting
3. export current API_ENV `export API_ENV=dev`
4. run database migration `scripts/run_migration.sh`
5. run `scripts/run_local.sh` (don't forget to set the permission)
6. you can check localhost:8000/docs for the available APIs and authentication scheme
7. you can run `scripts/test_app.sh` to run the app test_suite