# condensed Nearest Neighbor
# 10/08/2017
# Copyright (C) 2017 Parinya Sanguansat
import numpy as np

def CNN(Xtrain, Ytrain):
    nsample = Xtrain.shape[0]    # row ຈໍານວນຂໍ້ມູນ
    # Distance
    Dtrain = []
    for x in Xtrain:
        Dtrain.append(np.sqrt(np.sum((Xtrain - x)**2, axis=1)))  # ເອົາໂຕມັນເອງ ທຽບໄລຍະຫາງ ກັບໂຕມັນເອງທັງຫມົດ
    Dtrain = np.array(Dtrain)   # ປ່ຽນເປັນ numpy array ເນື່ອງຈາກກ່ອນໜ້ານີ້ຢາກໃຊ້ .append()
    print(f'Dtrain = {Dtrain}')
    # Border ratio
    a = []
    for i in range(nsample):
        # y = the closest sample from x with different class from x
        yidx = np.where(Ytrain != Ytrain[i])[0]    # index of Ytrain that not  "verginica" or "versicolor" or ....
        yidx = yidx[np.argmin(Dtrain[i, yidx])]    # index of Ytrain(0-6) that have little distance and different class from x
        # xd = the closest sample from y with same class as x
        xdidx = np.where(Ytrain == Ytrain[i])[0]     # index same class as x  sample = [0,1,2,3,4,5,6]
        xdidx = np.delete(xdidx, np.where(xdidx == np.array(i)))  # delete at i sample if i = 0 -> [1,2,3,4,5,6] or i = 2 -> [0,1,3,4,5,6]
        # print(f'xdidx = {xdidx}')
        # print(f'yidx = {yidx}')
        # print(f'Dtrain x = {Dtrain[yidx, xdidx]}')
        # print(f'argmin Dtrain = {np.argmin(Dtrain[yidx, xdidx])}')
        xdidx = xdidx[np.argmin(Dtrain[yidx, xdidx])]   # sample [1,2,3,4,5,6] => 1
        # print(f' => result = {xdidx}')
        a.append(Dtrain[yidx, xdidx] / Dtrain[i, yidx])
    print(a)
    # Scan order
    order = np.argsort(-np.array(a))    # order = [4 2 3 5 1 0 6 7]
    # Prototypes
    Prototypes = order[0]   # Prototypes = [4]
    i = 0
    while len(order) > 0 and i < len(order):   # ລົດຂະໜາດລົງປະມານ ເຄິ່ງຫນຶ່ງ (i < len(order))
        idx = np.argsort(Dtrain[order[i], Prototypes])
        print(idx)
        for j in idx:
            if Ytrain[order[i]] != Ytrain[order[j]]:
                Prototypes = np.append(Prototypes, order[i])
                order = np.delete(order, i)
                break
        i += 1
    return Prototypes   # [4 2 5 0 7]




if __name__ == '__main__':
    # Xtrain = np.array([[2, 2], [3, 1], [4, 3], [6, 3], [8, 9], [4, 2], [1, 2]])
    # Ytrain = np.array([1, 1, 1, 2, 2, 2, 2])
    # Xtrain = np.array([[1, 3], [2, 5], [3, 3], [3, 4],
    #                    [5, 3], [6, 4], [7, 3], [8, 4]])
    # Ytrain = np.array(['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'])
    #
    # CNN(Xtrain, Ytrain)

    from knn import kNN
    import iris_dataset
    from kNN_iris import plotdata
    import matplotlib.pyplot as plt

    Xtrain, Ytrain, Xtest, Ytest = iris_dataset.load(split_train_test=0.5)
    Prototypes = CNN(Xtrain, Ytrain)

    rate = []

    plt.figure(1)
    K = range(1, len(Prototypes) + 1)
    for k in K:
        Ztest = kNN(Xtrain[Prototypes], Ytrain[Prototypes], Xtest, k)

        plotdata(Xtrain[Prototypes], Ytrain[Prototypes], Xtest, Ytest, Ztest)
        plt.title('k = '+str(k))
        plt.draw()
        plt.pause(0.001)
        plt.cla()
        rate.append(sum(Ztest == Ytest) / len(Ytest) * 100)

    plt.figure(2)
    plt.plot(K, rate)
    plt.axis([0, 80, 30, 100])
    plt.xlabel('k')
    plt.ylabel('Accuracy rate (%)')
    plt.grid(True)
    print(rate)

    # Plot the best accuracy
    plt.figure(3)
    maxrate = max(rate)
    print(maxrate)
    k = rate.index(maxrate) + 1
    Ztest = kNN(Xtrain[Prototypes], Ytrain[Prototypes], Xtest, k)
    plotdata(Xtrain[Prototypes], Ytrain[Prototypes], Xtest, Ytest, Ztest)
    plt.title('k = ' + str(k))

    # Plot Prototypes vs All samples
    plt.figure(4)
    plt.subplot(121)
    plotdata(Xtrain[Prototypes], Ytrain[Prototypes])
    plt.title('Prototypes')

    plt.subplot(122)
    plotdata(Xtrain, Ytrain)
    plt.title('All training sumples')
    plt.show()

