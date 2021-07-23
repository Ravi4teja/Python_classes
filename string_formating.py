name = "Sreya"
age = 16

# sentence = "Her name is {}. her age is {}. {} is going to school".format(name, age, name)

#Using the positions of parameters
sentence = "Her name is {0}. her age is {1}. {0} is going to school".format(name, age)

print(sentence)


person = {'name': 'Krish', 'age' : 12}

#Accessing the dictionary values using keys
sentence2 = "He name is {0[name]}. His age is {0[age]}. {0[name]} is going to school".format(person)

print(sentence2)

sentence3 = "My name is {name1}. My Fav subject is {subject1}. {name1} is going to office".format(name1 = "Ravi", subject1 = "Maths")

print(sentence3)

#padding 0s
for i in range(1, 11):
    print("The number is {:03}".format(i))

pi = 3.14159265359

#specifying 
sentence4 = "The value of pi is {:.6}".format(pi)

print(sentence4)


import datetime

some_date = datetime.datetime(2021, 6, 22, 13, 6, 44)

#Formating dictionaries
# 2021 June, 22
print('The date is {:%Y %B, %d}'.format(some_date))


fruits = ["apple", "banana", "orange"]

#Accessing list usings indexes
print("I am having these fruits in my basket {0[0]}, {0[1]}, {0[2]}".format(fruits))