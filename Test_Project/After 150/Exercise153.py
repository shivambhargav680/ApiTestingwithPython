number = [1,2,3,4,5]

#simple square

"""def square(a):
    return a**2
new_list=[]
for num in number:
    new_list.append(square(num))
print(new_list)"""

#Square numbers with list comprehension

'''
new_list = [num**2 for num in number]
print(new_list)
'''

#Square with lambda expression

"""
ele_num = []
num = lambda a:a**2
for ele in number:
    ele_num.append(num(ele))
print(ele_num)"""


#Square with map function

def square(a):
    return a**2

#squares = list(map(square, number))

squares = list(map(lambda a:a**2,number))
#print(squares)

names = ['abc','abcd','abcdf']
length = list(map(len, names))
print(length)