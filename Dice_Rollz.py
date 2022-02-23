def Dice_rollz():
    import random

    min = 1
    max = 6

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        user = random.randint(min, max)
        computer = random.randint(min, max)
        print("Rolling the dices...")
        print("ur value is", user)
        print("the computer value is", computer)

        if user > computer:
            print("ur amount is bigger congrats(thats what she said)")
        elif user == computer:
            print("amount is sem lol")
        else:
            print("the computer's value is bigger ur trash lol")

        roll_again = input("You wanna roll le dice again?")