import itertools
days=["sun","mon",'tue','wed','thu','fri','sat']
mon=['jan','feb','mar',"apr",'may','jun','jul','aug','nov','desc']

# for i in range(len(days)):
#     print(i+1, days[i])

# for i,d in enumerate(days, start=1):
#     print(i,d)

# for i in zip(days,mon ):
#     print(i)

for i , d in enumerate(zip(days,mon),start=1):
    print(i,d[0],"=",d[1],"in -------")

r=itertools.zip_longest(days,mon,fillvalue="-")

# for i in r:
#     print(i)

print(r)

'''
PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> py '.\More iterators.py'
1 sun = jan in -------
2 mon = feb in -------
3 tue = mar in -------
4 wed = apr in -------
5 thu = may in -------
6 fri = jun in -------
7 sat = jul in -------
<itertools.zip_longest object at 0x000001EFE9AE0F40>

### this is giving an error. if i directly print (r)
'''