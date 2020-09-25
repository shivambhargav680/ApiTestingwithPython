string = input("Enter your string : ")
replacedStr = ''
finalStr = ''
char = 'l'
for i in range(len(string)):
    replacedStr = string.replace(char,'o')
print(replacedStr)
for j in range(len(replacedStr)):
    finalStr += string[j]
print(finalStr)
