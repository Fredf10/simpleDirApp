'''
Created on Oct 5, 2016

@author: fredrik
'''

import numpy as np

X = np.linspace(0, 1, 101)

Y1 = X

Y2 = X**2

f1 = open("data/linear.txt", 'w')

f2 = open("data/power.txt", 'w')

for n in range(len(X)):
    x = X[n]
    y1 = Y1[n]
    y2 = Y2[n]
    
    
    f1.write("{0}, {1}".format(x, y1))
    f1.write('\n')
    f2.write("{0}, {1}".format(x, y2))
    f2.write('\n')

f1.close()
f2.close()
