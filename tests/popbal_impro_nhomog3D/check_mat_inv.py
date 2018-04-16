from math import * 
import numpy as np
x1 = 0.90037927
x2 = 0.02375006
A = np.matrix([[1,1,0,0],[0,0,1,1],[-(x1)**2,-(x2)**2,2*x1,2*x2],[-(x1)**3,-(x2)**3,3*x1,3*x2]])
inverse_A = np.linalg.inv(A)
print inverse_A
