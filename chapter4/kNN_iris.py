from knn import kNN
import iris_dataset
import matplotlib.pyplot as plt
import numpy as np

def plotdata(Xtrain, Ytrain, Xtest=[], Ytest=[], Ztest=[]):
    color = {'setosa': 'b',
             'versicolor': 'g',
             'virginica': 'r'}
    for i in range(len(Xtrain)):
        plt.plot(Xtrain[i][0], Xtrain[i][1], 'x', c=color[Ytrain[i]], mfc='none')  # c = color, mfc = markerfacecolor
    for i in range(len(Xtest)):
        plt.plot(Xtest[i][0], Xtest[i][1], '.', c='none', mfc=color[Ytest[i]])
    for i in range(len(Ztest)):
        plt.plot(Xtest[i][0], Xtest[i][1], 'o', c=color[Ztest[i]], mfc='none')

if __name__ == '__main__':
    Xtrain, Ytrain, Xtest, Ytest = iris_dataset.load(split_train_test=0.6)
    plt.figure(1)
    rate = []
    K = range(1, len(Xtrain)+1)
    for k in K:
        Ztest = kNN(Xtrain, Ytrain, Xtest, k)
        plotdata(Xtrain, Ytrain, Xtest, Ytest, Ztest)
        plt.title('k = '+str(k))
        plt.draw()
        plt.pause(0.001)
        plt.cla()
        rate.append(np.sum(Ztest == Ytest) / len(Ytest) * 100)  # ກວດເບິ່ງວ່າ Ztest ກັບ Ytest ຄືກັນບໍ່
        # plt.figure(k+1)

    plt.figure(2)
    plt.plot(K, rate)
    plt.axis([0, 80, 30, 100])
    plt.xlabel('k')
    plt.ylabel('Accuracy rate (%)')
    plt.grid(True)
    plt.show()
    print(rate)

    plt.figure(3)
    k = rate.index(max(rate)) + 1
    print(f'K = {k}')
    Ztest = kNN(Xtrain, Ytrain, Xtest, k)
    plotdata(Xtrain, Ytrain, Xtest, Ytest, Ztest)
    plt.title('k = ' + str(k))
    plt.show()


