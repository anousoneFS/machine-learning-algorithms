# Tic-Tac-Toe
# 3/8/2017
# Copyright (C) 2017 Parinya Sanguansat

import numpy as np
import random

O = []
X = []
win = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]


def checkWin(P):
    for w in win:
        if all(x - 1 in P for x in w):
            return True
    return False


def displayOX():
    OX = np.array([" "] * 9)
    OX[O] = ["O"]
    OX[X] = ["X"]
    print(OX.reshape([3, 3]))


def AI():
    validmove = list(set(range(9)) - set(O + X))
    print(validmove)
    V = [-100] * 9
    for m in validmove:
        tempX = X + [m]
        V[m], criticalmove = evalOX(O, tempX)
        if len(criticalmove) > 0:
            move = [i - 1 for i in criticalmove if i - 1 in validmove]
            return random.choice(move)

    maxV = max(V)
    imaxV = [i for i, j in enumerate(V) if j == maxV]
    print(imaxV)
    return random.choice(imaxV)


def evalOX(O, X):
    SO, SX, criticalmove = calSOX(O, X)
    return 1 + SX - SO, criticalmove  # V(b) = X(b) - O(b) + 1


def calSOX(O, X):
    SO = SX = 0
    criticalmove = []
    # l = []
    for w in win:  # loop 8 times  [0, 1, 2], [3, 4, 5], ....
        o = [i - 1 in O for i in w]  # [True, False, False] ....
        x = [i - 1 in X for i in w]  # [False, False, False] ....
        if not any(x):  # if that line do not have x ( 8 line)
            nO = o.count(True)
            SO += nO
            if nO == 2:  # [0, 1]
                print("critical", w)  # [0, 1, 2]
                criticalmove = w

        if not any(o):  # if that line don't have o
            SX += x.count(True)
    return SO, SX, criticalmove


while True:
    move = int(input("Choose position [1-9]: ")) - 1
    while move in O + X or move > 8 or move < 0:
        move = int(input("Bad move: Choose position [1-9]: ")) - 1
    O.append(move)
    displayOX()
    if checkWin(O):
        print("O win")
        break
    if len(O) + len(X) == 9:
        print("Draw")
        break
    X.append(AI())
    displayOX()
    if checkWin(X):
        print("X win")
        break
    if len(O) + len(X) == 9:
        print("Draw")
        break

# if __name__ == '__main__':
#     # print(checkWin(X))
#     # displayOX()
#     # print(AI())
#     o, x, c = calSOX(O, X)
#     print(f'SO = {o}, SX = {x} and critical = {c}')
#     # o = [False, False, False]
#     # print(o.count(True))
