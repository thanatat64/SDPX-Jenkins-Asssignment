import unittest
from fastapi.testclient import TestClient
from main import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
    def test_plus_endpoint(self):
        response = self.client.get("/plus/5/6")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 11})

        response = self.client.get("/plus/8/8")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 16})

if __name__ == "__main__":
    unittest.main()
