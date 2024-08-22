import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

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
    
    def test_course_schedule_success(self):
        print("test_course_schedule_seccess")
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")
            
    """
Mocking requests.get:
The patch function from the unittest.mock module is used to replace the requests.get method in the
student module with a mock object (mocked_get).
This allows the test to control the behavior of requests.get without making actual HTTP requests.

Setting Mock Return Values:
mocked_get.return_value.ok = True: This sets the ok attribute of the mock response to True, simulating
a successful HTTP response.
mocked_get.return_value.text = "Success": This sets the text attribute of the mock response to "Success",
simulating the content of the HTTP response.

Calling course_schedule:
The course_schedule method of the student object is called, and its return value is stored in the schedule
variable.
Since requests.get is mocked, the course_schedule method will receive the mocked response.

Assertion:
self.assertEqual(schedule, "Success"): This asserts that the return value of course_schedule is "Success".
If the assertion is true, the test passes. If not, the test fails.
    """
            
    def test_course_schedule_failed(self):
        print("test_course_schedule_failed")
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")
    """
Mocking requests.get:
The patch function from the unittest.mock module is used to replace the requests.get method in the student
module with a mock object (mocked_get).
This allows the test to control the behavior of requests.get without making actual HTTP requests.

Setting Mock Return Values:
mocked_get.return_value.ok = False: This sets the ok attribute of the mock response to False, simulating
a failed HTTP response.

Calling course_schedule:
The course_schedule method of the student object is called, and its return value is stored in the schedule
variable.
Since requests.get is mocked, the course_schedule method will receive the mocked response.

Assertion:
self.assertEqual(schedule, "Something went wrong with the request!"): This asserts that the return value
of course_schedule is "Something went wrong with the request!".
If the assertion is true, the test passes. If not, the test fails.     
    """
if __name__ == "__main__":
    unittest.main()
#This block ensures that the tests are run when the script is executed directly.