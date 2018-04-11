import unittest

# Define a class in which the tests will run
class UnitTests(unittest.TestCase):

    # Each method in the class to execute a test
    def test_success(self):
        self.assertEqual(1, 1)
        
    def test_success1(self):
        self.assertTrue(1 == 1)

    def test_failure(self):
        import pdb; pdb.set_trace()
        self.assertEqual(1, 2)  
    
if __name__ == '__main__':
    unittest.main()
