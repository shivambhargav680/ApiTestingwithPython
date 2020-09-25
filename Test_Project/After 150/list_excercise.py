name = 'olololHello'
replaceword = ''
char = 'l'
final = ''
for i in range(len(name)):
    if name[i] == char:
       replaceword = name.replace('l','o')
print(replaceword)
for j in range(len(replaceword)):
    final += name[j]
print(final)


#min number

def minnumber(items):
    num = min(items)
    return num
print(minnumber([1,0,3,-6,-6]))