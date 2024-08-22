import unittest
from student import Student

class TestStudent(unittest.TestCase):
# TestStudent: A subclass of unittest.TestCase, which provides various methods to
# test the Student class.
    
    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")
# setUp: This method is called before each test method. It initializes a Student object
# with the name "John Doe" and assigns it to self.student.
  
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
        
if __name__ == "__main__":
    unittest.main()
#This block ensures that the tests are run when the script is executed directly.