

def three_cards():
    import random
    print("This be a 3 cards game. You will get three cards at random.")
    player_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    computer_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    player_card1 = random.choice(player_cards)
    player_card2 = random.choice(player_cards)
    player_card3 = random.choice(player_cards)
    computer_card1 = random.choice(computer_cards)
    computer_card2 = random.choice(computer_cards)
    computer_card3 = random.choice(computer_cards)
    if player_card1 == "Jack":
        player_card1 = 11
    if player_card1 == "Queen":
        player_card1 = 12
    if player_card1 == "King":
        player_card1 = 13
    if player_card1 == "Ace":
        player_card1 = 14
    if computer_card1 == "Jack":
        computer_card1 = 11
    if computer_card1 == "Queen":
        computer_card1 = 12
    if computer_card1 == "King":
        computer_card1 = 13
    if computer_card1 == "Ace":
        computer_card1 = 14
    sep = ","
    last = "and"
    period = "."
    ex_mark = "!"
    computer_score = 0
    player_score = 0
    print("We will now show you your cards. Here they are:",player_card2,"of spades",sep,player_card3,"of spades",last,player_card1,"of spades",period)
    print("The first round will now commence.")
    which_card = [player_card1, player_card2, player_card3]
    idk_what_to_call = random.choice(which_card)
    print("First round: You put", idk_what_to_call, "of spades and the computer put", computer_card1, "of clovers.")
    if computer_card1 > player_card1:
        print("Unfortunately, it looks like the computer won this round. You lose!")
        computer_score += 1
        player_score = 0
    if player_card1 > computer_card1:
        print("Nice! It looks like you won this round!")
        player_score += 1
        computer_score = 0
    if computer_card1 == player_card1:
        print("Whoa! It looks like the computer put", computer_card1, "and the player put", idk_what_to_call,"!", "It's a tie!")
    you_wanna_go_on_round_dos = input("Do you wish to go on to the second round? ")
    if you_wanna_go_on_round_dos == "no" or you_wanna_go_on_round_dos == "nah" or you_wanna_go_on_round_dos == "im good":
        print("Okay, have a nice life!")
    if you_wanna_go_on_round_dos == "yes" or you_wanna_go_on_round_dos == "ye" or you_wanna_go_on_round_dos == "sure":
        print("The second round will now commence.")
        if player_card2 == "Jack":
            player_card2 = 11
        if player_card2 == "Queen":
            player_card2 = 12
        if player_card2 == "King":
            player_card2 = 13
        if player_card2 == "Ace":
            player_card2 = 14
        if computer_card2 == "Jack":
            computer_card2 = 11
        if computer_card2 == "Queen":
            computer_card2 = 12
        if computer_card2 == "King":
            computer_card2 = 13
        if computer_card2 == "Ace":
            computer_card2 = 14
        which_card_round_dos = [player_card2, player_card3]
        idk_what_to_call_round_dos = random.choice(which_card_round_dos)
        print("We will now show you your two cards in case you forgot. Here they are:", player_card3," of spades",last,player_card2," of spades",period)
        print("Second round: You put" ,idk_what_to_call_round_dos, "of spades, and the computer put",computer_card2,"of clovers.")
        if player_card2 < computer_card2:
            print("Unfortunately, it looks like the computer won this round. You lose!")
            computer_score += 1
        if player_card2 > computer_card2:
            print("Nice! It looks like you won this round!")
            player_score += 1
        if computer_card2 == player_card2:
            print("Whoa! It looks like the computer put", computer_card2, "and the player put", player_card2, ex_mark, "It's a tie!")
            player_score += 0
            computer_score += 0
        you_wanna_go_on_round_tres = input("Do you want to continue to round three? ")
        if you_wanna_go_on_round_tres == "no":
            print("Okay, have a nice life!")
        if you_wanna_go_on_round_tres == "yes" or you_wanna_go_on_round_tres == "sure":
            print("The third round will now commence.")
            if player_card3 == "Jack":
                player_card3 = 11
            if player_card3 == "Queen":
                player_card3 = 12
            if player_card3 == "King":
                player_card3 = 13
            if player_card3 == "Ace":
                player_card3 = 14
            if computer_card3 == "Jack":
                computer_card3 = 11
            if computer_card3 == "Queen":
                computer_card3 = 12
            if computer_card3 == "King":
                computer_card3 = 13
            if computer_card3 == "Ace":
                computer_card3 = 14
            print("We will now show you your last card in case you forgot:", player_card3, "of spades.")
            print("Third round: You put",player_card3,"of spades and the computer put", computer_card3, "of clovers.")
            if player_card3 < computer_card3:
                print("Unfortunately, it looks like the computer won this round. You lose!")
                computer_score += 1
            if player_card3 > computer_card3:
                print("Nice! It looks like you won this round!")
                player_score += 1
            if computer_card3 == player_card3:
                print("Whoa! It looks like the computer put",computer_card3,"and the player put",player_card3,ex_mark,"It's a tie!")
                print("We will now show you the results for this game.")
                print("Here it is:", player_score, computer_score)
            if player_score > computer_score:
                print("Outstanding! You won the entire game!")
            if computer_score > player_score:
                print("Unfortunately, the computer won these three rounds. Try again next time.")