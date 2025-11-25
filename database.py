from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:Hasaali@localhost:5432/sana"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False,bind=engine)