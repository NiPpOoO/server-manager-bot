import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/server_manager_db")
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key")
    DEBUG = os.getenv("DEBUG", True)
