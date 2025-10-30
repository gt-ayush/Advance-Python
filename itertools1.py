import itertools

x= itertools.chain("Sur","123434")
print(list(x))

r"""
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools1.py
['S', 'u', 'r', '1', '2', '3', '4', '3', '4']
"""

def prepend(val, iter):
    return itertools.chain([val],iter)
print(list(prepend("a","bcdes")))

r"""
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools1.py
['S', 'u', 'r', '1', '2', '3', '4', '3', '4']
['a', 'b', 'c', 'd', 'e', 's']
"""



# r"""
# PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools1.py
# ['S', 'u', 'r', '1', '2', '3', '4', '3', '4']
# <itertools.chain object at 0x000001325BD75600>
# """

c=[1,2,233,14,14,15,245,25]
c1=[1,3424,542,52,52,423,425,4]
c2=[1,41,41,41,451,541.3]

r= itertools.chain.from_iterable([c,c1,c2])
print(list(r))

r"""
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools1.py
['S', 'u', 'r', '1', '2', '3', '4', '3', '4']
['a', 'b', 'c', 'd', 'e', 's']
[1, 2, 233, 14, 14, 15, 245, 25, 1, 3424, 542, 52, 52, 423, 425, 4, 1, 41, 41, 41, 451, 541.3]
"""