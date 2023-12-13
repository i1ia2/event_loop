import atexit
import os
from sqlalchemy import create_engine, DateTime, String, func, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_USER = os.getenv("POSTGRES_USER", "app")
POSTGRES_DB = os.getenv("POSTGRES_DB", "app")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5431")

PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Advertisement(Base):
    __tablename__ = "app_users"
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String)
    description = mapped_column(String)
    creation_date = mapped_column(DateTime)
    owner = mapped_column(String)

Base.metadata.create_all(bind=engine)

atexit.register(engine.dispose)