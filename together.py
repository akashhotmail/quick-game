from CoinToss import coinToss
from Dice_Rollz import Dice_rollz
from rock_paper_scissors import Rock_Paper_scissors
from three_cards import three_cards
while True:
    you_wanna_play = input("Do you want to play some games? ")
    if you_wanna_play == "n":
        break
    else:
        which_game = input("Which game do you want to play(dice_roll, RPS, three_cards, coin_toss)? ")
        if which_game == "n":
            break
        elif which_game == "dice_roll":
            Dice_rollz()
        elif which_game == "RPS":
            Rock_Paper_scissors()
        elif which_game == "three_cards":
            three_cards()
        elif which_game == "coin_toss":
            coinToss()
        else:
            break