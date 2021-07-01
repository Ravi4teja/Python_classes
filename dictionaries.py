#Dictionaries are Key Value Pairs

#Creating dictionary
student = {'name': 'Krish', 'age': 12, 'Subjects': ['Maths, Physics']}

print(student)

#Accessing the value through key
print(student['Subjects'])

#inserting new key-value pair
student['height'] = 4.5

#Updating the existing key-value pair
student['age'] = 13

print(student)

# print(student['movies'])
#Accessing the value through key with get() method
print(student.get('movies'))

print(student.get('movies', 'Not Found'))
print(student.get('age', 'Not Found'))

#Update the key-value pairs in the existing dictionary
student.update({'name': 'Sreya', 'age': 16, 'Subjects': ['Maths, Physics'], 'height': 4.8})

print(student)

#Deleting a key-value pair
del student['height']
print(student)

#Deleting a key-value pair and assigning the value to variable
SreyasAge = student.pop('age')

print(SreyasAge)
print(student)

#Creating the empty dictionary
dict1 = {}

dict1['work'] = 'Software'

#Creating the empty dictionary
dict2 = dict()

dict2['work'] = 'Software'

print(dict1)
print(dict2)



