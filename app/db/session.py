from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings, MONGODB_URL, DATABASE_NAME


DATABASE_URL = "sqlite:///./test.db"  # Cambia esto a tu URL de base de datos

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

client: AsyncIOMotorClient | None = None
db: AsyncIOMotorDatabase | None = None

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(MONGODB_URL)
    print(client)
    db = client[DATABASE_NAME]

async def close_mongo_connection():
    global client
    if client:
        client.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

