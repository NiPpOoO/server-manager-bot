from app.models.log import Log
from app import db

class LogRepository:
    @staticmethod
    def save_log(message):
        log = Log(message=message)
        db.session.add(log)
        db.session.commit()
