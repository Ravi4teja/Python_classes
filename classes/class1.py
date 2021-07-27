#Object-Oriented Programming.

#Class - Class is a Blueprint of Objects/Instances.
#An Object is an instance of Class.

#We use Class to logically group the features and behaviours of objects

# class Employee:
#     pass

# emp_1 = Employee()

# emp_1.first = "Ravi"
# emp_1.last = "Teja"
# emp_1.email = "Ravi.Teja@Company.com"
# emp_1.salary = 60000
# emp_1.contact = "989796858"

# emp_2 = Employee()

# emp_2.first = "Kishore"
# emp_2.last = "Kumar"
# emp_2.email = "Kishore.Kumar@Company.com"
# emp_2.salary = 65000


# print(emp_2.salary)
# print(emp_1.contact)
# print(emp_2.contact)

class Employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + "@Company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("Ravi", "Teja", 60000)

emp_2 = Employee("Kishore", "Kumar", 65000)

print(emp_1.email)
print(emp_2.email)


print(emp_1)
print(emp_2)

# print("{} {}".format(emp_1.first, emp_1.last))

print(emp_1.fullname())

print(Employee.fullname(emp_1))



#--------------Assignment-------------------#
#Create a class called Rectangle
#instance variables should be length and width
#create another instance variable called diagonal with the help of length and width provided.
#create methods to the Rectangle class - Area, Perimeter


#Once creation of the Rectangle class is completed. Create two objects and access the instance variables and call the instance methods.
#-------------------------------------------#