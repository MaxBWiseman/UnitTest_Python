import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)
    
    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False) # should return False (empty list)
        self.assertEqual(even_number_of_evens([2, 4]), True)# should return True (two even numbers)
        self.assertEqual(even_number_of_evens([2]), False)# should return False (one even number)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)# should return False (no even numbers)
        
        """
        The assertRaises() method is used in unit testing to verify that a specific exception
        is raised when a certain piece of code is executed. It is commonly used in Python's
        unittest framework.
        """


if __name__ == "__main__":
    unittest.main()
    
"""
Imports:

unittest: The built-in Python module for creating and running tests.
even_number_of_evens: The function being tested, imported from the evens module.
Test Class:

TestEvens is a subclass of unittest.TestCase, which provides methods to create and run tests.

Test Methods:

test_throws_error_if_value_passed_in_is_not_list:
Uses self.assertRaises(TypeError, even_number_of_evens, 4) to check if passing a non-list value
(in this case, 4) raises a TypeError.
test_values_in_list:
Uses self.assertEqual to check the return values of even_number_of_evens for various inputs:
even_number_of_evens([]) should return False (empty list).
even_number_of_evens([2, 4]) should return True (two even numbers).
even_number_of_evens([2]) should return False (one even number).
even_number_of_evens([1, 3, 5]) should return False (no even numbers).
Main Execution:

if __name__ == "__main__": unittest.main() runs the tests when the script is executed directly.
"""