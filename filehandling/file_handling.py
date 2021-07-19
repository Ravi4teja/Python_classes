#File Handling -  Create, Accessing and modifying the File

#Opening file
#If we dont specify the mode.Python will take read mode 'r' by defauly
f_handler = open("test.txt")

# #Modes
# # r -read
# # w - write
# # a - append
# # r+ - read and write

#To get the name of the file you are accessing
print(f_handler.name)
#To get the Mode you used to open the file
print(f_handler.mode)

#To read the contents of the file
filetext  = f_handler.read()

print(filetext)

#To close the file you opened using open() method
f_handler.close()

#Opening a file using Context Manager
with open("test.txt") as f_handler2:
    filetext2 = f_handler2.read()

print(filetext2)

#Using a to append the text to the existing file content
with open("test.txt", "a") as f_handler3:
    f_handler3.write("Hello world")

with open("test.txt", "r") as f_handler4:
    f = f_handler4.read()
    print(f)


with open("test.txt", "r") as f_handler4:
    #To extract each line in to an element in the list
    f = f_handler4.readlines()
    print(f)

    #Extracting the file contents through file handler using loop
    for i in f_handler4:
        print(i, end="")

    #To extract the part of the file content
    f = f_handler4.read(150)
    print(f)

#Using w mode to override the contents of the file
with open("test2.txt", "w") as f_handler5:
    #writing into the file
    f_handler5.write("Hi All")
    #Placing the curser a particalar place using seek() method
    f_handler5.seek(4)
    f_handler5.write("Good Morning")


#Using context manager to copy the contents from one file to another file.
with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as rwf:
        for line in rf:
            rwf.write(line)

#Using context manager to copy the image file. 
with open("teddy.jpg", "rb") as rf:
    with open("teddy2.jpg", "wb") as rwf:
        for line in rf:
            rwf.write(line)