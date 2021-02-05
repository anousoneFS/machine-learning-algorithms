import numpy as np
from iris_dataset import readData
from KNN import KNN

if __name__ == '__main__':
    Xtrain, Ytrain, Xtest, Ytest = readData(splitdata=0.5)
    K = len(Xtrain)
    a = []
    for k in range(1, K+1):
        # print(k)
        Ztest = KNN(Xtrain, Ytrain, Xtest, K=k)
        # print(Ztest.shape)
        # print(Ztest)
        # print(np.sum(Ztest == Ytest))
        a.append((np.sum(Ztest == Ytest) / len(Ytest)) * 100)

    print(np.argmax(a))
    K = np.argmax(a) + 1
    print(K)
    # print(Ytest.shape)

