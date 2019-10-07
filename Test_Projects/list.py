
#inp_name = input("Enter your name : ")

#names = ["grapps" , "apple"]
#names.append(inp_name)
#print(names)


'''
fruits = ["grapps" , "apple"]
#fruits.insert(1, "grapps1")


fruits2 = ["Pinaapple", "litchi", "orange"]

fruits.append(fruits2)
#print(fruits2)
#print(fruits)

fruits.pop(1)
print(fruits)

'''

'''
fruits = ["Litchi","Grapps", "bananna", "mango", "kiwi"]
number = [3,4,53,2,235,6,7.8,8,8543,2,6]
#print(fruits.count("mango"))
#fruits.sort()
#print(fruits)
print(sorted(number))
'''


#Split method

#user_info = " shivam,bhargava".split(",")
#print(user_info)


#name , age = input("Enter your name and age ").split(',')
#print(name)
#print(age)

#join method

#user_info = ["shivam ", "26"]
#print(','.join(user_info))


#List in side list

#matrix = [[[11,22],1,2,3],[4,5,6],[7,8,9]]
#print(matrix[2])

#for sublist in matrix:
#     for i in sublist:
#        print(i)

#print(matrix[0][0][1])
#print(type(matrix))



#Range function


## number = list(range(1,29))

numbers = [1,2,3,4,5,6,7,7,78,9]
# print(number)
#print(number.pop())


#print(number.index(5))


def nagative_list(l):
    nagative =[]
    for i in l:
        nagative.append(-i)
    return nagative

print(nagative_list(numbers))