# Pandas in Python - Complete Guide

## Table of Contents
1. [Introduction](#1-introduction)
2. [Installation & Setup](#2-installation--setup)
3. [Main Data Structures](#3-main-data-structures)
4. [Creating DataFrames](#4-creating-dataframes)
5. [Loading Data](#5-loading-data)
6. [Exploring Data](#6-exploring-data)
7. [Selecting & Filtering Data](#7-selecting--filtering-data)
8. [Data Manipulation](#8-data-manipulation)
9. [Data Cleaning](#9-data-cleaning)
10. [Data Analysis](#10-data-analysis)
11. [Exporting Data](#11-exporting-data)
12. [Practical Example: MyAnimeList](#12-practical-example-myanmelist)
13. [Reference Guide](#13-reference-guide)

---

## 1. Introduction

**Pandas** is a powerful open-source Python library used for **data manipulation, analysis, and handling structured data**. It provides easy-to-use data structures and functions that help work with datasets efficiently.

### Why Use Pandas?

Without Pandas, handling large datasets can be difficult and time-consuming. Pandas helps to:

* Read data from different sources
* Clean and transform data
* Analyze trends and patterns
* Handle missing values
* Filter and sort data
* Perform statistical operations
* Export processed data

### Common Use Cases

* Data Science & Machine Learning
* Business Intelligence
* Financial Analysis
* Data Cleaning & Preprocessing
* Academic Research

---

## 2. Installation & Setup

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

## 3. Main Data Structures

Pandas provides two primary data structures:

### A. Series

A **Series** is a one-dimensional labeled array.

**Example:**
```python
import pandas as pd

data = pd.Series([10, 20, 30, 40])
print(data)
```

**Output:**
```
0    10
1    20
2    30
3    40
dtype: int64
```

**Characteristics:**
* One-dimensional
* Stores a single column of data
* Has automatic indexes

---

### B. DataFrame (Most Important)

A **DataFrame** is a two-dimensional table consisting of rows and columns.

**Example:**
```python
import pandas as pd

data = {
    "Name": ["Ayush", "Rahul", "Aman"],
    "Age": [16, 17, 16]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**
```
    Name   Age
0  Ayush   16
1  Rahul   17
2   Aman   16
```

**Characteristics:**
* Most commonly used Pandas object
* Similar to an Excel spreadsheet
* Supports multiple data types
* Has both row and column indexes

---

## 4. Creating DataFrames

### From Dictionary

```python
data = {
    "Name": ["John", "Alice"],
    "Age": [20, 21]
}

df = pd.DataFrame(data)
```

### From List

```python
data = [
    ["John", 20],
    ["Alice", 21]
]

df = pd.DataFrame(data, columns=["Name", "Age"])
```

---

## 5. Loading Data

### Read CSV File

```python
df = pd.read_csv("students.csv")
```

### Read Excel File

```python
df = pd.read_excel("students.xlsx")
```

### Read JSON File

```python
df = pd.read_json("data.json")
```

---

## 6. Exploring Data

### View First/Last Rows

```python
df.head()      # First 5 rows
df.tail()      # Last 5 rows
df.head(10)    # First 10 rows
```

### Get Dataset Information

```python
df.info()      # Column info and data types
```

### Statistical Summary

```python
df.describe()  # Mean, std, min, max, quartiles
```

---

## 7. Selecting & Filtering Data

### Selecting Columns

```python
df["Name"]                    # Single column
df[["Name", "Age"]]          # Multiple columns
```

### Selecting Rows

```python
df.loc[0]                     # Select by label/index
df.iloc[0]                    # Select by position
df[0:3]                       # Slice rows (position-based)
```

### Filtering Data

```python
# Single condition
df[df["Age"] > 18]

# Multiple conditions
df[(df["Age"] > 18) & (df["Marks"] > 80)]

# Using isin()
df[df["City"].isin(["Delhi", "Mumbai"])]
```

---

## 8. Data Manipulation

### Adding New Columns

```python
# Add constant value
df["Grade"] = ["A", "B", "A"]

# Add calculated column
df["Total"] = df["Math"] + df["Science"]
```

### Updating Data

```python
# Update single cell
df.loc[0, "Age"] = 25

# Update multiple cells
df.loc[df["Age"] < 18, "Category"] = "Minor"
```

### Deleting Data

```python
# Delete column
df.drop("Age", axis=1)

# Delete row
df.drop(0)

# Drop multiple columns
df.drop(["Age", "Salary"], axis=1)
```

---

## 9. Data Cleaning

### Handling Missing Values

```python
# Check missing values
df.isnull()                    # Boolean DataFrame
df.isnull().sum()              # Count per column

# Remove missing values
df.dropna()                    # Drop rows with any NaN

# Fill missing values
df.fillna(0)                   # Fill with constant
df.fillna(method='ffill')      # Forward fill
df.fillna(df.mean())           # Fill with mean
```

### Sorting Data

```python
# Sort by single column
df.sort_values("Age")

# Sort descending
df.sort_values("Age", ascending=False)

# Sort by multiple columns
df.sort_values(["Department", "Salary"])
```

---

## 10. Data Analysis

### Aggregation Functions

```python
df["Marks"].sum()              # Total
df["Marks"].mean()             # Average
df["Marks"].max()              # Maximum
df["Marks"].min()              # Minimum
df["Marks"].std()              # Standard deviation
df["Marks"].count()            # Count non-null values
```

### GroupBy Operations

Used to group similar data and perform calculations.

```python
# Average salary by department
df.groupby("Department")["Salary"].mean()

# Multiple aggregations
df.groupby("Department").agg({
    "Salary": "mean",
    "Age": "max",
    "Employees": "count"
})
```

### Merging DataFrames

```python
# Merge on common column
pd.merge(df1, df2, on="ID")

# Different merge types
pd.merge(df1, df2, on="ID", how="inner")    # Inner join
pd.merge(df1, df2, on="ID", how="left")     # Left join
pd.merge(df1, df2, on="ID", how="outer")    # Outer join
```

---

## 11. Exporting Data

### Save as CSV

```python
df.to_csv("output.csv")
df.to_csv("output.csv", index=False)  # Without index
```

### Save as Excel

```python
df.to_excel("output.xlsx")
```

### Save as JSON

```python
df.to_json("output.json")
```

---

## 12. Practical Example: MyAnimeList

### Scenario

Downloading and analyzing anime data from GitHub using requests and pandas.

### Complete Workflow

#### Step 1: Download and Extract Data

```python
import requests, zipfile
from io import StringIO
import io
import pandas as pd

# Specify the url with data
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from the url
r = requests.get(url, stream=True)

# Read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
```

#### Step 2: Load CSV Files

```python
anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_list = pd.read_csv('MyAnimeList-Database-master/data/animelist.csv')
anime_synop = pd.read_csv('MyAnimeList-Database-master/data/anime_with_synopsis.csv')
```

#### Step 3: Explore the Dataset

```python
print(anime_data.head())      # View first 5 rows
print(anime_data.info())      # View column info and data types
print(anime_data.describe())  # View statistical summary
```

#### Step 4: Select Specific Columns

```python
col_use = ['MAL_ID', 'Name', 'Type', 'Episodes', 'Members', 'Score']
anime_data = anime_data[col_use]
print(anime_data.head())
```

### Dataset Insights

| Metric | Value |
|--------|-------|
| Total Records | 17,562 anime entries |
| Selected Columns | MAL_ID, Name, Type, Episodes, Members, Score |
| Data Types | int64 (MAL_ID, Members) & str (Name, Type, Episodes, Score) |
| Average Members | ~34,658 |
| Member Range | 1 to 2,589,552 |

### Key Concepts Applied

* **requests library**: Fetch data from URLs
* **zipfile module**: Extract compressed archives  
* **read_csv()**: Load data from CSV files
* **head()**: Preview first rows
* **info()**: Check data structure and types
* **describe()**: Get statistical overview
* **Column selection**: Filter specific columns using list indexing

---

## 13. Reference Guide

### Commonly Used Pandas Functions

| Function | Purpose |
|----------|---------|
| `read_csv()` | Read CSV file |
| `read_excel()` | Read Excel file |
| `head()` | View first rows |
| `tail()` | View last rows |
| `info()` | Dataset information |
| `describe()` | Statistical summary |
| `loc[]` | Label-based selection |
| `iloc[]` | Position-based selection |
| `sort_values()` | Sort data |
| `groupby()` | Group and aggregate data |
| `merge()` | Combine DataFrames |
| `drop()` | Remove rows/columns |
| `fillna()` | Fill missing values |
| `dropna()` | Remove missing values |
| `isnull()` | Check missing values |
| `to_csv()` | Export to CSV |
| `to_excel()` | Export to Excel |

### Advantages of Pandas

1. **Easy to learn and use** - Intuitive syntax similar to SQL
2. **Fast data processing** - Optimized for performance
3. **Excellent file support** - CSV, Excel, JSON, SQL databases
4. **Powerful operations** - Filtering, aggregation, merging
5. **Missing data handling** - Built-in functions for NaN values
6. **Visualization ready** - Integrates well with Matplotlib
7. **Machine Learning ready** - Works seamlessly with scikit-learn
8. **Widely adopted** - Industry standard for data analysis

### Real-World Applications

* Student result analysis
* Sales data analysis
* Financial market analysis & trading
* Customer behavior analysis
* Data preprocessing for Machine Learning
* Business reporting and dashboards
* Scientific research analysis
* Market research

