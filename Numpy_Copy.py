import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
x = arr.copy()
#The copy owns the data and any changes made to
# the copy will not affect original array,
# and any changes made to the original array will not affect the copy.
arr[0] = 42

print(arr)
print(x)

x = arr.view()
#The view does not own the data
# and any changes made to the view will affect the original array,
# and any changes made to the original array will affect the view.
arr[3] = 51

print (arr)
print(x)