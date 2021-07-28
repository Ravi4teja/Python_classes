#Object-Oriented Programming.

#Class Variables:Class Variables are variables those values are common to every intance/object/.

#Instance Variables: Instance Variables are unique to the particular instace/Object

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


print(Employee.No_of_Employees)

emp_1 = Employee("Ravi", "Teja", 60000)

emp_2 = Employee("Kishore", "Kumar", 65000)

#Accessing Class Variable
print(Employee.No_of_Employees)


print(emp_1.salary)

emp_1.salary_raise()

print(emp_1.salary)

print(emp_2.salary)

emp_2.salary_raise()

print(emp_2.salary)

#Checking the instance Variables of object
print(emp_1.__dict__)

#Checking the Methods and Class Variables of object
print(Employee.__dict__)

#Chaging Class Variable to instance Variable to particular object through modifying it.
emp_2.raise_income = 1.07

emp_2.special_salary_raise()

print(emp_2.salary)


print(emp_1.__dict__)
print(emp_2.__dict__)


#---------------Assignment---------------#
#In the Same Rectangle class. Create the Class variable called Color and assign "red" to it.
#Create a method to change the color.
#----------------------------------------#