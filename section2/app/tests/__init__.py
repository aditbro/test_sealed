from app.main import app
from app.db import session
from fastapi.testclient import TestClient
from sqlalchemy import MetaData

client = TestClient(app)

def clear_db():
    meta = MetaData(bind=session.get_bind(), reflect=True)
    session.rollback()

    for table in reversed(meta.sorted_tables):
        session.execute(table.delete())
    session.commit()

clear_db()

