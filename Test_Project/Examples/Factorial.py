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
for i in range(n,0,-1):
    result = result*i

print(result)