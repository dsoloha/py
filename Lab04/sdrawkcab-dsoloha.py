# Backwards-izer
# Dan Soloha
# 9/12/2019

word = input("Welcome to the Backwards-izer! Enter the word you would like to make backwards. Press \"enter\" at any time to exit. ")

while word != "":
    reversed_word = list(reversed(word))
    reversed_word = "".join(reversed_word)
    word = input(f"{reversed_word} ")