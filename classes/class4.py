#Object-Oriented Programming.

#Inheritance: It is the Mechanism that one class can reuse/inherits the properties of another Class.
#and it can override them as well.

#Parent Class/Super Class/Base Class: The class whose properties are inherited
#Child class/Derived Class/Sub class/extended class: The class that inherits properties of another class.


class Employee:

    raise_income = 1.05

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + "@Company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def salary_raise(self):
        self.salary =  int(self.salary * Employee.raise_income)

#Subclass - Developer, Parent Class - Employee
class Developer(Employee):

    #Changing the class variable
    raise_income = 1.07

    #__init__ method(Constructor) for Developer class
    def __init__(self, first, last, salary, programming_lang):

        #Reusing and calling the Parent class constructor
        super().__init__(first, last, salary)
        #Creating instance variable
        self.programming_lang = programming_lang



dev_1 = Developer("Charan", "Varma", 70000,"Python")
dev_2 = Developer("Harish", "Venu", 66000, "Java")

print(dev_1.email)
print(dev_1.programming_lang)


class Manager(Employee):
    
    #__init__ method(Constructor) for Manager class
    def __init__(self, first, last, salary, emps = None):
        #Reusing and calling the Parent class constructor
        super().__init__(first, last, salary)

        #Checking the employees list provided or not. If provided then assiging that list to instance variable emps.
        if emps is not None:
            self.emps = emps
        #If not provided. Then assigning empty list to instance variable emps
        if emps is None:
            self.emps = []
    
    #This method will take Employee object argument. Checks if that employee not present in the self.emps list. 
    #If not there then will append the employee to the list
    def add_emp(self, employee):
        if employee not in self.emps:
            self.emps.append(employee)
    #This method will take Employee object argument. Checks if that employee already present in the self.emps list. 
    #If there then will remove that employee from the self.emps list.
    def remove_emp(self, employee):
        if employee in self.emps:
            self.emps.remove(employee)
    
    #This method will print the full names of the employees present in the self.emps list.
    def print_emps(self):
        for emp in self.emps:
            print("--->", emp.fullname())

#Creating Manager Object with list of employees
mgr_1 = Manager("Saif", "Ahmed", 70000, [dev_1])

#calling the add_emp method with argument dev_2. so that this method will add dev_2 to the list of employees under this manager
mgr_1.add_emp(dev_2)

print(mgr_1.emps)

mgr_1.print_emps()

#calling the remove_emp method with argument dev_1. so that this method will remove dev_1 from the list of employees under this manager
mgr_1.remove_emp(dev_1)
print("-------")

mgr_1.print_emps()

#Creating Manager Object without list of employees
mgr_2 = Manager("Ramana", "Ram", 80000)

mgr_2.add_emp(dev_1)
print("-------")

mgr_2.print_emps()


#isinstance method will check the object/instance belongs to that Class or to its SuperClass
print(isinstance(dev_1, Developer))
print(isinstance(dev_1, Employee))
print(isinstance(dev_1, Manager))

print("-------")

#issubclass method will check the first argument is the subclass of second argument.
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))






























