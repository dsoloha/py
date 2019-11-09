# Tip Calculator
# Dan Soloha
# 9/12/2019

total = int(input("What was the total your bill came to? "))
print(f"With a total of {total}, you should tip ${int(total + (total * 0.15))}. If the waiter did a really good job, you should tip ${int(total + (total * 0.20))}. ")  # Multiplying by 1.x was returning the number rounded down for some reason