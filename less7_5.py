import numpy as np
import random


a = np.empty((3,3), dtype="float32")
for i in range(0,2):
    for j in (0,2):
        a[i][j] = random.random()

a_trans =  a.transpose()
print(a)
print(a_trans)