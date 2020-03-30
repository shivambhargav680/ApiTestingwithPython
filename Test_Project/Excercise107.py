lst1 = [123,[1,2,3,4,],[1,2,22,3,]]

def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

print(sublist_counter(lst1))


