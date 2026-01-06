from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This creates a file named 'intel_archive.db' in your project folder
SQLALCHEMY_DATABASE_URL = "sqlite:///./intel_archive.db"

# SQLite specific argument: check_same_thread=False allows FastAPI to access it safely
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()