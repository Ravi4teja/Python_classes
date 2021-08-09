# Special Methods(Magic Methods or Dunder) Methods

print(type(5))
print(type("Ravi"))

print(2 + 3)
print(int.__add__(2, 3))

print("Sreya" +  "Krish")
print(str.__add__("Sreya", "Krish"))


#Creating class
class Employee:

    #Constructor 
    #which will be called automatically while creating the object
    def __init__(self, first, last, salary):

        #Instance Variables
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + "@Company.com"

    #Instance Methods
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    # An Ambiguous representation of object used for debugging and logging. Generally used bt developers.
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.salary)

    #A Readable representation of an object meant to be to display to end user.
    def __str__(self):
        return "{} {}".format(self.first, self.last)

    #This special method returns sum of self and other salary
    def __add__(self, other):
        return self.salary + other.salary

    #This special method returns count of fullname method
    def __len__(self):
        return len(self.fullname())
    

#Creating Objects
emp_1 = Employee("Ravi", "Teja", 60000)


# print(emp_1)
print(emp_1.__repr__())
print(repr(emp_1))

print(str(emp_1))
print(emp_1.__str__())

emp_2 = Employee("Krishna", "Mohan", 55000)

print(Employee.__add__(emp_1, emp_2))
print(emp_1.__add__(emp_2))
print(emp_1 + emp_2)

print(len("Ravi"))

print(Employee.__len__(emp_1))
print(emp_1.__len__())
print(len(emp_1))



#https://docs.python.org/3/reference/datamodel.html






