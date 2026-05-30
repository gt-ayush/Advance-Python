import pandas as pd

data = {
    "Name": ["Ayush", "Rahul", "Aman", "Sita", "Gita","Rohit"],
    "Age": [16, 17, 16, 18, 19, 20],
    "Dob": ["2007-01-01", "2006-05-15", "2007-03-20", "2005-11-10", "2004-07-25", "2003-09-30"],
    "City": ["Delhi", "Mumbai", "Bangalore","Chennai","Kolkata","Hyderabad"]
}

df = pd.DataFrame(data,index=["A", "B", "C", "D", "E","F"])

print(df)
print(df.values)
print(df.columns)
print(df.index)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 3)
print("---"*10)
print(df)