s={1,2,3,4,45,6,66,1,2,3,34,}
#print(s)

l = [1,2,3,4,5,5,2,1,1,1,12,2,2,3,34,4]
s1= list(set(l))
#print(s1)

s.add(5)
s.add(5.5)
#print(s)

s.remove(5)
#print(s)

s.discard(10)
#print(s)

s.clear()
print(s)