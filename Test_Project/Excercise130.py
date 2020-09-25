def reverse_string(l):
    return [name[::-1] for name in l]

print(reverse_string(['abc','bfg']))

def reverse_list1(l):
    reverse_list = []
    for i in l:
        reverse_list.append(i[::-1])
    return reverse_list

print(reverse_list1(['abc','bfg']))


