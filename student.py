from datetime import date, timedelta
import requests

class Student:
    # A student class as a base for method testing
    
    """ 
Initializes a new instance of the Student class with a user entered first_name and last_name.
self.start_date: Sets the start date to the current date.
self.end_date: Sets the end date to one year from the current date.
self.naughty_list: Initializes the naughty_list attribute to False.
    """
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False
        
    @property 
    def full_name(self):
        return self.first_name + " " + self.last_name
    """
    Defines a read-only property full_name that returns the full name of the student by
    concatenating the first and last names with a space in between.
    """
    
    @property
    def email(self):
        return self.first_name.lower() + "." + self.last_name.lower() + "@email.com"
    """
    Defines a read-only property email that returns the email address of the student
    in the format firstname.lastname@email.com, with both names in lowercase.
    """
    
#Read-only properties cannot be modified directly.
# Attempting to set these properties will raise an AttributeError
# student.full_name = "Jane Doe"  # This will raise an error
# student.email = "jane.doe@email.com"  # This will raise an error
    
    def alert_santa(self):
        self.naughty_list = True
        return self.naughty_list
    """
    Defines a method alert_santa that sets the naughty_list attribute to True and returns its value.
    """
    
    def apply_extension(self, days):
        self.end_date += timedelta(days=days)
    """
Method Definition: The method apply_extension is defined with two parameters: self and days.
self refers to the instance of the class to which this method belongs.
days is the number of days by which the end_date should be extended.

Accessing end_date: The method accesses the end_date attribute of the instance (self.end_date).

Using timedelta: The method uses the timedelta class from the datetime module to create a time
duration representing the number of days specified by the days parameter.

Adding timedelta to end_date: The timedelta object is added to the end_date, effectively extending
it by the specified number of days. 
    """
    
    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/{self.first_name}/{self.last_name}")
        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"
    """
This mocks a API request to a course schedule website.

HTTP GET Request:
The method constructs a URL using the student's first and last names:
f"http://company.com/course-schedule/{self.first_name}/{self.last_name}".
It then makes an HTTP GET request to this URL using the requests.get method from the requests library.
The response from this request is stored in the response variable.

Check Response Status:
The method checks if the request was successful by evaluating response.ok.
response.ok is a boolean attribute that is True if the HTTP status code is less than 400, indicating
a successful request.

Return Response Text or Error Message:
If response.ok is True, the method returns the text content of the response using response.text.
If response.ok is False, the method returns the string "Something went wrong with the request!".     
    """