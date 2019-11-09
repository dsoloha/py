# Simple Calculator
# Dan Soloha
# 10/8/2019

import circle as c
import rectangle as r

abort = True

def again():
	u = input("Would you like to find something else? (y/n) ")
	while u.lower() not in ('y', 'n'):
		u = input("Please answer 'y' or 'n'. ")
	if u == 'y':
		return True
	else:
		return False

#  very messy but it works
print("Welcome to the Simple Calculator. Use 1 - 4 to select an option, or press ESC at any time to exit. ")
while abort is True:
	user_input = int(input("""
What shape would you like to use?
1	Circle
2	Rectangle
"""))

	if int(user_input) == 1:
		user_input = int(input("""
What would you like to find?
1	Area
2	Circumfrence
"""))
		radius = input("What is the radius of the circle? ")
		if user_input == 1:
			print(c.area(float(radius)))
			abort = again()
		elif user_input == 2:
			print(c.circumfrence(float(radius)))
			abort = again()
	elif int(user_input) == 2:
		user_input = int(input("""
What would you like to find?
1	Area
2	Perimeter
"""))
		width = input("What is the width of the rectangle? ")
		height = input("What is the height of the rectangle? ")
		if user_input == 1:
			print(r.area(float(width), float(height)))
			abort = again()
		elif user_input == 2:
			print(r.perimeter(float(width), float(height)))
			abort = again()
