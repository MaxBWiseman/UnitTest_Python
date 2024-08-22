import unittest
from student import Student
from datetime import timedelta

class TestStudent(unittest.TestCase):
# TestStudent: A subclass of unittest.TestCase, which provides various methods to
# test the Student class.

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        # setUpClass is called once before any tests are run, setting up a shared resource.
    """ 
Class Method: The method is defined with the @classmethod decorator,
which means it takes the class itself as the first argument (cls).
Setup: The setUpClass method is called once before any test methods in the class are executed.
Shared State: Any setup that is needed for all tests in the class can be performed here.
    """
    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        # tearDownClass is called once after all tests are run, cleaning up the shared resource.
    """ 
Class Method: The method is defined with the @classmethod decorator,
which means it takes the class itself as the first argument (cls).
Teardown: The tearDownClass method is called once after all test methods in the class have been executed.
Shared State Cleanup: Any cleanup that is needed for all tests in the class can be performed here.
    """
    
    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")
# setUp: This method is called before each test method. It initializes a Student object
# with the name "John Doe" and assigns it to self.student.

    def tearDown(self):
        print("tearDown")
        # Perform any necessary cleanup here
        del self.student
    """
Setup: The setUp() method is called before each test method to prepare the test environment.
Test Execution: The test method is executed.
Teardown: The tearDown() method is called after each test method to clean up the test environment.

the tearDown() method deletes the self.student object after each test method is executed. This ensures
that each test method starts with a fresh instance of the Student class.
    """
  
    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")
# This method tests the full_name property of the Student class.
# self.assertEqual: Asserts that self.student.full_name is equal to "John Doe".
        
    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)
        
    """ 
This method tests the alert_santa method of the Student class.
self.student.alert_santa(): Calls the alert_santa method, which sets naughty_list to True.
self.assertTrue: Asserts (makes sure) that self.student.naughty_list is True.
    """
    
    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email,"john.doe@email.com")
# This method tests the email property of the Student class.
# self.assertEqual: Asserts (makes sure) that self.student.email is equal to "john.doe@email.com".

    def test_apply_extension(self):
        print("test_apply_extension")
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, self.student.start_date + timedelta(days=370))
    """
When a Student object is instantiated, its start_date is set to the current date, and its end_date is set
to one year (365 days) from the current date.
The apply_extension method adds 5 days to the end_date.
Therefore, the end_date should now be 370 days from the start_date (365 initial days + 5 additional days).
The assertion checks if this is true, ensuring that the apply_extension method works correctly.

Example: 
Assume today's date is January 1, 2023:
start_date = January 1, 2023
end_date = January 1, 2024 (365 days from start_date)
After calling apply_extension(5):
end_date = January 6, 2024 (370 days from start_date)
    """
        
if __name__ == "__main__":
    unittest.main()
#This block ensures that the tests are run when the script is executed directly.