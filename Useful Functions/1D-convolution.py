'''
Imagine you have two following sequences:

X = [7.1,9.0,8.1,3.6]
Y = [3.5,2.6,1.0,2.6]

Convolve this two sequences  provide the first number in the answer field.
#Test
x(m)=[9.8, 9.1, 7.1, 5.1]
h(m)=[7.6, 3.2, 7.0, 6.4]

'''

import numpy as np

X=[8.9, 4.9, 8, 6.3]
Y=[1.1, 8.9, 2.3, 6.3]

conv = np.convolve(X,Y)
print("PRINTS THE FIRST NUMBER AFTER CONVOLUTION")
print(conv[0])