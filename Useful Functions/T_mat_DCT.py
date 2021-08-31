'''
Python Example for the DCT
We again assume a number of sub bands of
N=4. We generate our transform matrix T,
'''
import numpy as np
N=4
T=np.zeros((N,N))
for k in range(4):
    for n in range(4):
        T[n,k]=np.cos(np.pi/N*(n+0.5)*(k))*np.sqrt(2.0/N)
T[:,0]=T[:,0]*np.sqrt(0.5)
print("Very similar to KLT\n",T)
'''
We check if our computed matrix is indeed 
orthonormal, as it should be, by checking if
T⋅T
T
=I is the identity,'''
print("On diagonals we get one, else python rounding errors\n",np.dot(T,T.T))

