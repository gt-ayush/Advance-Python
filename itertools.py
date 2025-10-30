# Itertools: count, cycle, accumulate
import itertools
val =['as','i am' ,'lool']

# p=itertools.cycle(val)
# print(next(p))
# print(next(p))
# print(next(p))

# '''
# PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py
# as
# i am
# lool
# '''

x= itertools.count(100,20)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
'''
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py   
100
120
140
160
'''