import numpy as np
from scipy.sparse import csc_matrix
arr = np.array([0,0,0,0,0,1,1,0,2])

arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csc_matrix(arr).data)
print(csc_matrix(arr))
print(csc_matrix(arr).count_nonzero())