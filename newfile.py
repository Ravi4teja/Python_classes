#####importing  module
# import my_module

# print(my_module.sentence)


# countries = ["UK", "US", "India", "Canada", "France"]

# result = my_module.find_index(countries, "India")

# print(result)

#imporing functions, variables from module
from my_module import find_index, sentence

countries = ["UK", "US", "India", "Canada", "France"]
result = find_index(countries, "Canada")

print(result)

print(sentence)