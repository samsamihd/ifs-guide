from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# In a real project, we must put database credentials in .env files.
SQLALCHEMY_DATABASE_URL = "postgresql://ifs_db_user:59ip4hro5cv76ai4@db:5432/ifs_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
