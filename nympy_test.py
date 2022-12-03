import numpy as np

# we speak of a vector when we speak of a table of dimension 1
vector = np.array([3,4,17,65])
print(vector)

# we speak of a vector when we speak of a table of dimension 2
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)

"""
how to know the number of elements in an array :
            --- ndarray.shape ---
for vectors ndarray.shape will return a tuple
for matrices ndarray.shape will return the number of rows and columns
"""

print("Nb element vector : ", vector.shape)
print("Nb line & column matrix : ", matrix.shape)