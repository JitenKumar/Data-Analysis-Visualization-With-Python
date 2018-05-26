import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5,5,0.01)
print(points)

dx,dy = np.meshgrid(points,points)

print(dx)
print(dy)
# make an array
arr = (np.sin(dx)+np.sin(dy))
print(arr)
# won't show the plot if True
plt.interactive(False)
plt.imshow(arr)
plt.colorbar()
plt.title('Plot for sin(x)+sin(y)')
#plt.show()

# Numpy where
# long way using list comprehensions
A =  [1,2,4,5,6]
B = [3,4,56,77,5]
cond = [False,True,False,True,False]
ans = [(a if cond else b)for a,b,cond in zip(A,B,cond)]
print(ans)
# using the where
answer2 = np.where(cond,A,B)
print(answer2)

# random values
arr5 = np.random.randn(5,5)
# using np where
print(arr5)
np.where(arr5<0,0,arr5)

arr6 = np.array([[1,2,3,4],[55,6,7,8,9],[9,10,182,3]])
print(arr6.sum())
print(arr6.sum(0))
