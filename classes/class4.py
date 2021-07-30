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

class Developer(Employee):
    raise_income = 1.07

    def __init__(self, first, last, salary, programming_lang):
        super().__init__(first, last, salary)
        self.programming_lang = programming_lang



dev_1 = Developer("Charan", "Varma", 70000,"Python")
dev_2 = Developer("Harish", "Venu", 66000, "Java")

print(dev_1.email)
print(dev_1.programming_lang)


class Manager(Employee):
    
    def __init__(self, first, last, salary, emps = None):
        super().__init__(first, last, salary)
        if emps is not None:
            self.emps = emps
        if emps is None:
            self.emps = []
        
    def add_emp(self, employee):
        if employee not in self.emps:
            self.emps.append(employee)

    def remove_emp(self, employee):
        if employee in self.emps:
            self.emps.remove(employee)
    
    def print_emps(self):
        for emp in self.emps:
            print("--->", emp.fullname())

mgr_1 = Manager("Saif", "Ahmed", 70000, [dev_1])

mgr_1.add_emp(dev_2)

print(mgr_1.emps)

mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
print("-------")

mgr_1.print_emps()


mgr_2 = Manager("Ramana", "Ram", 80000)

mgr_2.add_emp(dev_1)
print("-------")

mgr_2.print_emps()

print(isinstance(dev_1, Developer))
print(isinstance(dev_1, Employee))
print(isinstance(dev_1, Manager))

print("-------")

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))






























