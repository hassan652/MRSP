from numpy import linalg as LA
import numpy as np

Axx = np.matrix([[9.2,0],[0,15.5]])
Lamba, T = LA.eig(Axx) #T contains eigen vectors as columns
print('T:', T[0,0])