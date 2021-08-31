'''

Compute the 2D convolution for the following two image blocks (s=x∗y) and provide s[0,1] (the second sample in the first row):

X = np.array([[6.1,9.4],[5.9,5.2]])
Y = np.array([[8.4,3.4],[5.6,3.1]])
#TEST
X = np.array([[8.7,7.3],[3.1,3.8]])
Y = np.array([[2.1,6.2],[8.3,1.9]])
'''


import numpy as np
import scipy.signal as sp

X = np.array([[9,7.4],[5.4,9.5]])
Y = np.array([[2,5.9],[5.9,4.2]])

conv = sp.convolve2d(X,Y)
print("Provides s[0,1] (the second sample in the first row)")
print(conv[0,1])