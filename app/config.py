import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://denis_user:secure_password@localhost/server_manager_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
