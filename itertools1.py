import itertools

x= itertools.chain("Sur","123434")
print(list(x))

r"""
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools1.py
['S', 'u', 'r', '1', '2', '3', '4', '3', '4']
"""

def prepend(val, iter):
    return itertools.chain(val,iter)
print(prepend("a","bcdes"))

r"""
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py .\itertools1.py
['S', 'u', 'r', '1', '2', '3', '4', '3', '4']
<itertools.chain object at 0x000001325BD75600>
"""