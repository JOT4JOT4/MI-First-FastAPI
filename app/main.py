from fastapi import FastAPI
from app.api.v1.routes import router as api_router
from app.db.session import connect_to_mongo, close_mongo_connection, get_database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await connect_to_mongo()
    print(f"Database connection: {get_database}")  # para debug

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(api_router, prefix="/api/v1")