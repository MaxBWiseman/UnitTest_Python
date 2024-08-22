from datetime import date, timedelta

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