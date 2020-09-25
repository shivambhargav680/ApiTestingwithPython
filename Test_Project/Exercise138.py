#odd_even = {num:('even' if num%2==0 else 'odd') for num in range(13,65)}
#print(odd_even,end="")


# Tables
"""num= int(input("Enter your numer: "))
for i in range(1,11):
    total = num*i
    print(f"{num}x{i}={total}")"""



# 2-10 Tables
#num= int(input("Enter your numer: "))
for num in range(2,11):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
    print('\n')

