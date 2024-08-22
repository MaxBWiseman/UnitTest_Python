import unittest
from student import Student

class TestStudent(unittest.TestCase):
    """
The TestStudent class is a subclass of unittest.TestCase and contains a test method test_full_name.
The test_full_name method creates an instance of the Student class with the first name "John" and last name "Doe".
It then uses self.assertEqual to check if the full_name property of the student instance returns "John Doe".
    """  
    def test_full_name(self):
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")
        
    def test_alert_santa(self):
        student = Student("John", "Doe")
        student.alert_santa()
        self.assertTrue(student.naughty_list)
        
    """ 
Create an Instance of Student:
student = Student("John", "Doe"): This line creates a new instance of the Student class with the
first name "John" and last name "Doe".

Call alert_santa Method:
student.alert_santa(): This line calls the alert_santa method on the student instance. This method
is expected to set the naughty_list attribute of the student instance to True.

Assert naughty_list is True:
self.assertTrue(student.naughty_list): This line checks if the naughty_list attribute of the student
instance is True. If it is, the test passes; otherwise, it fails.
    """
    
    def test_email(self):
        student = Student("John", "Doe")
        self.assertEqual(student.email,"john.doe@email.com")
        
if __name__ == "__main__":
    unittest.main()