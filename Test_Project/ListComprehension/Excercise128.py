"""
list1 = []
for i in range(0,11):
    list1.append(i**2)
print(list1)

list2 = print([i**2 for i in range(0,11)])
"""
"""
negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

new_nagative = print([-i for i in range(1,11)])
"""

names = ['Shivam', 'hitesh', 'monu', 'geeta']
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)


new_list2 = print([name[0] for name in names])