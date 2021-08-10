#property decorators - Getters, Setters and Deleters

class Employee:

    def __init__(self,first, last):
        self.first = first
        self.last = last

    @property #This is getter
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    @property #This is getter
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter #This is setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter #This is deleter
    def fullname(self):
        print("Deleted FullName!")
        self.first = None
        self.last = None
        
    
emp_1 = Employee("Ramana", "Varma")

emp_1.first = "Rahul"

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

print("---------------")

emp_1.fullname = "Kishore Kumar"

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

print("---------------")

del emp_1.fullname

print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)


