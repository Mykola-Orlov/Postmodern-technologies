import unittest
from dumb_code import exponentiation 

class TestDumbCode(unittest.TestCase):
    def test_dumb(self):
        self.assertEqual(exponentiation(2, 3), 8)

if __name__ == '__main__':
    unittest.main()