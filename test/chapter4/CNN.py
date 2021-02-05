import numpy as np
import matplotlib.pyplot as plt

Xtrain = np.array([[1, 3], [2, 5], [3, 3], [3, 4],
                   [5, 3], [6, 4], [7, 3], [8, 4]])
Ytrain = np.array(['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'])

plt.plot(Xtrain[:4, 0], Xtrain[:4, 1], "or")
plt.plot(Xtrain[4:, 0], Xtrain[4:, 1], "ob")
plt.show()


