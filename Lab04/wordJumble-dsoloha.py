# Word Jumble
# Dan Soloha
#9/12/2019

import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
word = random.choice(WORDS)
correct = word
jumbled = ""

while word:
    position = random.randrange(len(word))
    jumbled += word[position]
    word = word[:position] + word[(position + 1):]

print("Welcome to Word Jumble! Unscramble the letters to make a word. Press enter at any time to quit. ")
playerInput = input(f"The jumble is \"{jumbled}\". ")

while playerInput != correct and playerInput != "":
    playerInput = input("Sorry, that's not right. Try again! ")

if playerInput == correct:
    print("That's correct! You got it! ")
    print("Thanks for playing!")