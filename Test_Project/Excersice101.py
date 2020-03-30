'''def odd_even(l):
    odd_nums=[]
    even_nums=[]
    for i in l:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums,even_nums]
    return output

numbers = [1,2,3,4,5,6,7,8,9]
print(odd_even(numbers))'''

# Two lists
def two_list_find(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

list1 = [1,2,4,51,43]
list2 = [1,2,4,56,8]
print(two_list_find(list1,list2))


def min_max(l1,l2):
    diff = max(l1)-min(l2)
    return diff


print(min_max(list1,list2))