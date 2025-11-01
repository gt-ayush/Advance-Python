import pprint


val=['one','two','three','four','five']
print(*val)

print(*val,sep=' -- ')

for i in range (0,len(val)):
    print(val[i], end=f" [Line: {str(i+1)}]\n")

exit()