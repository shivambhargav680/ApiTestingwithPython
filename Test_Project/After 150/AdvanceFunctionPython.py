"""def find (*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
"""

find = lambda *args:[sum(pair)/len(pair)for pair in zip(*args)]

l1 = [1,2,3,1]
l2 = [4,5,6,1]
l3 = [7,8,9,1]

print(find(l1,l2,l3))