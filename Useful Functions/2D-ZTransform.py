'''
Compute the 2D z-Transform of the following 2x2 image block x, for z1=9.3 and z2=9.1:

X = np.matrix([[7.6,7.3],[1.5,9.5]])

'''

import numpy as np

X = np.matrix([[7.6,7.3],[1.5,9.5]])
z1 = 9.3
z2 = 9.1
Ans = 0
for r in range(X.shape[0]):
    for col in range(X.shape[1]):
        Ans += X[r,col] * z1**(-r) * z2**(-col)
Ans = str(round(Ans, 2))
print(Ans)
