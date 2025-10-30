days=["sun","mon",'tue','wed','thu','fri','sat']
mon=['jan','feb','mar',"apr",'may','jun','jul']

# for i in range(len(days)):
#     print(i+1, days[i])

# for i,d in enumerate(days, start=1):
#     print(i,d)

# for i in zip(days,mon ):
#     print(i)

for i , d in enumerate(zip(days,mon),start=1):
    print(i,d[0],"=",d[1],"in -------")