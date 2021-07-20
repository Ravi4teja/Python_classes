# my_var = 50
try:
    f = open("some_thing.txt")
    print(f.read())
    list1 = ["Ravi", "Ram"]
    print(list1[2])
    # if:
    var1 = 1
except FileNotFoundError:
    print("This File does not exist")
except IndexError as e:
    print(e)
except Exception:
    print("This Variable not there!")
else:
    firstLine = f.readline()
    print(firstLine)
    f.close()
finally:
    print("Finally is excecuting.....")

age = 26
print(age)

var1 = 45
try:
    if type(var1) != "str":
        raise Exception
except Exception:
    print("This variable should be string")





