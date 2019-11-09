# The Useless Trivia Program
# Dan Soloha
# 9/12/2019

name = input("Hi. What's your name? ")
age = input("How old are you? ")
weight = input("Okay, last question. How many pounds do you weigh? ")

print(f"If poet EE Cummings were to email you, he'd address you as {name}. But if EE were mad, he'd call you {name.upper()}.\n")
print(f"If a small child were trying to get your attention your name would become: \n{name}{name}{name}{name}{name}.\n")
print(f"You're over {int(int(age) * 365.25 * 24 * 60 * 60)} seconds old. \n")
print(f"Did you know on the moon you'd weigh only {int(weight) * .165} pounds?")
print(f"On the sun you'd weigh {int(weight) * 27} (but, uh... not for long). ")

input("Press enter to exit. ")