#A Module is the file which consists of Python Code.

print("Importing my_module...")

sentence = "This is a variable in my_module"

def find_index(sequence, element):
    i = 0
    for item in sequence:
        if item == element:
            return i
        i = i + 1
    return False
    

# list1 = ["hi", "Hello", "How", "Who"]

# find_index(list1, "ROOM")



# def fun_1():
#     print("Hi Raving")
#     return
#     print("This is another part")
#     print("This will not execute")

# fun_1()
