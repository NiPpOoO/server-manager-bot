import psutil

class SystemMonitor:
    @staticmethod
    def get_cpu_usage():
        return psutil.cpu_percent()

    @staticmethod
    def get_memory_usage():
        return psutil.virtual_memory().percent

    @staticmethod
    def get_disk_usage():
        return psutil.disk_usage('/').percent
