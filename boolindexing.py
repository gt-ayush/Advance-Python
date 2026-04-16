import numpy as np
a = np.array([1, 1, 2, 3, 5, 8, 13])

# Create a list of boolean values
idx = [True, False, False, True, False, True, True]

# Boolean indexing
print(a[idx])

print("First value from the front:",a[0])

print("First value from the back:",a[-1])

def make_bool_ids(a):
    
    b= (a%2 ==1) | (a%4 ==2)

    return a[b] 

print(make_bool_ids(a))

def count_square(n):
  squares = np.arange(1, n) ** 2
  m = squares < n
  return np.sum(m)

print(count_square(20))

