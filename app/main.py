from fastapi import FastAPI
from app.routes.server_routes import server_bp

app = FastAPI()
app.include_router(server_bp)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
