#!/usr/bin/python3
import random

name = input("What's your name? ")
operators = ["-", "+", "×", "÷"]

x = int()

for _ in range(10):
    first = random.randint(1, 20)
    print(first)
    second = random.randint(2, first)
    operator = random.choice(operators)
    message = f"{str(first)} {operator} {str(second)} = "
    answer = input(message)

    match operator:
        case "-":
            correctAnswer = first - second
        case "+":
            correctAnswer = first + second
        case "×":
            correctAnswer = first * second
        case "÷":
            correctAnswer = first / second

    if answer == str(correctAnswer):
        print("Correct answer! ")
        x += 1
    else:
        print("Wrong answer :( ")
print(x,"/10")
