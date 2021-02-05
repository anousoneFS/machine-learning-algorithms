import pandas as pd
import os
import numpy as np

def load(path = '/Users/anousoneworlakoumman/Desktop/AIwithML/dataset/iris.csv', split_train_test=None):
    if os.path.isfile(path):
        iris = pd.read_csv(path)
    else:
        url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        iris = pd.read_csv(url, header=None)
        iris.to_csv(path, index=False)

    X = iris.iloc[:, :4].values
    Y = iris.iloc[:, -1].values
    if split_train_test:
        classes = np.unique(Y)    # ['setosa', 'versicolor', 'virginica']
        itrain = np.empty((0,), dtype=np.int)   # numpy.ndarray 1 dimension
        itest = np.empty((0, ), dtype=np.int)
        for i in classes:
            idx = np.where(Y == i)[0]  # id where have setosa or versicolor (default 2 dimension)
            split = int(len(idx) * split_train_test)  # 50 * 0.5 = 25 //  25 + 25 + 25 = 75
            itrain = np.concatenate((itrain, idx[:split]))  # Joining the two arrays along axis 0:
            itest = np.concatenate((itest, idx[split:]))   # if Joining dimension should same

        return X[itrain], Y[itrain], X[itest], Y[itest]
    return X, Y

if __name__ == '__main__':
    a, b, c, d = load(split_train_test=0.5)
    # idx = np.where(irisTargets == 'virginica')[0]
    # print(idx[: 15])
    print(a, b)
