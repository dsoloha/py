# Alien Wars
# Dan Soloha
# 10/23/2019

import games
from games import Player

class Hero(Player):
    """The player character"""
    def __init__(self, name = "Arnold"):
        self.name = name
        self.health = 10
        self.shield = 10
        self.life = 1

    def blast(self, target):
        from random import randint
        chance = randint(1, 10)
        if chance > 4:
            target.die()
            return True
        return False

    def die(self):
        self.health -= 2

class Alien(Player):
    """An alien character"""
    def __init__(self, name="Zxblrb"):
        self.name = name
        self.health = 10
        self.shield = 10
        self.life = 1

    def blast(self, target):
        from random import randint
        chance = randint(1, 10)
        if chance > 4:
            target.die()
            return True
        return False

    def die(self):
        self.health -= 2

def main():
    print("Welcome to Alien Wars!")
    play_again = None
    while play_again != "n":
        goes_first = games.ask_yes_no("Would you like to go first? (y/n) ")
        player = Hero()
        enemy = Alien()
        turn = None
        if goes_first == "y":
            input("Press enter to fire at the alien. ")
            if player.blast(enemy) == True:
                print("You hit the alien!")
            else:
                print("You missed!")
            print("The alien has", enemy.health, "health left. ")
            turn = enemy
        else:
            if enemy.blast(player) == True:
                print("The alien hit you!")
            else:
                print("The alien missed!")
            print("You have", player.health, "health left.")
            turn = player
        while player.health > 0 or enemy.health > 0:
            if turn == player:
                input("Press enter to fire at the alien. ")
                if player.blast(enemy) == True:
                    print("You hit the alien!")
                else:
                    print("You missed!")
                print("The alien has", enemy.health, "health left. ")
                turn = enemy
            else:
                if enemy.blast(player) == True:
                    print("The alien hit you!")
                else:
                    print("The alien missed!")
                print("You have", player.health, "health left.")
                turn = player
        if player.health > 0:
            print("Congratulations! You won!")
        else:
            print("Unfortunately, you lost. Better luck next time!")
        play_again = games.ask_yes_no("Would you like to play again? (y/n) ")

if __name__ == "__main__":
    main()
