export API_ENV=dev
. scripts/load_env.sh \
&& poetry run flake8 \
&& poetry run mamba app/ --enable-coverage \
&& poetry run coverage report -m