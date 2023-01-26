from app import ping
import unittest

class FlaskTest(unittest.TestCase):
    
    def test_app(self):
        tester = ping.test_client(self)
        response = tester.get("/ping/")
        statuscode = response.statuscode
        self.assertEqual(statuscode, 200)

if __name__ == "__main__":
    unittest.main()