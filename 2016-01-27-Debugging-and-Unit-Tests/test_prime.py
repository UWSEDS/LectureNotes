''' Unit tests for prime.py '''

import unittest
from prime import primeChecker

class TestPrimeChecker(unittest.TestCase):

  # Test for primes
  def testPrimes(self):
    # 1 digit
    result = primeChecker(7)
    self.assertTrue(result[0])
    # 2 digit
    result = primeChecker(31)
    self.assertTrue(result[0])
    # 3 digit
    result = primeChecker(113)
    self.assertTrue(result[0])

  # Test non-primes
  def testNonPrimes(self):
    # 1 digit
    result = primeChecker(8)
    self.assertFalse(result[0])
    # 2 digit
    result = primeChecker(33)
    self.assertFalse(result[0])
    # 3 digit
    result = primeChecker(112)
    self.assertFalse(result[0])

  # Test explanation for non-prime
  def testExplanation(self):
    result = primeChecker(32)
    self.assertFalse(result[0])
    expected_explanation = "2 times 16 is 32"
    self.assertEqual(result[1], expected_explanation)
    

if __name__ == '__main__':
    unittest.main()
