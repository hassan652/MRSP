from numpy import linalg as LA
import numpy as np

X = np.matrix([[1,1,1,1],
               [2,1,-1,-2],
               [1,-1,-1,1],
               [1,-2,2,-1]])
print(LA.inv(X))
