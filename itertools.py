# Itertools: count, cycle, accumulate
import itertools
val =['as','i am' ,'lool']

p=itertools.cycle(val)
print(next(p))
print(next(p))
print(next(p))

'''
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py
as
i am
lool
'''