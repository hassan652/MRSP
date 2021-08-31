#2d-DFT

import numpy as np
import scipy.fftpack

X = np.array([[9.5,5.5,2.7],[1.5,9.1,1.0]])
T=scipy.fftpack.fft2(X)
print(T[0,0])