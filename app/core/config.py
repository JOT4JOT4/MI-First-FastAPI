import os
from dotenv import load_dotenv

load_dotenv()  # carga .env si existe en la raíz del proyecto

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "DisenoWeb")


class Settings:
    app_name: str = os.getenv("APP_NAME", "My FastAPI Project")
    admin_email: str = os.getenv("ADMIN_EMAIL", "admin@example.com")
    items_per_page: int = int(os.getenv("ITEMS_PER_PAGE", "10"))

settings = Settings()