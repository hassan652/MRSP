'''
The following 2x2 image block is given:

np.matrix([[5,7.8],[8.8,7.4]])

What is the DC coefficient of its resulting 2x2 WHT?
#TEST
np.matrix([[1.3,6.5],[5.0,4.0]])
'''

import numpy as np

X = np.matrix([[1,1],[1,-1]])
given_matrix = np.matrix([[7.1,3],[8.7,7]])

step_1 = np.dot(X,given_matrix)
WHT_DC_coefficient = 0.5 * np.dot(step_1,X)
print(WHT_DC_coefficient)
print("DC-COEFFICIENT IS THE TOP RIGHT MOST VALUE OF THE WHT MATRIX; SO")
print(WHT_DC_coefficient[0,0])