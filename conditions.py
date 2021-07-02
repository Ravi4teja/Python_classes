
if False:
    print("Hello this is True")

name1 = "Krish"
if name1 == "Krish":
    print("Yes")

if name1 == "Sreya":
    print("Yes")

age = 21
if name1 == "Krish":
    if age == 12:
        print("He is Krish of age 12")

if age < 20:
    print("He may be studying")
else:
    print("He may be working")

num1 = 6

if num1 < 6:
    print("This is Less than 6")
elif num1 == 6:
    print("This is equal to 6")
else:
    print("This is greater than 6")


result = "Pass"
Percentage = 72

# if result == "Pass":
#     if Percentage >= 70:
#         print("The Person got distinction")

#Using "and" operator. "if" condition will be True only when both the conditions before and after the "and" operator is True.
if result == "Pass" and Percentage >= 70:
    print("The Person got distinction")
else:
    print("He missed it")

PercentageineachSubject = 33
result = "Pass"

#Using "or" operator. "if" condition will be True when "anyone or both" of the conditions before and after the "or" operator is True.
if result == "Pass" or PercentageineachSubject >35:
    print("The Person is Pass, cleared all Subjects")

#Using "not" operator. "not" oprator makes False to True. True to False.
if not False:
    print("This is also True")

a = [1, 2, 3]
b = [1, 2, 3]

#Checking both elements have same values.
print(a == b)

#Checking both elements are same object.means both elements share the same memory address.
print(a is b)

#id() method will give the address of the object
print(id(a))
print(id(b))

#if you directly assign the element to another element. Then they both share the same memory address. and basically they both elements are same object.
c = a

print(id(c))
print(c is a)

#Below are the list of False.
# False, None, 0, '', "", (), [], {}

if {}:
    print("This is True")
else:
    print("This is False")

#Any value other than False statements are True.
if {'a': 30}:
    print("This is True")
else:
    print("This is False")





