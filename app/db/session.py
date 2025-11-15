from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings, MONGODB_URL, DATABASE_NAME


DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


client: AsyncIOMotorClient | None = None
db: AsyncIOMotorDatabase | None = None

async def connect_to_mongo():
    global client, db
    try:
        client = AsyncIOMotorClient(MONGODB_URL)
        db = client[DATABASE_NAME]
        
        await client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        print(f"Database: {DATABASE_NAME}")
    except Exception as e:
        print(e)
        raise

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("MongoDB connection closed")



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_database() -> AsyncIOMotorDatabase:
    if db is None:
        raise Exception("Database not initialized. Call connect_to_mongo() first.")
    return db