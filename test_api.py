import unittest
import json
from api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_add(self):
        response = self.client.post("/api/add",
            json={"a": 2, "b": 3})
        data = json.loads(response.data)
        self.assertEqual(data["result"], 5)
    
    def test_subtract(self):
        response = self.client.post("/api/subtract",
            json={"a": 5, "b": 2})
        data = json.loads(response.data)
        self.assertEqual(data["result"], 3)
    
    def test_multiply(self):
        response = self.client.post("/api/multiply",
            json={"a": 4, "b": 3})
        data = json.loads(response.data)
        self.assertEqual(data["result"], 12)
    
    def test_divide(self):
        response = self.client.post("/api/divide",
            json={"a": 10, "b": 2})
        data = json.loads(response.data)
        self.assertEqual(data["result"], 5)
    
    def test_square(self):
        response = self.client.post("/api/square",
            json={"a": 4})
        data = json.loads(response.data)
        self.assertEqual(data["result"], 16)

if __name__ == "__main__":
    unittest.main()
