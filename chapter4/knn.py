# k-Nearest Neighbor
# 07/08/2017
# Copyright (C) 2017 Parinya Sanguansat
import numpy as np

def kNN(Xtrain, Ytrain, Xtest, k=5):
    Ztest = []
    for x in Xtest:   # [[10, 9]]
        d = np.sqrt(np.sum((Xtrain - x)**2, axis=1))   # d = [6 index] , axis = 1 -> [[3, 4], [2, 5]] = 3 + 4, 2 + 5
        idx = np.argsort(d)   # idx = [5, 4, 3, 1, 0, 2] or .... index of Xtrain
        (values, counts) = np.unique(Ytrain[idx[:k]], return_counts=True)   # same Target, count same Target
        print(f'values = {values}, counts = {counts}')
        ind = np.argmax(counts)   # select more counts
        Ztest.append(values[ind])   # append to Ytest
    return Ztest

if __name__ == '__main__':
    Xtrain = np.array([[1, 2], [2, 2], [2, 1], [8, 9], [10, 8], [9, 10]])
    Ytrain = np.array([1, 1, 1, 2, 2, 2])
    Xtest = np.array([[10, 9]])
    result = kNN(Xtrain, Ytrain, Xtest)
    print(f'group = {result}')