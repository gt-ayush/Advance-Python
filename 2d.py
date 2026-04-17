import numpy as np

# Create a 3*2 matrix from 3*2 list
a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(a)
print("shape:", a.shape) # Returns a tuple representing the shape of array a

a = np.array([1, 2, 3, 4, 5, 6])
a = a.reshape(3, 2)
print(a)
print("shape:", a.shape)

a = np.array([1, 2, 3, 4, 5, 6])
a = a.reshape(3, 1)