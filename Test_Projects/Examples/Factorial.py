"""
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


n = int(input("Enter factorial number : "))
result = fact(n)
print(result)
"""

n = int(input("Enter fact number : "))
result = 1
if n==0:
    print("Invalid number")
else:
    for i in range(n,0,-1):
        result = result*i
    #print(result)
cont=0
temp = []
num = str(result)
for i in range(len(num)):
    if num[i]=='0':
        #print(num[i])
        cont +=1
#print(cont)
temp.append(num[i])
print(temp[0])





