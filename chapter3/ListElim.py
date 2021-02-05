# List-Then-Elimination algorithm
# 07/08/2017
# Copyright (C) 2017 Parinya sanguansat

import numpy as np

def ListElim(X, T):
    X = np.array(X)
    T = np.array(T)
    n = X.shape[1]
    A = []
    for i in range(n):
        A.append(sorted(list(set(X[:, i]))))    # select All Row, One Column

    H = []
    t = []
    i = 1
    print(A)

    idx_data = [0] * n
    while True:
        h = []
        for j in range(n):
            h.append(A[j][idx_data[j]])   # row 0, column 0 / row 1, column 0 / row 2, column 0
        for tt in np.unique(T):   # tt = No, tt = Yes
            if isConsist(X, T, h, tt):
                H.append(h)
                t.append(tt)
                print(i, h, tt)
                i += 1

            idx_data[-1] += 1
            print(f'idx = {idx_data}')
            letter_index = n-1     # letter_index = 6-1 = 5
            while idx_data[letter_index] > len(A[letter_index])-1:    #      > 2 - 1
                idx_data[letter_index] = 0
                letter_index -= 1
                if letter_index < 0:
                    return H, t
                idx_data[letter_index] += 1
            print(idx_data)
    return H, t

def isConsist(X, T, h, t):
    for i in range(len(X)):   # len(X) = 4
        if h == list(X[i]):   # h = ['Rainy', 'Cold', 'High', 'Strong', 'Cool', 'Change'] == X[0] , ....
            if T[i] != t:     # T = ['Yes', 'Yes', 'No', 'Yes'],  t = tt = No or Yes
                return False
    return True

if __name__ == '__main__':
    X = [['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
         ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'],
         ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],
         ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change']]
    T = ['Yes', 'Yes', 'No', 'Yes']
    H, t = ListElim(X, T)     # H = Hypothesis, t = target
    # print(H, t)