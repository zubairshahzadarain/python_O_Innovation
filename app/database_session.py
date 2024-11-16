from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.config import settings

# SQLAlchemy setup
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
metadata = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
