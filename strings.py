
name = "Sreya"
name2 = "Krish"

print (name + name2)

sentence = """Hi,Good morning!
how are you.
"""


sentence = '''Hi, Good Evening!
how are you.
'''

print(sentence)

#find the number of characters in a string
print(len(name))

#capi
print(name.upper())
print(name2.lower())

print("ravi teja is giving lession".title())
print("ravi teja is giving lession".capitalize())

#type() function used to get the type of the variable
print(type(name))

num1 = 4

print(type(num1))
dec1 = 5.97

print(type(dec1))

# returns list of the attributes and methods of any object
print(dir(str))

# The python help function is used to display the documentation of modules, functions, classes, keywords etc.
print(help(str.upper))

# \n - new line character
# \t - tab 
# \b - backspace
print("Hi,  I am doing good. \nHow are you doing")
print("Hi,  I am doing good.\tHow are you doing")
print("Hi,  I am doing good.\bHow are you doing")


print(name, name, name, name)

#For printing multiple times
# print(100*name)

#Slicing
print(name[1])
print(name2[0:3]) # print(name2[:3])
print(name2[2:])

print(name[2:4])

quote = "Everyday is pleasant day"

#Used to find the index of first occurance of substring in a main string.
print(quote.find('pleasant'))

#Used to get the index of first occurance of letter in a main string.
print(quote.index('a'))

#Used to get the index of last occurance of letter in a main string.
print(quote.rindex('a'))

#used to replace the substring with another value but it will not replace in the main string.
print(quote.replace('pleasant', 'great'))

print(quote)

#replace and assign.
quote = quote.replace('pleasant', 'great')

print(quote)

message1 = "      Hello what are doing    "
# used to remove all the leading and trailing spaces from a string. 
print(message1.strip())
print(message1)
message1 = message1.strip()
print(message1)

#check whether the string starts with the given value.
print(name.startswith('Sr'))
print(name2.startswith('Sr'))

#count the number of occurances of substring in main string.
print("hi how are you hi what are you doing".count('e'))

#check whether the given string has all lowercase characters.
print('Hello'.islower())

numstring = "45263"

#check whether the given string has all numbers.
print(numstring.isnumeric())

numstring2 = "232raja"

print(numstring2.isnumeric())


person = "Ravi"
person2 = "Krish"
work="Cricket"
work2 = "Music"


#String Formating
sentence= "{} is going to play {}".format(person, work)
# sentence2 = "Krish is going to play music"
sentence2= "{} is going to play {}"

print(sentence)
# print(sentence2)

print(sentence2.format(person2, work2))

person3="Sreya"
work3="chess"

#F-strings
sentence3 = f"{person3} is going to play {work3}"
print(sentence3)





