# File: CS112_A1_T2_3_20231036.py
# Purpose: subtract a square game, in this game you should enter square numbers of coins only to subtract from a starting total and the player who removes the last coin wins
#you also should start the game with a non-square number of coins.
# Author: Passant Shaaban Abdelazim Mohamed
# ID: 20231036

#Main function
def subtract_square_game() :
    # define a function to check that the input number is a square number
    def square_number_check (player_one) :
        return player_one > 0 and (int(player_one**0.5))**2 == player_one
    def square_number_check (player_two) :
        return player_two > 0 and (int(player_two**0.5))**2 == player_two
    def square_number_check (coins) :
        return coins > 0 and (int(coins**0.5))**2 == coins

    # to be able to use the random option
    import random

    # showing the menu for users
    print("Welcome to subtracting squares game!")
    print("choose one option A , B or C  ")
    print("A) Random initial number of coins ")
    print("B) initial number of coins chosen By me")
    print("C) Exit game ")
    coins_option = input("choose one option ").upper()

    # option one
    if coins_option == "A" :
        coins = random.randint(10,1000)
        print("there are ", coins , "coin in the pile")
        while True:
            try:
                player_one = int(input("player one turn\n "))
            except ValueError :
                print("please enter a number")
                continue
            # Ensure play is correct and valid
            if (player_one <= coins) and square_number_check(player_one) and player_one > 0 :
                coins = coins - player_one
                # Update game status
                print("Now you have " , coins , " coin in the pile")
            else:
                # while loop till we get valid input
                while True:
                    try:
                        player_one = int(input("please enter a valid number \n"))
                    except ValueError :
                        continue
                    # Ensure play is correct and valid
                    if (player_one <= coins) and square_number_check(player_one) and player_one > 0 :
                        coins = coins - player_one
                        # update game status
                        print("Now you have " , coins , " coin in the pile")
                        break

            # determine the winner
            if coins == 0:
                print("congrats, player one is the winner!")
                # end game
                break

            # While true loop to be able to continue if the input is not a number
            while True :
                try:
                    player_two = int(input("player two turn \n"))
                    break
                except ValueError:
                    print("please enter a number")
                continue
            # Ensure play is correct and valid
            if (player_two <= coins) and square_number_check(player_two) and player_two > 0 :
                coins = coins - player_two
                # update game status
                print("Now you have " , coins , " coin in the pile")
            else:
                # while loop till we get valid input
                while True:
                    try :
                        player_two = int(input("please enter a valid number \n"))
                    except ValueError :
                        continue
                    # Ensure play is correct and valid
                    if (player_two <= coins) and square_number_check(player_two) and player_two > 0 :
                        coins = coins - player_two
                        # update game status
                        print ("Now you have " , coins , " coin in the pile")
                        break

            # determine the winner
            if coins == 0:
                print("congrats, player two is the winner!")
                # end game
                break

    # option two
    elif coins_option =="B":
        # while true loop to be able to continue if the input is not a number
        while True :
            try:
                coins = int(input("How many coins do you wanna begin with ? \n"))
                break
            except ValueError:
                print("please enter a number")
                continue

        while True:
            # check if total coins valid to the rules of the game
            if square_number_check(coins) :
                try :
                    coins=int(input("you shouldn't start with a square number of coins , please enter a valid number\n"))
                except ValueError :
                    continue
            else :
                break

        while True :
            try:
                player_one = int(input("player one turn\n "))
            except ValueError :
                print("please enter a number")
                continue
            # Ensure play is correct and valid
            if (player_one <= coins) and square_number_check(player_one) and player_one > 0 :
                coins = coins - player_one
                # update game status
                print("Now you have " , coins , " coin in the pile")
            else:
                # while loop till we get valid input
                while True:
                    try:
                        player_one = int(input("please enter a valid number \n"))
                    except ValueError :
                        continue
                    # Ensure play is correct and valid
                    if (player_one <= coins) and square_number_check(player_one) and player_one > 0 :
                        coins = coins - player_one
                        # update game status
                        print("Now you have " , coins , " coin in the pile")
                        break

            # determining the winner
            if coins == 0:
                print("congrats, player one is the winner!")
                # end game
                break

            # While true loop to be able to continue if the input is not a number
            while True :
                try:
                    player_two = int(input("player two turn \n"))
                except ValueError :
                    print("please enter a number")
                    continue
                # Ensure play is correct and valid
                if (player_two <= coins) and square_number_check(player_two) and player_two > 0 :
                    coins = coins - player_two
                    # update game status
                    print("Now you have " , coins , " coin in the pile")
                    break
                else :
                    # while loop till we get a valid input
                    while True:
                        try :
                            player_two = int(input("please enter a valid number \n"))
                        except ValueError :
                            continue
                        # Ensure play is correct and valid
                        if (player_two <= coins) and square_number_check(player_two) and player_two > 0 :
                            coins = coins - player_two
                            # update game status
                            print("Now you have " , coins , " coin in the pile")
                            break
                break

            # determine the winner
            if coins ==0:
                print("congrats, player two is the winner!")
                # end game
                break

    # option three
    elif coins_option == "C" :
        print("Thanks for using my program")
        while True :
            # end game
            break

    else :
        print("please input a valid choice")

while True :
    subtract_square_game()
