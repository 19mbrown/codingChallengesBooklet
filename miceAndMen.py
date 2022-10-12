import random

foo = str(f"{random.randint(0, 1000):04}")
number = int()

guess = False

print(foo)
while not guess:
    guessInput = f"{input('Guess a four digit number: '):04}"
    guessInput = "".join(list(set(guessInput)))
    for i in guessInput:
        if i in foo:
            number += 1
        if number == 4:
            guess = True
        print("Correct: ", number)

print("Correct! ")
print(foo)
