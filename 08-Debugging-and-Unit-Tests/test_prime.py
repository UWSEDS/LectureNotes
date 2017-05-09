''' Unit tests for prime.py '''

import unittest
from prime import primeChecker

class TestPrimeChecker(unittest.TestCase):

  # Test for primes
  def testPrimes(self):
    # 1 digit
    result = primeChecker(7)
    self.assertTrue(result[0])

  # Test non-primes
  def testNonPrimes(self):
    result = primeChecker(8)
    self.assertFalse(result[0])
    result = primeChecker(582)
    self.assertFalse(result[0])

  # Test explanation for non-prime
  def testExplanation(self):
    result = primeChecker(32)
    self.assertFalse(result[0])
    expected_explanation = "2 times 16 is 32"
    self.assertEqual(result[1], expected_explanation)
    result = primeChecker(582)
    expected_explanation = '2 times 291 is 582'
    self.assertEqual(result[1], expected_explanation)
    

if __name__ == '__main__':
    unittest.main()
