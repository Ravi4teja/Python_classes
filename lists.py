#List Creation
countries = ['US', 'India', 'UK', 'Canada']
print(countries)

#Accessing List element
print(countries[2])

nums = [2, 4, 6, 9]

print(nums[2])

#Accessing List element by negative index
print(nums[-1])
print(countries[-2])

#Find the length of list
print(len(countries))

#Use Slicing and extract various elements from list
print(countries[1:3])
print(countries[:2])

print(countries[2:])

#Insert another element to the end of list
countries.append("Newzealand")

print(countries)

# countries.append(["Pak", 'Afganistan'])

# print(countries)

#Insert more than one element to the end of list
countries.extend(["Pak", 'Afganistan'])

print(countries)

#Insert element at particular index
countries.insert(2, "Australia")

print(countries)

#Remove an element from List
countries.remove("Pak")

print(countries)

#removing last element from the List and assigning it to the another variable
othercountry = countries.pop()

print(othercountry)
print(countries)

#reverse the order of elements in the list
countries.reverse()
print(countries)

#Sorting the elements in the list
countries.sort()

print(countries)

num2 = [9, 3, 4, 2]

# num2.sort()
print(num2)

#sorting and returing sorted list
num3 = sorted(num2)

print(num3)

#sorting in decending order and returing sorted list
num4 = sorted(num2, reverse=True)

print(num4)

#Maximum value in the list
print(max(num2))

#Minimum value in the list
print(min(num2))

#Addition of all the values in the list
print(sum(num2))

#Finding the index of the value in the list
print(countries.index('Canada'))

countries.append("Canada")

print(countries)

#Count the number of times the value repeated
print(countries.count('Canada'))

print(countries.count('Mexico'))

#Insert the list elements to another list
countries = countries + ['Mexico', 'westindies']

print(countries)

#checking the element present in the list
print('UK' in countries)

sentence = "Krish is going to park"

#Covert the string into list based on space
sentenceList = sentence.split()

print(sentenceList)

fruitstring = "orange,apple,banana"

#Covert the string into list based on ",". we can use other string to split
fruitList = fruitstring.split(",")

print(fruitList)

#join the list with specified string/character. we can give what ever we want.
countriesString = '-'.join(countries)

print(countriesString)

#changing the element in the index
countries[1] = "Bangladesh"

print(countries)

names = ['Ravi', 
            ['Sreya',
            ['santosh', 'kishore'], 
            'Krish'], 
        'Sireesha']

#accessing the nested list
print(names[1][1][1])

#Creating empty list
list1 = []

list1.append('something')

#Creating empty list
list2 = list()

list2.append('something')

print(list1)
print(list2)






