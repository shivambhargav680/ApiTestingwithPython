'''num = input("Enter number: ")
total = 0
i=0
while i < len(num):
    total += int(num[i])
    i += 1
print(total)
'''


name =input("Enter Your Name: ")
temp_var = ""
i=0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i+=1


