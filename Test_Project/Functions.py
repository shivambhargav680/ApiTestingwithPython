#def add_three(a,b,c):
#    return a+b+c

#print(add_three(2,3,5))


def greater_num(a, b):

    if a > b:
        return "a is greater then b"
    elif b > a:
        return "b is greater then a"
    else:
        print("Numbers are equals ")

#num_a = int(input("Enter number a = "))
#num_b = int(input("Enter number b = "))

#bigger = (greater_num(num_a,num_b))
#print(bigger)

def greatest(a,b,c):
    if a>b and a>c:
        return "a is bigger"
    elif b>a and b>c:
        return "b is bigger"
    elif c>a and c>b:
        return "c is bigger"
    else:
        print("All three numbers are equals")
#num_a = int(input("Enter number a = "))
#num_b = int(input("Enter number b = "))
#num_c = int(input("Enter number c = "))
#bigger = greatest(num_a,num_b,num_c)
#print(bigger)


def new_greater(a,b,c):

    bigger = greater_num(a,b)
    return greater_num(bigger)

print(new_greater(19,2,3))