import random

winning_number = random.randint(0,100)
guess = 1
number = int(input(" Gusse number between 1 and 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"You win, Gussing count is {guess}")
        game_over = True
    else:
        if number > winning_number:
            print("Too High")
        else:
            print("Too low")
        # input again
        guess += 1
        number = int(input("Guess again : "))