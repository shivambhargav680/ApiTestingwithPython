# Dictonary

str1 ='shivam bhargava'
count = {}
for char in str1:
    count[char] = str1.count(char)
#print(count)

# for loop

name = 'Shivam bhargava'#input("Enter your name : ")
temp = ''
for i in range(len(name)):
    st = name[i]
    num = name.count(name[i])
    if st not in temp:
        print(st,num)