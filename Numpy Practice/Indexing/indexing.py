import numpy as np

arr = np.arange(0,11)

print(arr)
# getting upto a range
print(arr[1:6])
# setting all the values
arr[0:5] = 100
print(arr)
# new array
arr2 = np.arange(0,11)

# getting a slice of the array
slice_of_arr2 = arr2.copy()

slice_of_arr2[:] = 55

print(slice_of_arr2)
# 2d array
arr3 = np.array(([1,2,4,565,66],[24,5,4,44],[3,45,5,34,34,4],[424,2424]))
print(arr3)
print(arr3[0][1])

print(arr3[2][1])