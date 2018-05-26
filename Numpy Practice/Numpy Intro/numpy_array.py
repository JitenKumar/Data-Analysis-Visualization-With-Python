import numpy as np
list1 = [1,24,5,55,5]
list2 = [3,4,6,7,7]



list3 = [list1,list2]
my_array = np.array(list3)
print(my_array)
print(my_array.shape)

# array of zeroes
np.zeros(5)

# float array of ones

np.ones([5,5])

# diagonal of ones
np.ones(1)
# array upto a range
np.arange(5)
# array from a range to a limit
np.arange(5,50,3)