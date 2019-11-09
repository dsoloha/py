# Number Guessing Game
# Dan Soloha
# 9/12/2019

from random import randint

print("Welcome to the Number Guessing game! The goal is simple: try to guess the number in the least number of guesses possible.")

num = randint(1, 100)
num_guesses = 0
guess = int(input("Guess a number between 1 and 100. "))
while guess != num:
    num_guesses = num_guesses + 1
    if guess > num:
        guess = int(input("That's too high. Guess lower. "))
    elif guess < num:
        guess = int(input("That's too low. Guess higher. "))

print(f"You got it! The number was {num}, and you guessed it in {num_guesses} guesses. Good job!")
input("Press enter to exit. ")

