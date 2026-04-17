import numpy as np

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("When start is omitted:", end='\t')
print(a[:15:3])
# When start is omitted:        [ 0  3  6  9]

print("When end is omitted:", end='\t')
print(a[2::3])
# When end is omitted:          [ 2  5  8]

print("When step is omitted (1):", end='\t')
print(a[2:15:])
# When step is omitted (1):     [ 2  3  4  5  6  7  8  9]

# The last ":" can also be omitted
print("When step is omitted (2):", end='\t')
print(a[2:15])
# When step is omitted (2):     [ 2  3  4  5  6  7  8  9]

print("When step and end are omitted:", end='\t')
print(a[2:])
# When step and end are omitted: [ 2  3  4  5  6  7  8  9]