# Coin Matcher
# Dan Soloha
# 10/15/2019

from random import randint

class Coin(object):
    """A coin that can be tossed by a player"""

    def __init__(self, amount = 20):
        self.amount = amount
        self.__sideup = None

    def toss(self):
        toss = randint(0, 1)
        if toss == 0:
            self.__sideup = "heads"
        else:
            self.__sideup = "tails"

    def get_amount(self):
        return(self.amount)

    def set_amount(self, new_amount):
        if new_amount >= 1:
            new_amount = 1
        else:
            new_amount = -1
        self.amount += new_amount

    def get_sideup(self):
        return self.__sideup
        


def again():
    """Asks the user if they would like to play again"""
    again = input("Would you like to play again? Enter 'y' or 'n'. ")
    while again.lower() not in ("y", "n"):
        again = input("Please enter either 'y' or 'n'. ")
    if again == "y":
        return True
    else:
        return False

def total(player):
    """Returns the player's total"""
    return player.get_amount()

def main():
    """Main game loop"""
    play = True
    print("Welcome to Coin Toss! The rules are simple: if both coins land on the same side, Player 1 wins. Otherwise, Player 2 wins. ")
    player1 = Coin()
    player2 = Coin()

    while play is True:

        input("Press 'enter' to toss the coin. ")
        player1.toss()
        player2.toss()

        if player1.get_sideup() == player2.get_sideup():
            player1.set_amount(1)
            player2.set_amount(-1)
            print(f"They're both {player1.get_sideup()}. Player 1 wins! ")
        else:
            player1.set_amount(-1)
            player2.set_amount(1)
            print(f"Player 1 is {player1.get_sideup()} and Player 2 is {player2.get_sideup()}. Player 2 wins! ")
        print(f"Player 1 has a total of {total(player1)} and Player 2 has a total of {total(player2)}. ")

        play = again()
        
    print("Thanks for playing! ")



if __name__ == "__main__":
    main()
