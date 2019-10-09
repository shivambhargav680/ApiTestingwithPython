list1 = ["burger","Pizza","Burger with cheese"]

print(list1)

firstinpur = input()

#print(firstinpur)
for i in range(0,3):

    def burger():
        burger = 50
        tip = 50*0.2
        tax = 50*0.18
        total = burger+tip+tax
        print("Please pay "+total+" for your burger")

    def pizza():
        pizza = 250
        tip = 50*0.2
        tax = 50*0.18
        total = pizza+tip+tax
        print("Please pay " + total + " for your pizza")


    def burgerwithcheese():
        cheeseburger = 100
        tip = 50*0.2
        tax = 50*0.18
        total = cheeseburger+tip+tax
        print("Please pay " + total + " for your burger with cheese")



