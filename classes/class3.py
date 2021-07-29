#Object-Oriented Programming.

#Class Methods: Class Methods take cls as their first argument.It can be called through Class name.

#Class Methods can be used as alternative constructors.

#A constructor is the method which will call automatically while creating object.This will initialize the instance Variables.

#Static Methods: Static method dont need to have self/cls as its first argument.

#Importing datetime module
import datetime

class Employee:

    #Class Variables
    raise_income = 1.05
    No_of_Employees = 0

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + "@Company.com"
        #Changing class variable value through constructor
        Employee.No_of_Employees = Employee.No_of_Employees + 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def salary_raise(self):
        self.salary =  int(self.salary * Employee.raise_income)

    def special_salary_raise(self):
        self.salary =  int(self.salary * self.raise_income)

    #Class method
    @classmethod
    def set_raise_income(cls, income):
        cls.raise_income = income
    
    #Using Class method as a alternative constructor
    @classmethod
    def object_from_str(cls, emp_str):
        first, last , salary = emp_str.split("-")
        return cls(first, last, salary)  

    #Static Method
    @staticmethod
    def is_weekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False


emp_1 = Employee("Ravi", "Teja", 60000)

emp_2 = Employee("Kishore", "Kumar", 65000)

print(Employee.raise_income)

#Calling class method
Employee.set_raise_income(1.07)

print(Employee.raise_income)

emp_3_str = "Ram-Kamal-50000"
emp_4_str = "Kiran-Venu-67000"
emp_5_str = "Harish-Kumar-45000"

#Creating objects through classmethod(alternative constructor)
emp_3 = Employee.object_from_str(emp_3_str)
emp_4 = Employee.object_from_str(emp_4_str)
emp_5 = Employee.object_from_str(emp_5_str)

print(emp_3.email)
print(emp_4.email)
print(emp_5.email)

#Creating date using datet
my_date = datetime.date(2021, 7, 31)
                   #Calling Static Method
print("Weekend? ", Employee.is_weekend(my_date))


#---------------Assignment-----------------#
#In the same Rectangle class
#Create a class method called change_our_color() that will take the color as an argument and 
# it changes the color to given color in the argument.

#Create a static method called is_leap_year that will take year as an argument and
#it should return True/False based on whether it is leap year or not.
#Hint: For this you can use calender module. Or you can use ur calculation.

#----------------------------------------#






