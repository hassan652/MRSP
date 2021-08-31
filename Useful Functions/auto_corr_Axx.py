'''
Imagine we have a matrix X = np.matrix([[2.1,6.6],[4.6,5.3]])

Calculate autocorrelation function Axx. In the answer field provide Axx(1,1) using Matlab notation.
'''
import numpy as np

X = np.matrix([[2.1,6.6],[4.6,5.3]])
print('original matrix\n',X)
Xtrans = X.T
print('Transpose matrix\n',Xtrans)
Auto_correlation = np.dot(Xtrans,X)
print('Autocorr matrix\n',Auto_correlation)
print("Matlab (1,1) is (0,0) in python")
print('required value\n',Auto_correlation[0,0])