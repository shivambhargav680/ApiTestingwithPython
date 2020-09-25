#num = int(input('Enter your number')

def lop (num):
    i = num
    result = 0
    n = len(str(num))
    while(num!=0):
        digit = num%10
        result = result+digit**n
        num = num//10
    com(i,result)

def com(i,result):
    if i == result:
        print(f'Numer {i} is an armstrong number')
    else:
        print(f'Numer {i} is not an armstrong number')

for num in range(101):
    lop(num)