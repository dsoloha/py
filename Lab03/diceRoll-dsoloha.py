# Dice Roller
# Dan Soloha
# 9/12/2019

from random import randint

player_input = input("You have two die. Press enter at any time to roll them. Enter \"exit\" to exit. ")

while player_input != 'exit':
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)

    if dice1 + dice2 == 2:
        name = "Snake Eyes"
    elif dice1 + dice2 == 3:
        name = "Ace Caught a Deuce"
    elif (dice1 == 2 and dice2 == 2):
        name = "Little Joe from Kokomo"
    elif dice1 + dice2 == 5:
        name = "Little Phoebe"
    elif dice1 == 3 and dice2 == 3:
        name = "Jimmy Hicks from the Sticks"
    elif dice1 == 6 and dice2 == 1:
        name = "Six Ace"
    elif dice1 == 4 and dice2 == 4:
        name = "Eighter from Decatur"
    elif dice1 + dice2 == 9:
        name = "Nina from Pasadena"
    elif dice1 == 5 and dice2 == 5:
        name = "Puppy Paws"
    elif dice1 == 6 and dice2 == 5:
        name = "Six Five no Jive"
    elif dice1 + dice2 == 12:
        name = "Boxcar"
    else:
        name = ""

    if name != "":
        player_input = input(f"You rolled a {dice1} and a {dice2}. This is called a {name}. ")
    else:
        player_input = input(f"You rolled a {dice1} and a {dice2}. This doesn't have a special name. ")