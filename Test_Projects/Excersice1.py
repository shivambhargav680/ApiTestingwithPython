#name, age = input("Please enter your name or age ").split()
#print("Your name is {} and your age is {}".format(name,age))
#print(f"Your name is {name} your age is {age}")


#num1,num2,num3 = input("First number or second number or third number: ").split()
#num2 = int(input("First number second number third number"))
#num3 = int(input("First number second number third number"))
#avg = (int(num1)+int(num2)+int(num3))/3
#print(f"Average of three numbers is {(int(num1)+int(num2)+int(num3))/3}")

# Exercise
#name = input("Enter your name : ")
#print(name[-1::-1])


#Length
"""name = "ShIvAm BharGAVa"

print(len(name))

# Lower
print(name.lower())

# Upper
print(name.upper())

#Title
print(name.title())

#count
print(name.count("h"))
"""
#------------------------
#Tutorial 32
#username, letter = input("Enter username,letter").split(",")
#print(len(username))
#print(username.lower().count(letter.lower()))

#------------------------
#Tutorial 33
#name = "         Shivam Bhargav         "
#dots = "......................"
#lstrip method

#print(name.lstrip() + dots)
#print(name.rstrip() + dots)
#print(name.strip() + dots)
#print(name.replace(" ", ",")+ dots)


#---------------------------
#Tutorial 34
#string = "she is beautiful and intelegent also"
#print(string.replace("is","was"))


#---------------------------
#Tutorial 35
#name = "shivam"
#print(name.center(9,"#"))

#name2 = input("enter your name ")
#print(name.center(len(name)+9,"#"))


#---------------------------
#Tutorial 60
''''
num = int(input("Enter your number range : "))
total = 0
for i in range(1,num+1):
    total = total + i
    print(total,i)
'''

# Tutorial 68 Sum numbers 123 = 6
'''
num = input("Enter the num : ")
total = 0
for i in num:
    total += int(i)
print(total)
'''








