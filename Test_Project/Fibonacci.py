'''

def fibonacci_seq(n):
    a=0 # first number
    b=1 # second number

    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a,b, end=" ")
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            print(b , end =" ")

fibonacci_seq(10)

'''

x=3
def func():
    global x
    x=8
    return x

print(x)
print(func())
