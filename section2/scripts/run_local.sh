export API_ENV=dev
. scripts/run_migration.sh
uvicorn app:app --reload