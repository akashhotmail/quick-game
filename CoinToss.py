def coinToss():
    from random import randrange
    repeat = 'Yes'
    while repeat == 'Yes':
        #Betting
        coin_list = ['Heads', 'Tails']
        user_bet = input('Hey user, do you want to choose head or the tails ')
        computer_bet = 0
        if user_bet == 'Heads':
            computer_bet = 'Tails'
        else:
            computer_bet = 'Heads'
        #Tossing
        i = randrange(len(coin_list))
        item = coin_list[i]
        # Select item using index number
        print("The coin landed on", item)

        if item == user_bet:
            print('You won!! good job buddy now get a life')
        else:
            print('The computer won :(')

        repeat = input('Do you want to play againn? Say Yes or No')







