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

# val=[10,20,30,1000,40,50,60,70,80,90,100]
# a=itertools.accumulate(val,max)
# print(list(a))


# '''
# PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py
# [10, 20, 30, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
# '''
# '''
# PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py
# [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]
# '''

pay=[100,200,300,400,500]
update= lambda balsnces,pay : round(balsnces*1.04)-pay
balsnces= itertools.accumulate(pay, update,initial=2000)
print(list(balsnces))
r"""
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py
[2000, 1980, 1859, 1633, 1298, 850]
"""

r'''
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py
  File "C:\Users\Ayush Kumar Gupta\Desktop\Advance Python\itertools.py", line 48
    """
    ^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 6-7: truncated \UXXXXXXXX escape
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools.py
[2000, 1980, 1859, 1633, 1298, 850]
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> 
'''