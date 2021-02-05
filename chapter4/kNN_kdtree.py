
import numpy as np
from kdtree import kdtree, node2tree

class Currentbest:
    d = []
    def __init__(self, dim):
        self.X = np.empty((0, dim + 1))    #  add 1 dim for label

def kNN_kdtree(node, X, k=1):
    label = []
    for i in range(X.shape[0]):
        currentbest = Currentbest(X.shape[1])
        currentbest = NN_kdtree2(X[i, :], node, currentbest, k)
        (values, counts) = np.unique(currentbest.X[:, -1], return_counts=True)
        ind = np.argmax(counts)
        label += [values[ind]]
    return label

def NN_kdtree2(X, node, currentbest, k):
    if node is None:
        return currentbest
    if node.right is None and node.left is None:   # leaf
        d = np.sum((X-node.med[:, :-1]) ** 2)
        if len(currentbest.d) == k and currentbest.d[-1] > d:
            currentbest.d = np.append(currentbest.d, d)
            IDX = np.argsort(currentbest.d)
            currentbest.d = currentbest.d[IDX]
            currentbest.X = np.vstack((currentbest.X, node.med))
            currentbest.X = currentbest.X[IDX]
            currentbest.d = currentbest.d[:-1]
            currentbest.X = currentbest.X[:-1]
        elif len(currentbest.d) < k:
            currentbest.d = np.append(currentbest.d, d)
            IDX = np.argsort(currentbest.d)
            currentbest.d = currentbest.d[IDX]
            currentbest.X = np.vstack((currentbest.X, node.med))
            currentbest.X = currentbest.X[IDX]
    else:
        if X[node.axis] <= node.med:
            print(f'-> {X[node.axis]}')
            currentbest = NN_kdtree2(X, node.left, currentbest, k)
            if len(currentbest.d) < k or (X[node.axis] - node.med) ** 2 <= currentbest.d[-1]:
                currentbest = NN_kdtree2(X, node.right, currentbest, k)
            else:
                currentbest = NN_kdtree2(X, node.right, currentbest, k)
                if len(currentbest.d) < k or (X[node.axis] - node.med) ** 2 <= currentbest.d[-1]:
                    currentbest = NN_kdtree2(X, node.left, currentbest, k)

    return currentbest

if __name__ == '__main__':

    from kNN_iris import plotdata
    import iris_dataset
    import matplotlib.pyplot as plt
    from chapter5.treeplot import treeplot

    Xtrain, Ytrain, Xtest, Ytest = iris_dataset.load(split_train_test=0.5)
    Xtrain, Ytrain, Xtest, Ytest = Xtrain[:5], Ytrain[:5], Xtest[:5], Ytest[:5]

    node = kdtree(Xtrain, Ytrain[:5])
    tree = node2tree(node)
    treeplot(tree, show=False)

    rate = []
    plt.figure()
    K = range(1, len(Xtrain) + 1)
    for k in K:
        Ztest = kNN_kdtree(node, Xtest, k)

        plotdata(Xtrain, Ytrain, Xtest, Ytest, Ztest)
        plt.title('k = ' + str(k))
        plt.draw()
        plt.pause(0.001)
        plt.cla()
        rate.append(np.sum(Ytest == Ztest) / len(Ytest) * 100)

    plt.figure()
    plt.plot(K, rate)
    plt.axis([0, 80, 30, 100])
    plt.xlabel('k')
    plt.ylabel('Accuracy rate (%)')

