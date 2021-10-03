a = [4, 3, 3, 2]

O = [1, 2, 6, 8]
X = [3, 4, 5]

V = [-100] * 9
j = ["-"] * 9

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

# for w in win:
# o = [i - 1 in O for i in w]
# print(f"o = {o}")
# x = [i - 1 in X for i in w]
# print(f"x = {x}")

# x = [False, False, True, False]
x = [True, True]
if not any(x):
    print("yes")

else:
    print("no")
