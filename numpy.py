import numpy as np
arr=np.array(([2,3,4],[7,6,5]))
arr1=np.array([1,7,9,5])
maxind = arr1.argmax()
print(arr1.argmax)
print("max index is ",maxind)

print(arr)
#arr(0)
print("ravi")
print(arr.argmax())
print(arr1.argsort())
#the argmax , argsort and many method must be define as a method like this ()   . 
sort_arr1=arr1.argsort()
print("sorting the arr1",sort_arr1)
#print(arr(type))

# Create a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_1d.shape)
#shape=arr_1d.shape()
#print(shape)
print(arr1.size)
print(arr1.dtype)


x=np.sum(arr_2d,axis=0)




arr3= np.array([[1, 2, 3], [4, 5, 6]])

# Sum along rows (axis=0)
axis_sum_row = arr3.sum(axis=0)
row_sum = np.sum(arr3, axis=0)  # Output: [5, 7, 9]
print("the row sum is ",axis_sum_row)
axis_sum_colomn = arr3.sum(axis=1)
print("the sum of the colomn is ",axis_sum_colomn)

# Sum along columns (axis=1)
#column_sum = np.sum(arr, axis=1)  # Output: [6, 15]


#######............

import numpy as np

arr = np.array([10, 5, 20, 15, 30])
max_index = arr.argmax()
#print(arr.argmax)

print("Index of maximum value:", max_index)  # Output: Index of maximum value: 4
#..................
rng= np.arange(15)
print(rng)

zero=np.zeros((2,5))
print(zero)


lspace=np.linspace(1,5,4)
print(lspace)


# Suppose 'data.csv' contains:
# 1, 2, 3
# 4, 5, 6

#loaded_array = np.loadtxt('data.csv', delimiter=',')
#print(loaded_array)
