from fastapi import FastAPI
from app.routes.server_routes import server_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

app = FastAPI()
app.include_router(server_bp)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
