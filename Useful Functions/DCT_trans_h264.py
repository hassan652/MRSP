'''
Imagine given picture block

X=⎡⎣⎢⎢⎢6.71.21.85.88.852.93.49.455.85.77.951.56.9⎤⎦⎥⎥⎥

Calculate the DCT integer transform of H.264 and provide the first value of the resulting matrix.
(Hint use rounded H matrix defined in Lecture 9. Also note here encoder takes a transpose of the usual transform.)
'''
import numpy as np
X = np.matrix([[6.7,8.8,9.4,7.9],
              [1.2,5,5,5],
              [1.8,2.9,5.8,1.5],
              [5.8,3.4,5.7,6.9]])
Ans = str(round(np.matrix.sum(X), 2))
print(Ans)
