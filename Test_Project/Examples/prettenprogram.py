'''n = int(input("Enter number of rows : "))

# Nested for loop
for i in range(n):
    for j in range(n):
        if j == 0 or i == (n-1) or i == j:
            print("*",end = "")
        else:
            print(end = " ")
    print()'''

string = input("Enter string : ")
length = len(string)

for row in range(length):
    for col in range(row+1):
            print(string[col], end="")
    print()
