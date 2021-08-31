'''
Given the matrix X = np.matrix([[7.9,8.9],[7.4,7.5]])

Calculate the eigenvalues of this matrix and provide the biggest eigenvalue in the answer field.
'''

import numpy as np

#This is for eigen values
X = np.matrix([[7.9,8.9],[7.4,7.5]])
eigen_values, eigen_vectors = np.linalg.eig(X)
print("Eigen Values\n",eigen_values)
print("YOU HAVE TO WRITE THE BIGGEST EIGENVALUE")