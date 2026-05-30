import pandas as pd

data = {
    "Name": ["Ayush", "Rahul", "Aman", "Sita", "Gita","Rohit"],
    "Age": [16, 17, 16, 18, 19, 20],
    "Dob": ["2007-01-01", "2006-05-15", "2007-03-20", "2005-11-10", "2004-07-25", "2003-09-30"],
    "City": ["Delhi", "Mumbai", "Bangalore","Chennai","Kolkata","Hyderabad"]
}

df = pd.DataFrame(data)

print(df)
