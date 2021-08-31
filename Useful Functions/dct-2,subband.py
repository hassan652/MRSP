'''
Assume we have a DCT type 2 transform for N=8 subbands. Determine its equivalent filters.
What is sample 5 of subband 2 of the impulse response for the equivalent filter bank on the synthesis side? (We start the indices with 0, as in the Lecture 4.)
'''

import numpy as np
import scipy.fftpack
I=np.eye(8)
T=scipy.fftpack.dct(I,norm='ortho')
T=np.matrix(T)
#print(T)
Tinv=T.I
print("-------")
#print(Tinv)
print('For sub band 2, sample 5')
print(Tinv[3,1])

#print('HINT: Sub band for synthesis is the inverse, sub band is vertical, sample is horizontal, both starts from 0')