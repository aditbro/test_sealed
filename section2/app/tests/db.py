import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_config = dict(
    db_type=os.environ['db_type'],
    db_name=os.environ['db_name'],
    host=os.environ['db_host'],
    user=os.environ['db_user'],
    password=os.environ['db_password'],
    port=os.environ['db_port']
)

db_uri = "{db_type}://{user}:{password}@{host}:{port}/{db_name}"
db_uri = db_uri.format(**db_config)

engine = create_engine(db_uri, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
