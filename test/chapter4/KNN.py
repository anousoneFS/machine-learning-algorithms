import numpy as np
import matplotlib.pyplot as plt

def KNN(Xtrain, Ytrain, Xtest, K=1):
    Ztest = []
    for xtest in Xtest:
        dIndex = np.argsort(np.sqrt(np.sum((Xtrain - xtest) ** 2, axis=1)))
        U, count = np.unique(Ytrain[dIndex[:K]], return_counts=True)
        Z = U[np.argmax(count)]
        Ztest.append(Z)
    # result = np.sqrt(((5.1 - 5.4) ** 2 + (3.5 - 3.4) ** 2 + (1.4 - 1.7) ** 2 + (0.2 - 0.2) ** 2))
    # print(result)
    Ztest = np.array(Ztest)
    return Ztest

if __name__ == '__main__':

    # Xtrain = np.array([[1, 3], [2, 5], [3, 3], [3, 4],
    #                [5, 3], [6, 4], [7, 3], [8, 4]])
    Xtrain = np.array([[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2], [5.7, 4.4, 1.5, 0.4], [5.1, 3.8, 1.5, 0.3],
                       [7.0, 3.2, 4.7, 1.4], [6.4, 3.2, 4.5, 1.5], [5.9, 3.2, 4.8, 1.8], [6.7, 3.0, 5.0, 1.7]])
    Ytrain = np.array(['setosa', 'setosa', 'setosa', 'setosa', 'versicolor', 'versicolor', 'versicolor', 'versicolor'])
    Xtest = np.array([[5.4, 3.4, 1.7, 0.2]])
    print(KNN(Xtrain, Ytrain, Xtest))

    # plt.plot(Xtrain[:4, 0], Xtrain[:4, 1], "or")
    # plt.plot(Xtrain[4:, 0], Xtrain[4:, 1], "ob")
    # plt.show()
