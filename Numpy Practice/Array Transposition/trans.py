import numpy as np
#import panda as pd

arr = np.arange(50).reshape((10,5))

print(arr)

# Transposing the array
print(arr.T)

# Dot product

print(np.dot(arr,arr.T))

# another example
arr3 = np.arange(50).reshape((5,5,2))
print(arr3)
print(arr3.transpose(1,0,2))
# swapping axes

arr4 = np.array([[1,2,3,4,5]])
print(arr4)
print(arr4.swapaxes(0,1))
