# Employee module

class Employee():
    """Class representing an employee"""

    raise_factor = 1.05

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_factor)
    
