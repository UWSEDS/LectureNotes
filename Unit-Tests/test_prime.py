import unittest
from prime import check_prime

# Define a class in which the tests will run
class PrimeTest(unittest.TestCase):

    def testSimple(self):
        self.assertTrue(check_prime(3))
    
    
if __name__ == '__main__':
    unittest.main()
