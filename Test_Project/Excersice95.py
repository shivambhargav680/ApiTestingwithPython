
'''
def square(num):
    li = []
    for i in num:
        li.append(i**2)
    return li

num1 = int(input("Enter number : "))
num = list(range(num1))
print(square(num))
'''

"""
def reverseList(l):
    l.reverse()
    return l
lst = [1,2,3,4]
print(reverseList(lst))

"""
"""
def slcing(l):
    return l[::-1]
lst = [1,2,3,4]
print(slcing(lst))

"""


def reverList(l):
    r_List = []
    for i in range(len(l)):
        popped_item = l.pop()
        r_List.append(popped_item)
    return r_List
num = [1,2,3,4]
print(reverList(num))
