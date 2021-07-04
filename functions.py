#A Fuction is block of code which will execute only when it is called

# def hello():
#     pass

def hello():
    print("Hello All!")
    print("Hi Sreya")
    print("Hi Krish")
    print(6)

hello()
print("something")
print("something")
print("something")
hello()



#We can Pass Data as Parameters

def hello_name(name):
    print("Hello" + " "+ name)

hello_name("Kishore")
hello_name("Ravi")

def task(name, work):
    print("{} is working as {}".format(name, work))

task("Ramesh", "Carpenter")

def age_fun(name, age):
    print("The age of {} is {}".format(name, age))

age_fun("Ravi", 13)


def cal_sum(a, b , c):
    return a + b + c

summ = cal_sum(2, 3, 1)

print(summ)

def fee_paid(name, paid="No"):
    print("{}, {} paid the fee".format(paid, name))

fee_paid("Ramana", "Yes")

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info(3, 4, 5, name="sreya", age="15")

def sum_of(*args):
    summ = 0
    for i in args:
        summ = summ + i
    print(summ)

sum_of(2, 3)
sum_of(2, 3, 5)

nums = [3, 8, 5, 0]
student = {"name": "Krish", "age": 11}
student_info(*nums, **student) #Unpack




