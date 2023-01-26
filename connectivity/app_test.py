from app import app
import unittest

class FlaskTest(unittest.TestCase):
    
    def test_app(self):
        tester = app.test_client(self)
        response = tester.get("/ping/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

if __name__ == "__main__":
    unittest.main()
