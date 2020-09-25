'''total = 0
i=1
while i<=10:
    total+=i
    i+=1
    print(total,i)
'''

#Exc-1
'''
num = int(input("Enter number : "))
total=0
i=1
while i<=num:
    total+=i
    i+=1
    print(total,i) 
'''

# Tu-61

num = (input("Enter your num : "))
total =0
for i in range(0, len(num)):
    total += int(num[i])
print(total,i)