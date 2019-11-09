# Car Salesman
# Dan Soloha
# 9/12/2019

price = int(input("How much did the car cost? "))

print("Sales tax here is 5.75%, and the license fee is 1.25%. The dealer charges $250 for prepping the car and a $800 destination charge.")
print(f"With all of these applied, your total comes to ${int(price + (price * 0.575) + (price * 0.125) + 250 + 800)}. ")