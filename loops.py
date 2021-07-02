
#We use Loops to do repeated tasks.

#While Loop
num = 0
while(num<10):
    print(num)
    num = num + 1


# while True:
#     print("This is infinite Loop")

nums = [1, 4, 7, 2, 3]

#We use for loop to iterate through the list/tuples/dictionaries/sets or any collection of elements.
for num in nums:
    print(num)

print("-------------")

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
for i in range(10):
    print(i)

#We can 
for i in range(3, 10):
    print(i)


print("-------------")
#break , continue
#We use "break" to break the loop when ever needed.
for i in range(10):
    if i == 6:
        break
    print(i)

print("-------------")

#We use "continue" to return the control to the beginning of the loop. 
for i in range(10):
    if i == 6:
        continue
    print(i)
    print("This is continue")

#Loop and else. When ever the loop ended or became false then else part will execute.
x = 0
while(x < 7):
    print(x)
    x = x + 1
else:
    print("This is greater than 7")


for i in nums:
    print(i)
else:
    print("Loop ended")

# print(list(range(10)))
