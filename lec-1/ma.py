import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 2, 3, 6, 1])

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)

a = np.array([1, 2, 3])
print("2a =", 2 * a)

twos = np.array([2, 2, 2])
print("2a =", twos * a)

b = np.array([1, 2, 3, 4, 5])
c = np.array([1, 2])
print("b + c =", b + c)  # This will raise an error due to shape mismatch