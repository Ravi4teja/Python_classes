#Polymorphism: It is an ability of object to behave in multiple form.
#Method overloading

def sum_of_nums(a, b, c=None, d= None):

    if (c is None) and (d is None):
        print(a + b)
    elif d is None:
        print(a + b + c)
    else:
        print(a + b + c +d)

sum_of_nums(5, 6)
sum_of_nums(9, 2, 1)
sum_of_nums(6, 3, 2, 8)

print("----------------")


class MathExpression:

    def sum_of_nums(self, a, b, c=None, d= None):

        if (c is None) and (d is None):
            print(a + b)
        elif d is None:
            print(a + b + c)
        else:
            print(a + b + c +d)

m1 = MathExpression()
m1.sum_of_nums(3, 4)
m1.sum_of_nums(3, 4, 9)
m1.sum_of_nums(3, 4, 2, 3)
