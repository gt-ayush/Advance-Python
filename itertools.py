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

# x= itertools.count(100,20)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# '''
# PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py   
# 100
# 120
# 140
# 160
# '''

val=[10,20,30,1000,40,50,60,70,80,90,100]
a=itertools.accumulate(val,max)
print(list(a))


'''
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py
[10, 20, 30, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
'''
# '''
# PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py
# [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]
# '''