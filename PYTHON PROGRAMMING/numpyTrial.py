# # basic array characteristics
# import numpy as np

# # Creating array object
# arr = np.array( [[ 1, 2, 3],
#                 [ 4, 2, 5]] )

# # Printing type of arr object
# print("Array is of type: ", type(arr))

# # Printing array dimensions (axes)
# print("No. of dimensions: ", arr.ndim)

# # Printing shape of array
# print("Shape of array: ", type(arr.shape))

# # Printing size (total number of elements) of array
# print("Size of array: ", type(arr.size))

# # Printing type of elements in array
# # print("Array stores elements of type: ", arr.dtype)


# array creation techniques
'''
import numpy as np

# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)

# Creating array from tuple
b = np.array(((1 , 3, 2),(4,5,6)))
print ("\nArray created using passed tuple:\n", b)

# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)

# Create a constant value array of complex type
d = np.full((3, 3), 6,dtype = 'complex')
print ("\nAn array initialized with all 6s."
            "Array type is complex:\n", d)

# Create an array with random values
e = np.random.random((2, 2))
print ("\nA random array:\n", e)

# Create a sequence of integers
# from 0 to 30 with steps of 5
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)

# Create a sequence of 10 values in range 0 to 5
g = np.linspace(0, 5, 10)
print ("\nA sequential array with 10 values between"
                                        "0 and 5:\n", g)

# Reshaping 3X4 array to 2X2X3 array
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])

newarr = arr.reshape(2, 2, 3)

print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)

# Flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()

print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)


# indexing in numpy
import numpy as np

# An exemplar array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Slicing array
temp = arr[:2, :1:]
print ("Array with first 2 rows and alternate"
                    "columns(0 and 2):\n", temp)

# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
                                    "(3, 0):\n", temp)

# boolean array indexing example
cond = arr > 0 # cond is a boolean array
temp = arr[cond]
print ("\nElements greater than 0:\n", temp)

import numpy as np

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])

# maximum element of array
print ("Largest element is:", arr.max())
print ("Row-wise maximum elements:",
                    arr.max(axis=1))

# minimum element of array
print ("Column-wise minimum elements:",
                        arr.min(axis = 0))

# sum of array elements
print ("Sum of all array elements:",
                            arr.sum())

# cumulative sum along each row
print ("Cumulative sum along each row:\n",
                        arr.cumsum(axis = 1))



# binary operators in Numpy
import numpy as np

a = np.array([[1, 2],
            [3, 4]])
b = np.array([[4, 3],
            [2, 1]])

# add arrays
print ("Array sum:\n", a + b)

# multiply arrays (elementwise multiplication)
print ("Array multiplication:\n", a*b)

# matrix multiplication
print ("Matrix multiplication:\n", a.dot(b))

import numpy as np
a = np.array([[1, 4, 2],
                [3, 4, 6],
            [0, -1, 5]])

# sorted array
print ("Array elements in sorted order:\n",
                    np.sort(a, axis = None))

# sort array row-wise
print ("Row-wise sorted array:\n",
                np.sort(a, axis = 1))

# specify sort algorithm
print ("Column wise sort by applying merge-sort:\n",
            np.sort(a, axis = 0, kind = 'mergesort'))
'''

def ExtEuclidean(a, b):
    r = a
    r1 = b
    s = 1
    s1 = 0
    t = 0
    t1 = 1
    while r1 != 0:
        q = r//r1
        r2 = r%r1
        print(f"{r}, {r1}, {q}, {r2}, {s}, {t}, {s1}, {t1}")
        r, r1, s, t, s1, t1 = r1, r2, s1, t1, (s - s1*q), (t - t1*q)
    return r, s, t

r, s, t = ExtEuclidean(166, 13)

print(f"{r} = {s}*166 + {t}*13")
