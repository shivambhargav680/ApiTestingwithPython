

#interest = int((p*r*t))/100


"""def interest_rate(p,r,t):
    rate=(p*r*t)/100
    return rate

print(interest_rate(5000,8.5,2))"""

num = int(input("Enter number"))
for i in range(5):
    if num == 1:
        print("Poor")
        break
    elif num == 2 or 3:
        print("Average")
        break
    elif num == 4 or 5:
        print("Awesome")
        break
    else:
        print("You enter incorroct number")
