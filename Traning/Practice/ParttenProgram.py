# Tutorial 104


'''def finder(l1,l2):
    outlist=[]
    for i in l1:
        if i in l2:
            outlist.append(i)
    return outlist


list1 = [1,2,23,4,5,6,7,8,9]
list2 = [3,4,2,8,9,11,22,344]

print(finder(list1,list2))'''


'''n = int(input("Enter number range: "))
for row in range(0,n):
    for col in range(0,n):
        if row ==0 or col ==n-1 or row==col:
            print("#", end="")
        else:
            print(end=" ")
    print()'''



'''n = int(input("Enter numeber : "))
6
num=1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num=num+1
    print()'''

'''s = input("Enter string : ")

lenth = len(s)

for row in range(lenth):
    for col in range(row+1):
        print(s[col],end='')
    print()'''

for row in range(0,4):
    for i in range(2,0,-1):
        print(i,end=" ")
    print()