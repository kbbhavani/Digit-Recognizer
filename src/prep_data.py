"""
This file will be used to prepare the data to be used by the model.
Data will be divided into train, cross validation, and test
"""


import numpy as np
import pandas as pd


data = pd.read_csv('../digit-recognizer/train.csv')

labels = np.asarray(data['label']) # can be used as y, the true values

data.set_index('label', inplace=True) # permanently sets label column to be the index

train_data = np.asarray(data)
train_data = np.transpose(train_data) # this fixes a small bug, changes shape to (784, 42000)

test_data = pd.read_csv('../digit-recognizer/test.csv')
test_data = np.asarray(test_data) # shape (28000, 784)
test_data = np.transpose(test_data) # this fixes a small bug, changes shape to (784, 28000)

m = len(labels) # number of training examples in training data

y = []
for i in range(m):
    temp = np.zeros((10,), dtype=int)
    temp[labels[i]] = 1
    y.append(temp)

y = np.asarray(y) # shape (42000, 10), a 1 for each label digit's position in an empty (10,) zeros array
y = np.transpose(y) # fixes a bug and changes shape of y to (10, 42000)

'''
FOR NOW THERE WILL BE NO CROSS VALIDATION TEST. AFTER A PRELIMINARY MODEL HAS BEEN MADE AND TESTED, 
THEN A CROSS VALIDATION TEST WILL BE USED TO OPTIMIZE THE REGULARIZATION PARAMETER (THERE IS NO
REGULARIZATION RIGHT NOW EITHER)
'''

