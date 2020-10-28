import numpy as np
#Get the Shape OF An Array

arr = np.array([[1,2,3,4,5,6],["Marvel","DC","Legendary","Dragon-ball","Pokemon","SonyMCU"]])
print("Shape of the array:- " ,arr.shape)
arry = np.array([1,2,3,4], ndmin=5)
#Create an array with 5 dimensions using ndmin using a vector with
# values 1,2,3,4 and verify that last dimension has value 4:

print(arry)
print("Shape of the array :- ", arry.shape)

#NumPy arrays have an attribute called shape that returns
# a tuple with each index having the number of corresponding elements.





