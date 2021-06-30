#Sets are collection of elements with no duplicates
#only unique values

numset = {3, 6, 1, 9, 2, 1, 6}

stringSet = {"kamal", 'ram', 'syam', 'ram'}

print(numset)

print(stringSet)

names1 = {"Krish", 'Sreya', "Ram", "Syam"}

names2 = {"Keerthi", "Ram", "Kishore"}

#Returns the elements in the list which are different than other set
print(names1.difference(names2))

#Returns the common elements in the two sets
print(names1.intersection(names2))

#Combines all the elements in the two strings and returns the unique elements.
print(names1.union(names2))
