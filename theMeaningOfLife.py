#########################
###### NOT WORKING ######
#########################


import random
import time

x = int(input("How many on the x-axis do you want there to be? "))
y = int(input("How many on the y-axis do you want there to be? "))

board = []

for i in range(y):
    board.append([])
    for j in range(x):
        if random.randint(0, x//2) == 1:
            board[i].append("+")
        else:
            board[i].append(".")

def printBoard( board ):
    for i in board:
        print(" ".join(i))


while True:
    for i in range(x):
        for j in range(y):
            tmp = 0
            try:
                if  "+" in board[i][y]:
                    tmp = [
                        board[i-1][y],
                        board[i][y-1],
                        board[i+1][y],
                        board[i][y+1],
                        board[i-1][y+1],
                        board[i+1][y-1],
                        board[i-1][y-1],
                        board[i+1][y-1]
                    ]
                    for k in tmp:
                        if k == "+":
                            tmp2 += 1
                    if tmp2 >= 2:
                        continue
                    else:
                        board[i][y] = "."
            except IndexError:
                continue
    printBoard(board)
    input("")
