import atexit
import os
from sqlalchemy import create_engine, DateTime, String, func, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped


# POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "153268425Zz")
# POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
# POSTGRES_DB = os.getenv("POSTGRES_DB", "flask")
# POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
# POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5431")

PG_DSN = "postgresql://postgres:153268425Zz@localhost:5431/flask"


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