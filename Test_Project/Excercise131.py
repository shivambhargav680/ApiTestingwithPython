def find_number(l):
    num =[]
    for i in l:
        if (type(i)==int or type(i)==float):
            print(str(i))

print(find_number([False,True,1,4,2.4,6.4]))


"""def find_num(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]

print(find_num([False,True,1,4,2.4,6.4]))"""
