'''
Calculate the Mean Squared Error (MSE) for the following sequence: 
x = np.array([1,2,3,4]) if the decoded sequence is: 
decoded = np.array([6.4,8.7,7.2,1.0])
#TEST
x = np.array([1,2,3,4]) if the decoded sequence is: 
decoded = np.array([6.8, 6.3, 8.6, 1.0])

'''


import numpy as np

x = np.array([1,2,3,4])
decoded = np.array([2.9, 5.4, 5.5, 9.5])
difference_array = np.subtract(x, decoded)
squared_array = np.square(difference_array)
mse = squared_array.mean()
print(mse)