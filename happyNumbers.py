#!/usr/bin/python3
x = 20
while (x != 1):
    new = list(str(x))
    x = 0
    for i in new:
        x += int(i) ** 2
    print(x)
