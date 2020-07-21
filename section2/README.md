# FastAPI Project Template
Is this overengineered for the problem given? yes, it kinda is. But I've been working on this fastapi template for any backend projects in the future and it would be a shame not to use it.

## Requirements
* [Python 3.8](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/)
* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

## Local development
### Installing required dependency
1. Install each dependency from the requirements section above.
2. Install python virtualenv for python3.8
```
sudo apt install python3.8-venv
```
3. Set poetry env to use python3.8
```
poetry env use python3.8
```
4. Install poetry dependencies
```
poetry install
```

### Running the app
1. Run poetry shell
```
poetry shell
```
2. Export API_ENV
```
export API_ENV=dev
```
3. Run docker-compose
```
docker-compose up -d
```
4. To run the app localy you can use the run_local script **(please run the script from project main dir)**. the script will load the required environment variables and run the app. To inspect any available endpoints you can visit {app_host}:{port}/docs (normally http://localhost:8000/docs) which will run swagger.
```
scripts/run_local.sh
```
5. To run the app test suite you can use the test_app script. which will load the required environment variables, run the test suite, and calculate test coverage.
```
scripts/test_app.sh
```

## Project Structure
<pre>
├── README.md
├── alembic    -> directories concerning about database migrations
│   ├── README
│   ├── alembic.ini  -> database migration config
│   ├── env.py
│   ├── script.py.mako
│   └── versions  -> database migrations folder, come here to create or edit db migration
├── app
│   ├── __init__.py
│   ├── controllers  -> request receivers, this is where the requests are handled
│   ├── db.py  -> initiating db connection
│   ├── main.py  -> main entrypoint of the app
│   ├── models  -> store classes that represents the saved data in DB
│   ├── schemas  -> store classes that represents resources
│   ├── services  -> place to put functions that are commonly used between controllers or too complex
│   └── tests  -> testing suite folder
├── config.yaml  -> place to set environment variables that will be used
├── docker-compose.yml  -> place to set development tools requirements
├── poetry.lock  -> represents poetry dependency, DO NOT EDIT MANUALLY
├── pyproject.toml  -> poetry setting, TRY NOT TO EDIT MANUALLY
└── scripts  -> various helper script
    ├── load_env.py
    ├── load_env.sh  -> load environment variable to shell, use it like (. scripts/load_env.sh) (the initial dot is important)
    ├── run_local.sh  -> run the app localy
    ├── run_migration.sh  -> run database migration based on env var on config
    └── test_app.sh  -> run the app test suite
</pre>
