# find value position
# abc = 0
# bcd = 1

names = ['abc','bcd','egf']
'''pos = 0
for name in names:
    print(f'{name} = {pos}')
    pos+=1'''

'''for pos,name in enumerate(names):
    print(f'{pos}={name}')'''



def postion_find(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
    return -1

print(postion_find(names,'abcdf'))
