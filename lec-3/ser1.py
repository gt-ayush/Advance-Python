import pandas as pd

data = pd.Series([10, 20, 30, 40]
                 ,index=['a', 'b', 'c', 'd'])

print(data)
print(data.index)
print(data.values)