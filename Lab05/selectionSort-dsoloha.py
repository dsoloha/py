# Selection Sort
# Dan Soloha
# 9/24/2019

import random

unordered = list(range(10))
ordered = []
random.shuffle(unordered)

for i in range(len(unordered)):
    lowest = i
    for j in range(i+1, len(unordered)):
        if unordered[lowest] > unordered[j]:
            lowest = j

    unordered[i], unordered[lowest] = unordered[lowest], unordered[i]
    ordered.append(unordered[i])

print(ordered)