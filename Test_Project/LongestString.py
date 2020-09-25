# Python program to find the length of the longest substring
# without repeating characters
"""
string = 'abcdbcbb'
n = len(string)
s = 0
start = 0
maxlen = 0
storeval = {}
storeval[string[0]]=0

for i in range(1,n):
    if string[i] not in storeval:
        #print({string[i]})
        #print(storeval)
        storeval[string[i]] = i
        #print(i)
    else:
        if storeval[string[i]] >= s:
            curlen = i-s
            #print(curlen)
            if maxlen<curlen:
                maxlen=curlen
                start=s
            s=storeval[string[i]]+1
            #print(s)
        storeval[string[i]] = i
        #print(storeval[string[i]])
if maxlen<i-s:
    maxlen= i-s
    start=s
print(string[start:start+maxlen])
"""


def longest_sublist(string):
    n = len(string)
    val1 = set()
    for i in range(0,n):
        val1.add(string[i])
    return len(val1)
print(longest_sublist(input("Enter your string : ")))