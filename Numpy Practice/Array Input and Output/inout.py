import numpy as np

array = [1,3,4,5,6,7,7]
np.save('myarray',array)
array = np.arange(11)
print(array)
print(np.load('myarray.npy'))

# saving two array
arr1 = np.array([1,3,5,64,3,5,6,6])
arr2 = np.array([1,3,4,5,5,5,5,55,5])
print(arr1)
print(arr2)
#saving the array
np.savez('newzip.npz',x = arr1,y = arr2)
# loading the saved zipped arrays
zipped_array = np.load('newzip.npz')
print(zipped_array['x'])
print(zipped_array['y'])

#saving the text files using the delimiter
text_array = np.array([1,3,45,55,6])
np.savetxt('file.txt',text_array,delimiter=',')
text_array_loaded = np.loadtxt('file.txt',delimiter=',')
print(text_array_loaded)
