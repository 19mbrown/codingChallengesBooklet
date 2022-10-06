#!/usr/bin/python3
import random

possible = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

money = 100

x = [random.choice(possible), random.choice(possible), random.choice(possible)]
print(x)
for i in x:
    money -= 20
    # break
    if x.count(i) == 2:
        money += 50
        if i != "Bell":
            break
    if x.count(i) == 3:
        money += 100
        if i != "Bell":
            break
    if x.count("Bell") == 3:
        print("Bell",x.count("Bell"))
        money += 500
        break

print(money)