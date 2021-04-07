import unittest
from secure_all import AccessManager
import os
MY_DIRECTORY = os.getcwd() +"/testingfiles"

class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_dir=os.getcwd()
        print(my_dir)
        print("Working directory", MY_DIRECTORY)
        print("open("+ MY_DIRECTORY + "request.json)")
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()


