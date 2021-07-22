#Scopes


x = "global x" #Global Variable

def local_func1():
    x = "local x" #Local variable
    print(x) #Accessing local variable


local_func1()
print(x) #Accessing global variable


y = "global y" #Global Variable

def outer_func1():
    y = "outer y" #this is local variable to the outer_func1
    def inner_func1():
        y = "inner y" #this is local variable to the innner_func1
        print(y) #Accessing local variable in inner_func1 scope
    inner_func1()
    print(y) #Accessing local variable in outer_func1 scope

print(y) #Accessing global variable
outer_func1()
print("done")


z = "global z"

def local_func():
    global z #Using global variable
    z = "local z" #Modifying global variable
    print(z) #Accessing global variable


local_func()
print(z) #Accessing global variable


a = "global a"

def outer_func2():
    a = "outer a" #this is local to the outer_func
    def inner_func2():
        nonlocal a #Using variable from outer_func2 scope
        a = "inner a" #Modifying variable from outer_func2 scope
        print(a) #Accessing variable from outer_func2 scope
    inner_func2()
    print(a) #Accessing variable from outer_func2 scope

print(a) #Accessing global variable
outer_func2()
print("done")