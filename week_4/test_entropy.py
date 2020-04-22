import unittest
import entropy

# Define a class in which the tests will run
class UnitTests(unittest.TestCase):

    # Each method in the class to execute a test
    def test_smoke_test(self):
        result = entropy.entropy([0.5, 0.5])
        self.assertTrue(isinstance(result, float))
        

if __name__ == '__main__':
    unittest.main()
