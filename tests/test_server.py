import unittest
from app.services.server_service import ServerService

class ServerTest(unittest.TestCase):
    def test_restart_server(self):
        response = ServerService.restart_server()
        self.assertEqual(response["message"], "Server is restarting")

    def test_shutdown_server(self):
        response = ServerService.shutdown_server()
        self.assertEqual(response["message"], "Server is shutting down")

if __name__ == "__main__":
    unittest.main()
