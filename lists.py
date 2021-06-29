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

num2.sort()
print(num2)



