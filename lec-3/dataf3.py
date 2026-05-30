import pandas as pd

df = pd.DataFrame({
    'ID': [100, 101, 102, 103],
    'City': ['Tokyo', 'Osaka', 'Kyoto', 'Nagoya'],
    'Birth_year': [1990, 1989, 1992, 1995],
    'Name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru']},
    index=['a', 'b', 'c', 'd']
)
print(df)
print(df['City'])
print(df['a':'c'])
