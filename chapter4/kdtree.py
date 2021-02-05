import numpy as np

class Node:
    med = None
    left = None
    right = None
    axis = -1

def kdtree(X, label):
    X, d = np.unique(X, axis=0, return_index=True)
    X = np.hstack((X, label[d].reshape((X.shape[0], 1))))
    print(X)
    node = kdtree2(X)
    print(node)
    return node

def kdtree2(X):
    node = Node()
    if len(X) == 0:
        return node

    if X.shape[0] == 1:
        node.med = X
        return node

    node.axis = np.argmax(np.max(X[:, :-1], axis=0) - np.min(X[:, :-1], axis=0))  # ຊອກຫາ column ທີມີຄ່າ ຫ່າງກັນຫລາຍສຸດ
    # print(node.axis)
    med = X.shape[0] // 2 - 1        # id ຂອງ median ຄ່າກາງ

    if med == -1:                      # med ບໍ່ມີທາງເທົ່າກັບ -1
        print("eeeeeeeeeeeeeeeeeee")
        return node

    idx = np.argsort(X[:, node.axis])          # ເອົາ index ລຽງລໍາດັບແຕ່ນ້ອຍຫາຫລາຍຂອງ column ທີ່ມີຄ່າຫ່າງກັນຫລາຍສຸດ
    X = X[idx]                                 # ລຽງລໍາດັບຄ່າ X ໃໝ່ ໂດຍອີງຕາມ column ທີມີຄ່າຫາງກັນຫລາຍສຸດ
    print(f'X = {X}')
    node.med = (X[med, node.axis] + X[med+1, node.axis]) / 2     # ຊອກຫາຄ່າ median
    node.left = kdtree2(X[:med+1])
    node.right = kdtree2(X[med+1:])

    return node

def node2tree(node):
    T = []
    def buildtree(node, parent):
        T.append(parent)
        idx = len(T)
        if node.left is not None:
            buildtree(node.left, idx)
        if node.right is not None:
            buildtree(node.right, idx)
    buildtree(node, 0)
    return T

if __name__ == '__main__':
    import iris_dataset
    from chapter5.treeplot import treeplot
    Xtrain, Ytrain, Xtest, Ytest = iris_dataset.load(split_train_test=0.5)

    # xtrain = np.array([[2.0, 5.0, 8.0, 9.0], [3.2, 6.3, 8.1, 10.0], [3.6, 6.3, 7.8, 9.0], [1.0, 2.4, 8.9, 9.0], [7.4, 8.8, 9.0, 3.8]])
    # ytrain = np.array(['A', 'A', 'B', 'B', 'B'])

    node = kdtree(Xtrain[:5], Ytrain[:5])
    tree = node2tree(node)
    print(tree)
    treeplot(tree, show=True)


