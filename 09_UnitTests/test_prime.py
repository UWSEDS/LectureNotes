import unittest
from prime import check_prime

# Define a class in which the tests will run
# Insert code like that used in notebook

class UnitTests(unittest.TestCase):

    # Each method in the class to execute a test
    def test_success(self):
        self.assertTrue(check_prime(5))

if __name__ == '__main__':
    unittest.main()
