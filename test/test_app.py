import unittest
import os
from app.app import app  # adjust path if needed


class TestColorApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        """Valid color should return 200."""
        os.environ['BG_COLOR'] = '#00ff00'
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_invalid_color(self):
        """Invalid hex color should return 500."""
        os.environ['BG_COLOR'] = 'invalidcolor'
        response = self.app.get('/')
        self.assertEqual(response.status_code, 500)
        self.assertIn(b'Invalid color', response.data)

    def test_default_color(self):
        """Default color should be used if BG_COLOR not set."""
        os.environ.pop('BG_COLOR', None)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'#00ff00', response.data)


if __name__ == '__main__':
    unittest.main()
