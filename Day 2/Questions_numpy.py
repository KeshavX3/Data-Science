# 1. Wtie a Numpy program to create an array of 10 zeroes 
import numpy as np


zeroes_array = np.zeros(10)
print("Array of 10 zeroes : ")
print(zeroes_array)




# 2. Create a 2x3 numpy array filled with zeroes and print it 

arr_zeroes = np.zeros((2,3))
print("Array of zeroes")
print(arr_zeroes)


# 3. Wrie a Numpy program to create an array of 10 ones

ones_array = np.ones(10)
print("Array of 10 ones : ")
print(ones_array)


# 4. Create a 3x3 identify matrix using Numpy and print it 



identity_matrix = np.eye(3)
print("Identity_matrix")
print(identity_matrix)


# 5. Write a numpy Program to create an array of integers from 10 to 50 

import numpy as np
array = np.arange(10, 51)
print("Array of integers from 10 to 50 : ")
print(array)


# 6. Write a anumpy program to genrate a 1d array of 10 random integers between 0 to 50 

import numpy as np
arr = np.random.randint(0, 51, size=10)
print(arr)


# 7. Write a NumPy program to create a 2x3 array of random floats between 0 and 1

import numpy as np
array = np.random.rand(2, 3)
print(array)


# 8. Write a Numpy program to genrate the same random 3x3 matrix by setting a ssed


import numpy as np
np.random.seed(0)
matrix = np.random.rand(4,4)
print("Random 3x3 matrix:")
print(matrix)



# 9. import numpy as np

matrix = np.random.randint(1, 101, size=(4, 4))
print(matrix)


# 10 . Write a NumPy program to iterate over a 1D array and print each element?

array = np.array([1,2,3,4,5])
for element in array:
    print(element)


# 11. Write a Numpy program to split a 1D array of 10 elemetns into two equal sub arrays


array = np.arange(10)
sub_arrays = np.array_split(array,2)
print(sub_arrays)


# 12. Create a NumPy array and point its shape 
 
arr = np.array([[1,2,3],[4,5,6]])
arr.shape
print(arr)


# 13. Perform elelment-wise multiplication of two Numpy arrays [1,2,3] and [4,5,6] and print the result

import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 * array2
print("Element-wise multiplication result:")
print(result)



import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
addition_result = array1 + array2
print("Element-wise addition result: ", addition_result)
subtraction_result = array1 - array2
print("Element-wise subtraction result: ", subtraction_result)


# 14. Concatenate two Numpy arrays [1,2,3] and [4,5,6] along axis 0 and print the concatenated array 

import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
concatenated_array = np.concatenate((array1, array2))
print(concatenated_array)



# 15. create a 3x3 Numpy array filled with random numbers between 0 and 1 and print it 
import numpy as np
arr_random = np.random.rand(3,3)
print("3X3 Array of random numbers between 0 and 1 : ")
print(arr_random)


# 16. create a NumPy array with 5 evenly 