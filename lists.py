import random

n = int(input("How long do you want this list to be? "))
new = []
[new.append(i) for i in range(1, n + 1)]

string = input("What string do you want to insert? ")
index = int(input("Where do you want to insert this? "))

new.insert(index, string)

numberOfElems = int(input("How many elements do you want? "))

x = []
[x.append(random.choice(new)) for _ in range(numberOfElems)]
x.sort()
print(x)
