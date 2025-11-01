import pprint


val=['one','two','three','four','five']
print(*val)

print(*val,sep=' -- ')

for i in range (0,len(val)):
    print(val[i], end=f" [Line: {str(i+1)}]\n")


r"""Output:


PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> & "C:/Users/Ayush Kumar Gupta/AppData/Local/Programs/Python/Python314/python.exe" "c:/Users/Ayush Kumar Gupta/Desktop/Advance Python/pprint.py"
one two three four five
one -- two -- three -- four -- five
one [Line: 1]
two [Line: 2]
three [Line: 3]
four [Line: 4]
five [Line: 5]
"""
nf=open("output.txt","w")
print(*val,sep=" -- ",file=nf,flush=True)



exit()