import unittest
import json
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        """Set up test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    # --- Home Route Tests ---

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    # --- Add Tests ---

    def test_add_positive(self):
        response = self.app.get('/add?a=2&b=3')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 5.0)

    def test_add_negative(self):
        response = self.app.get('/add?a=-2&b=-3')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], -5.0)

    def test_add_mixed(self):
        response = self.app.get('/add?a=10&b=-4')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 6.0)

    def test_add_missing_params(self):
        response = self.app.get('/add?a=5')
        self.assertEqual(response.status_code, 400)

    # --- Subtract Tests ---

    def test_subtract_positive(self):
        response = self.app.get('/subtract?a=10&b=4')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 6.0)

    def test_subtract_negative_result(self):
        response = self.app.get('/subtract?a=2&b=5')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], -3.0)

    def test_subtract_zero(self):
        response = self.app.get('/subtract?a=7&b=0')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 7.0)

    def test_subtract_missing_params(self):
        response = self.app.get('/subtract?b=3')
        self.assertEqual(response.status_code, 400)

    # --- Multiply Tests ---

    def test_multiply_positive(self):
        response = self.app.get('/multiply?a=3&b=4')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 12.0)

    def test_multiply_by_zero(self):
        response = self.app.get('/multiply?a=5&b=0')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 0.0)

    def test_multiply_negative(self):
        response = self.app.get('/multiply?a=-3&b=4')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], -12.0)

    def test_multiply_missing_params(self):
        response = self.app.get('/multiply')
        self.assertEqual(response.status_code, 400)

    # --- Divide Tests ---

    def test_divide_even(self):
        response = self.app.get('/divide?a=10&b=2')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], 5.0)

    def test_divide_decimal(self):
        response = self.app.get('/divide?a=7&b=2')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertAlmostEqual(data['result'], 3.5, places=4)

    def test_divide_negative(self):
        response = self.app.get('/divide?a=-9&b=3')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['result'], -3.0)

    def test_divide_by_zero(self):
        response = self.app.get('/divide?a=5&b=0')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_divide_missing_params(self):
        response = self.app.get('/divide?a=10')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
