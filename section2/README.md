# FastAPI Project Template
Is this solution overengineered for the problem given? yes, it kinda is. But I've been working on this fastapi template for any backend projects in the future and it would be a waste if I don't use it. This template also has a rather clean structure.

## Requirements
* Python 3.8
* Poetry for Python package and environment management.
### If you want to use docker
* Docker
* Docker Compose
### If not
* Latest Postgresql

## How to run the app
1. either do (poetry install && poetry shell) or (pip3 install -r requirements.txt)
2. run postgresql, either with or without docker
3. change config.yaml setting to the matching db setting
4. run `scripts/run_local.sh` (don't forget to set the permission)
5. you can check localhost:8000/docs for the available APIs and authentication scheme