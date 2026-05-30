# Pandas in Python

## 1. Introduction

**Pandas** is a powerful open-source Python library used for **data manipulation, analysis, and handling structured data**. It provides easy-to-use data structures and functions that help work with datasets efficiently.

Pandas is widely used in:

* Data Science
* Machine Learning
* Data Analysis
* Business Intelligence
* Data Cleaning
* Financial Analysis

### Installation

```python
pip install pandas
```

### Importing Pandas

```python
import pandas as pd
```

The alias `pd` is the standard convention used by Python developers.

---

# 2. Why Use Pandas?

Without Pandas, handling large datasets can be difficult and time-consuming.

Pandas helps to:

* Read data from different sources
* Clean and transform data
* Analyze trends and patterns
* Handle missing values
* Filter and sort data
* Perform statistical operations
* Export processed data

---

# 3. Main Data Structures in Pandas

Pandas provides two primary data structures:

## A. Series

A **Series** is a one-dimensional labeled array.

### Example

```python
import pandas as pd

data = pd.Series([10, 20, 30, 40])

print(data)
```

### Output

```python
0    10
1    20
2    30
3    40
dtype: int64
```

### Characteristics

* One-dimensional
* Stores a single column of data
* Has indexes

---

## B. DataFrame

A **DataFrame** is a two-dimensional table consisting of rows and columns.

### Example

```python
import pandas as pd

data = {
    "Name": ["Ayush", "Rahul", "Aman"],
    "Age": [16, 17, 16]
}

df = pd.DataFrame(data)

print(df)
```

### Output

```python
    Name   Age
0  Ayush   16
1  Rahul   17
2   Aman   16
```

### Characteristics

* Most commonly used Pandas object
* Similar to an Excel spreadsheet
* Supports multiple data types

---

# 4. Creating a DataFrame

## From Dictionary

```python
data = {
    "Name": ["John", "Alice"],
    "Age": [20, 21]
}

df = pd.DataFrame(data)
```

## From List

```python
data = [
    ["John", 20],
    ["Alice", 21]
]

df = pd.DataFrame(data, columns=["Name", "Age"])
```

---

# 5. Reading Data Files

## Read CSV File

```python
df = pd.read_csv("students.csv")
```

## Read Excel File

```python
df = pd.read_excel("students.xlsx")
```

## Read JSON File

```python
df = pd.read_json("data.json")
```

---

# 6. Viewing Data

## First 5 Rows

```python
df.head()
```

## Last 5 Rows

```python
df.tail()
```

## Data Information

```python
df.info()
```

## Statistical Summary

```python
df.describe()
```

---

# 7. Selecting Data

## Select a Column

```python
df["Name"]
```

## Select Multiple Columns

```python
df[["Name", "Age"]]
```

## Select Row by Index

```python
df.loc[0]
```

## Select Row by Position

```python
df.iloc[0]
```

---

# 8. Filtering Data

### Example

```python
df[df["Age"] > 18]
```

### Output

Returns only rows where age is greater than 18.

### Multiple Conditions

```python
df[(df["Age"] > 18) & (df["Marks"] > 80)]
```

---

# 9. Adding New Columns

```python
df["Grade"] = ["A", "B", "A"]
```

### Example

```python
df["Total"] = df["Math"] + df["Science"]
```

---

# 10. Updating Data

```python
df.loc[0, "Age"] = 25
```

### Output

Updates age in the first row.

---

# 11. Deleting Data

## Delete Column

```python
df.drop("Age", axis=1)
```

## Delete Row

```python
df.drop(0)
```

---

# 12. Handling Missing Values

## Check Missing Values

```python
df.isnull()
```

## Count Missing Values

```python
df.isnull().sum()
```

## Remove Missing Values

```python
df.dropna()
```

## Fill Missing Values

```python
df.fillna(0)
```

---

# 13. Sorting Data

## Sort by Column

```python
df.sort_values("Age")
```

## Descending Order

```python
df.sort_values("Age", ascending=False)
```

---

# 14. Aggregation Functions

## Sum

```python
df["Marks"].sum()
```

## Mean

```python
df["Marks"].mean()
```

## Maximum

```python
df["Marks"].max()
```

## Minimum

```python
df["Marks"].min()
```

---

# 15. GroupBy Operation

Used to group similar data and perform calculations.

### Example

```python
df.groupby("Department")["Salary"].mean()
```

### Purpose

Find average salary department-wise.

---

# 16. Merging DataFrames

### Example

```python
pd.merge(df1, df2, on="ID")
```

### Uses

* Combine multiple datasets
* Similar to SQL JOIN operations

---

# 17. Exporting Data

## Save as CSV

```python
df.to_csv("output.csv")
```

## Save as Excel

```python
df.to_excel("output.xlsx")
```

---

# 18. Commonly Used Pandas Functions

| Function        | Purpose                  |
| --------------- | ------------------------ |
| `read_csv()`    | Read CSV file            |
| `head()`        | View first rows          |
| `tail()`        | View last rows           |
| `info()`        | Dataset information      |
| `describe()`    | Statistical summary      |
| `loc[]`         | Label-based selection    |
| `iloc[]`        | Position-based selection |
| `groupby()`     | Group data               |
| `sort_values()` | Sort data                |
| `drop()`        | Remove rows/columns      |
| `fillna()`      | Fill missing values      |
| `merge()`       | Combine DataFrames       |

---

# 19. Advantages of Pandas

1. Easy to learn and use.
2. Fast data processing.
3. Excellent support for CSV and Excel files.
4. Powerful filtering and aggregation features.
5. Integrates well with NumPy, Matplotlib, and Machine Learning libraries.
6. Widely used in industry and research.

---

# 20. Real-World Applications

* Student result analysis
* Sales data analysis
* Financial market analysis
* Customer behavior analysis
* Data preprocessing for Machine Learning
* Business reporting and dashboards

