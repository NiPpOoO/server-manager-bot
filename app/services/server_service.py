import os
from app.utils.logging import log_info, log_error

class ServerService:
    @staticmethod
    def restart_server():
        try:
            os.system("sudo reboot")
            log_info("Сервер перезапущен")
            return {"message": "Server is restarting"}
        except Exception as e:
            log_error(f"Ошибка при перезапуске: {e}")

    @staticmethod
    def shutdown_server():
        try:
            os.system("sudo shutdown -h now")
            log_info("Сервер выключен")
            return {"message": "Server is shutting down"}
        except Exception as e:
            log_error(f"Ошибка при выключении: {e}")

