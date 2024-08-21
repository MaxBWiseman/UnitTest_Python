from datetime import date, timedelta

class Student:
    # A student class as a base for method testing
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False
        
    @property 
    def full_name(self):
        return self.first_name + " " + self.last_name