. scripts/load_env.sh
echo $db_type
cd alembic
alembic upgrade head
cd ..
