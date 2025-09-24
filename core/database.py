from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from core.config import settings


engine = create_engine(
    settings.DATABASE_URL, 
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()