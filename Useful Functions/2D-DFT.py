'''
Imagine you have the following 2D array (Matrix)

X = np.matrix([[9.5,5.5,2.7],[1.5,9.1,1.0]])
Calculate 2D-DFT for this sequence and provide the first sample of the resulting spectrum X[0,0]
'''

import numpy as np

X = np.matrix([[9.3,9.7,3],[9.3,9.9,1.5]])
print(np.fft.fft2(X)[0,0])
print("IF YOU HAVE IMAGINARY VALUES, ONLY WRITE THE REAL ONE")