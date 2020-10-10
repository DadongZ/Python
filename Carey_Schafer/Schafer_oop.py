# regular method (self)
# class method (cls)
# static method () don't pass anything automatically
# dunker method __method__; automatically directly called
# decorator: define a method but access it like an attribute

class Employee():
    """Employee class
    """
    # class attributes
    num_of_emps = 0 
    raise_amount = 1.04 

    def __init__(self, first, last, pay):
        # self is the instance itself
        # instance attributes
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1
 
    # regular method: automatically taks in the instance as the first argument
    def fullname(self):
        return f'{self.first} {self.last}'

    # decorator
    @property
    def email(self):
        return f'{self.first}.{self.last}@complany.com'

    def apply_raise(self):
        # self.raise_amount allow to change for each instance
        # Employee.raise_amount only allow to change globally
        self.pay = int(self.pay * self.raise_amount)
    
    # dunker method
    ## __repr__ an unambiguous representation of the object
    ## should be used for debugging and logging
    def __repr__(self):
        # return a string I can use to recreate the object
        return f'Employee({self.first}, {self.last}, {self.pay})'
    
    ## readable representation of the object
    ## used as a display to the end-user
    def __str__(self):
        return f'{self.fullname()}-{self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    # class method decorator
    # receive class=cls automatically as first argument instead of instance
    @classmethod
    def set_raise_amt(cls, amount):
        """set pya raise amount
        """
        cls.raise_amount = amount   

    # class method an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        """
        docstring
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Inheritance (classname)
class Developer(Employee):
   raise_amount = 1.10 # without affect of the parent class

   def __init__(self, first, last, pay, prog_lang):
       """Developer
       """
       #let parent class handle the common attributes
       super().__init__(first, last, pay)
       #alternatively Employee.__init__(self, first, last, pay) 
       self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        """
        docstring
        """
        super().__init__(first, last, pay)
        if employees is None:
           self.employees=[]
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employess.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        [print(e.fullname()) for e in self.employees]



emp_1 = Employee('Halley', 'Ji', 20000)
print(emp_1.email) #instead of print(emp_1.email()) due to decorator @property

# emp_2 = Employee('Alex', 'Zhang', 30000)
# print(emp_1)
# print(emp_1.__str__())
# print(str(emp_1))
# print(emp_1.__repr__())
# print(repr(emp_1))

# print(emp_1 + emp_2)
# print(emp_1.__add__(emp_2))


