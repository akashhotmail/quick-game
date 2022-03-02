def Rock_Paper_scissors():
    import random


    print("What do you want to pick? Rock(1), Paper(2), or Scissors(3)")
    player = int(input())


    mylist = ["rock", "paper", "scissors"]

    computer = random.choice(mylist)
    print(computer)

    if player == 1:
        print("rock(your choice)")
    elif player == 2:
        print("paper(your choice)")
    elif player == 3:
        print("scissors(your choice)")


    if player == 1 and computer == "scissors":
        print("You won!")
    elif player == 2 and computer == "rock":
        print("You won!")
    elif player == 3 and computer == "paper":
        print("You won!")
    elif player == 1 and computer == "paper":
        print("You lost  L  ")
    elif player == 2 and computer == "scissors":
        print("You lost  L  ")
    elif player == 3 and computer == "rock":
        print("You lost  L  ")
    elif player == 1 and computer == "rock":
        print("You tied")
    elif player == 2 and computer == "paper":
        print("You tied")
    elif player == 3 and computer == "scissors":
        print("You tied")












