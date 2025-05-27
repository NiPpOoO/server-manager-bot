from fastapi import APIRouter
from app.services.server_service import ServerService

server_bp = APIRouter()

@server_bp.get("/server/status")
def check_status():
    return {"status": "running"}

@server_bp.post("/server/restart")
def restart_server():
    return ServerService.restart_server()

@server_bp.post("/server/shutdown")
def shutdown_server():
    return ServerService.shutdown_server()
