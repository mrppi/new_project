from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL= "postgresql+psycopg2://training_inc0_user:FeCAsUQJfHtvShlzUPrxwWUHuL92Itea@dpg-dbbfgnbrjlhs73e3gpqg-a.oregon-postgres.render.com/training_inc0"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()