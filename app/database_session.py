from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.models import image_data 
# SQLAlchemy setup
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
print(settings.DATABASE_URL)
print("connection successfully")
image_data.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
