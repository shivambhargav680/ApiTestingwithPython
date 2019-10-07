import random

def ranNumber():
    usernum = int(input("Enter your lucky number: "))
    ran = random.randint(0,100)
    print(ran) == print(usernum)
    if usernum==ran:
        print("Your are amazing")
    elif usernum > ran:
        print("your are higher ")
    elif usernum <=ran:
        print("your number is low")
    print(ran,usernum )
ranNumber()