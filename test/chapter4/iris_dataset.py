import numpy as np
import pandas as pd
import os

def readData(path = "/Users/anousoneworlakoumman/Desktop/AIwithML/dataset/iris.csv", splitdata=None):
    if os.path.isfile(path):
        iris = pd.read_csv(path)
    else:
        url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        iris = pd.read_csv(url)
        iris.to_csv(path, index=False)

    X = iris.iloc[:, :4].values
    Y = iris.iloc[:, -1].values

    classes = np.unique(Y)
    itrain = np.empty((0,), dtype=int)
    itest = np.empty((0,), dtype=int)
    if splitdata:
        for i in range(len(classes)):
            index = np.where(Y == classes[i])[0]
            l = int(len(index) * splitdata)
            itrain = np.concatenate((itrain, index[:l]))
            itest = np.concatenate((itest, index[l:]))

        return X[itrain], Y[itrain], X[itest], Y[itest]
    return X, Y
if __name__ == '__main__':
    a, b = readData()
    print(a.shape)
    print(b.shape)
    # print(c)
    # print(d)