#Sum of numbers
def sumnumber(*args):
    number = 0
    for x in args:
        number += x
    return number

print(sumnumber(1,2,-3,-4,-5,6))

#Multiplication of numbers
def multiplication(*args):
    multinumber = 1
    for i in args:
        multinumber *= i
    return multinumber

print(multiplication(1,3,6))

