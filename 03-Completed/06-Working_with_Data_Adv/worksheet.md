# 📝 Worksheet: 06 - Working with Data (Advanced)

Use this worksheet to reinforce Pandas Series/DataFrames and the core data-wrangling workflow: load, explore, select, clean, transform, sort/filter/search, group, and combine. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🐼 Section 1: Series and DataFrames

1. What's the difference between a Pandas `Series` and a `DataFrame`? How does a list of dictionaries (from Module 03) turn into one?  
   `Answer:` A Series is a one-dimensional collection of data (like a single column), while a DataFrame is a two-dimensional table with rows and columns.A list of dictionaries can be converted into a DataFrame using pd.DataFrame(). Each dictionary becomes a row, and the dictionary keys become the column names.

2. If you add two `Series` together and a label appears in only one of them, what value do you get at that label, and why?  
   `Answer:`When you add two Series, Pandas aligns them by their index labels. If one Series has a label that the other does not, the result for that label will be NaN.

---

### ✏️ Task: Series Basics

```python
# Create a Series from a dictionary mapping 4 of your classes to your grade in each.
# Print the Series, then print the average of all grades (hint: .mean()).
```
import pandas as pd

grades = {
    'Statistics': 95,
    'Python': 92,
    'Database Systems': 88,
    'Business Analytics': 94
}

grade_series = pd.Series(grades)

print(grade_series)
print("\nAverage grade:", grade_series.mean())
### 🤖 Explain It

In your own words: how is a Pandas `Series` similar to a Python dictionary, and how is it similar to a list? What does it borrow from each?
`A Pandas Series is similar to both a dictionary and a list. A Series combines the labeled lookup of a dictionary with the ordered sequence and numeric operations of a list.`
---

## 📂 Section 2: Loading and Exploring

3. What does `df.info()` tell you that `df.describe()` doesn't?  
   `Answer:` df.info() tells you about the DataFrame's structure, data types, non-null counts, and memory usage, while df.describe() provides statistical summaries of the data. df.info() can reveal missing values and column dtypes, which df.describe() does not.
4. If `df.isnull().sum()` shows `Age: 177`, what does that number mean?  
   `Answer:` There are 177 mising values in the Age column.

5. In `titanic.csv`, what does **one row** represent, and which column identifies each row?  
   `Answer:` Answer: In titanic.csv, one row represents one passenger and their information (such as age, sex, ticket, fare, and survival status). The PassengerId column uniquely identifies each passenger (row).
---

### ✏️ Task: First Look at a Dataset

```python
# Load pokemon.csv.
# Print its shape, its columns, and .describe() for just the numeric columns.
# Which column has the most missing values, if any?
```
import pandas as pd

# Load the dataset
pokemon = pd.read_csv("pokemon.csv")

# Print shape
print("Shape:", pokemon.shape)

# Print columns
print("\nColumns:")
print(pokemon.columns.tolist())

# Describe only numeric columns
print("\nNumeric summary:")
print(pokemon.describe())

# Find the column with the most missing values
missing = pokemon.isnull().sum()
most_missing_col = missing.idxmax()
most_missing_count = missing.max()

print("\nMissing values by column:")
print(missing.sort_values(ascending=False))

if most_missing_count > 0:
    print(f"\nColumn with the most missing values: {most_missing_col} ({most_missing_count})")
else:
    print("\nNo missing values in the dataset.")
### 🤖 Explain It

In your own words: why is it worth running `.info()` and `.isnull().sum()` on a dataset *before* you start analyzing it, rather than jumping straight to the questions you actually care about?
`Answer: It's worth running df.info() and df.isnull().sum() before analyzing a dataset because they help you understand the data's structure and identify data quality issues. df.info() shows column names, data types, non-null counts, and memory usage, while df.isnull().sum() shows how many missing values are in each column.

Checking these first helps you catch problems such as incorrect data types, missing values, or unexpected columns before they affect your analysis. It also gives you a baseline so you can verify that your cleaning steps worked correctly.`
---

## 🎯 Section 3: Indexing and Selection

6. Rewrite this using `.loc[]` instead of bracket + `.iloc[]` mixed together — or explain why you can't mix them the way it's written:
```python
df.iloc[df['Age'] < 10]  # this is actually broken — why?
```
   `Answer:` .iloc[] uses integer positions (0, 1, 2, ...), while df['Age'] < 10 creates a Boolean mask. Therefore df.iloc[df['Age'] < 10] is invalid. The correct code is: df.loc[df['Age'] < 10]

7. What's wrong with `df[df['Age'] < 10 and df['Fare'] > 100]`, and how would you fix it?  
   `Answer:`The problem is that Pandas does not use Python's and and or operators for combining Series conditions. Use & for "and" and put each condition in parentheses: df[(df['Age'] < 10) & (df['Fare'] > 100)]

8. Rewrite `df[(df['Pclass'] == 1) | (df['Pclass'] == 2)]` with `.isin()`. Why is `.isin()` easier to read when there are five values to match instead of two?  
   `Answer:` .isin() checks whether values belong to a list of allowed values. It's easier to read and maintain because you don't have to repeat the column name and multiple | conditions.

---

### ✏️ Task: Titanic Slicing

```python
# Using titanic.csv:
# 1. Select passengers in 3rd class (Pclass == 3) who survived (Survived == 1).
# 2. Of those, show only the Name, Age, and Fare columns.
# 3. Sort the result by Fare, descending.
```
result = (
    titanic.loc[
        (titanic['Pclass'] == 3) & (titanic['Survived'] == 1),
        ['Name', 'Age', 'Fare']
    ]
    .sort_values(by='Fare', ascending=False)
)

print(result)
### 🤖 Explain It

In your own words: why does `df.iloc[df['Age'] < 10]` not work, when `df.loc[df['Age'] < 10]` and `df[df['Age'] < 10]` both do?
`df.iloc[df['Age'] < 10] does not work because .iloc[] expects integer position indexes (0, 1, 2, ...), but df['Age'] < 10 produces a Boolean Series (True/False values).`
---

## 🧼 Section 4: Cleaning

9. If a column has the values `['25', 'thirty', '35']`, what happens when you run `pd.to_numeric(col, errors='coerce')` on it?  
   `Answer:` ['25', 'thirty', '35'] becomes approximately [25, NaN, 35], with the invalid value 'thirty' converted to NaN.

10. When would you choose `.dropna()` over `.fillna()`, and vice versa?  
   `Answer:`Use .dropna() when missing values are few or when rows/columns with missing data are not useful for your analysis. Use .fillna() when you want to keep the data and replace missing values with something meaningful, such as 0, the mean, median, or a placeholder value.

11. A survey stores missing ages as `-1`. Why is that *worse* for analysis than a blank (`NaN`), and what one-line fix turns them into real missing values?  
   `Answer:` Using -1 to represent a missing age is worse than using NaN because Pandas treats -1 as a real number. As a result, calculations such as .mean(), .median(), .min(), and other statistics will include -1 and produce misleading results. NaN is recognized as missing data and is automatically ignored by most Pandas calculations.

12. Two rows share an `order_id` but have different amounts. Will `df.drop_duplicates()` remove one? What argument makes it compare only `order_id`?  
   `Answer:` df.drop_duplicates() will not remove one of the rows if they differ in another column. Use subset=['order_id'] to check duplicates based only on order_id.
---

### ✏️ Task: Clean a Column

```python
# Using ufo.csv:
# 1. Check .isnull().sum() for the whole dataset.
# 2. Pick the column with the most missing values.
# 3. Decide (and justify in a comment) whether dropping or filling makes more
#    sense for that specific column, then do it.
```
import pandas as pd

# Load the dataset
ufo = pd.read_csv("ufo.csv")

# 1. Check missing values
missing = ufo.isnull().sum()
print("Missing values by column:")
print(missing.sort_values(ascending=False))

# 2. Find the column with the most missing values
most_missing_col = missing.idxmax()
most_missing_count = missing.max()

print(f"\nColumn with the most missing values: {most_missing_col}")
print(f"Missing values: {most_missing_count}")

# 3. Clean that column
decision: If this column is mostly descriptive text (e.g., comments), filling with 'Unknown' preserves rows. If it is missing in many records and isn't essential, dropping may be reasonable.

ufo[most_missing_col] = ufo[most_missing_col].fillna("Unknown")

print("\nMissing values after cleaning:")
print(ufo[most_missing_col].isnull().sum())
### 🤖 Explain It

In your own words: why might dropping rows with missing data be a bad idea if a large fraction of your dataset has at least one missing value somewhere?
`Dropping rows with missing data can be a bad idea when a large fraction of the dataset contains missing values because you may lose a significant amount of data. This can reduce your sample size, decrease statistical power, and potentially introduce bias if the missing values are not random. Instead of immediately dropping rows, you should first investigate why the data is missing and consider methods such as filling missing values with appropriate estimates (mean, median, mode, or other techniques) when appropriate.`
---

## 🧱 Section 5: Column Operations, Sorting, and Filtering

13. What's the difference between `df.rename(columns={'a': 'b'})` and `df.columns = ['b', 'c', 'd']`?  
   `Answer:` df.rename(columns={'a': 'b'}) renames only the specified column(s). In this example, column 'a' becomes 'b', and all other column names stay the same. df.columns = ['b', 'c', 'd'] replaces the entire list of column names at once. The number of names provided must exactly match the number of columns in the DataFrame.
14. Rewrite this bracket-filter as a `.query()` call:
```python
df[(df['math_score'] >= 80) & (df['science_score'] >= 80)]
```
   `Answer:` df.query("math_score >= 80 and science_score >= 80")


15. If `status` is a brand-new column, what do the rows with `score >= 70` contain after `df.loc[df['score'] < 70, 'status'] = 'review'`? How do you give every row a default first?  
   `Answer:` 
df['status'] = 'pass'
df.loc[df['score'] < 70, 'status'] = 'review'

---

### ✏️ Task: Build a Feature

```python
# Using students.csv:
# 1. Create a "total_score" column (math + science).
# 2. Sort by total_score, descending.
# 3. Print just the top 3 students' first_name and total_score.
```
students['total_score'] = students['math_score'] + students['science_score']
students = students.sort_values('total_score', ascending=False)
students[['first_name', 'total_score']].head(3)
### ✏️ Task: Loop vs. Vectorized

```python
# Using students.csv:
# 1. Build a list of each student's total score with an .itertuples() loop.
# 2. Compute the same totals with one whole-column expression.
# 3. Confirm they match, then use %timeit to compare the two.
```
import pandas as pd

students = pd.read_csv('02-assignments/06-working_with_Data_Adv/students.csv')
# 1. Build totals with an .itertuples() loop
totals_loop = []

for row in students.itertuples(index=False):
    totals_loop.append(row.math_score + row.science_score)

# 2. Compute the same totals with a whole-column expression
totals_vectorized = (students['math_score'] + students['science_score']).tolist()

# 3. Confirm they match
print(totals_loop == totals_vectorized)
%timeit [row.math_score + row.science_score for row in students.itertuples(index=False)]
%timeit students['math'] + students['science']
Using %timeit to show the vectorized approach is faster.
### 🤖 Explain It

In your own words: what does "feature engineering" mean in the context of `total_score` or `average_score` — why create a new column instead of just computing the value fresh every time you need it?
Feature engineering means creating new variables (features) from existing data that make analysis, reporting, or modeling easier and more useful. It is the process of creating new, useful columns from existing data. We create columns like total_score or average_score so we can reuse them easily, reduce errors, improve readability, and often improve analysis or modeling.
---

## 🧩 Section 6: Grouping and Combining

16. Describe the three steps of `df.groupby('Pclass')['Survived'].mean()` (split, apply, combine) in plain words. What does the result tell you?  
   `Answer:` df.groupby('Pclass')['Survived'].mean() follows the split → apply → combine pattern:
Split:

Pandas splits the passengers into groups based on their Pclass value.
One group for 1st class, one for 2nd class, and one for 3rd class.

Apply:

For each group, Pandas calculates the mean of the Survived column.
Since Survived is usually coded as:
1 = survived
0 = did not survive
The mean is the proportion of passengers who survived.

Combine:

Pandas combines the results into a new Series with one value per passenger class.

17. What's the difference between `pd.concat()` and `.merge()`, and between a `'left'` and an `'inner'` merge?  
   `Answer:` pd.concat(): combines DataFrames by stacking them together.
.merge(): joins DataFrames using matching key columns.
how='left': keep all rows from the left DataFrame.
how='inner': keep only rows with matching keys in both DataFrames.

---

### ✏️ Task: Survival by Group

```python
# Using titanic.csv:
# 1. Find the survival rate by Pclass, then by Pclass AND Sex together.
# 2. Use .agg() to show, per Embarked port: passengers, average Fare, survival rate.
# 3. .reset_index() the result and sort it by survival rate, highest first.
```
# 1. Survival rate by Pclass
print(
    titanic.groupby('Pclass')['Survived'].mean()
)

# Survival rate by Pclass and Sex
print(
    titanic.groupby(['Pclass', 'Sex'])['Survived'].mean()
)

# 2. Per Embarked port: passengers, average Fare, survival rate
embarked_stats = (
    titanic.groupby('Embarked')
           .agg(
               passengers=('PassengerId', 'count'),
               average_fare=('Fare', 'mean'),
               survival_rate=('Survived', 'mean')
           )
)

# 3. Reset index and sort by survival rate (highest first)
embarked_stats = (
    embarked_stats
    .reset_index()
    .sort_values('survival_rate', ascending=False)
)

print(embarked_stats)

### ✏️ Task: Join Two Tables

```python
# Build a table of 5 students (student_id, name) and a table of 4 grades
# (student_id, grade), where one student has no grade.
# Merge them with how='left' and with how='inner'. How many rows does each give, and why?
```
import pandas as pd

# Students table (5 students)
students = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
})

# Grades table (4 grades)
grades = pd.DataFrame({
    'student_id': [1, 2, 3, 4],
    'grade': ['A', 'B', 'A', 'C']
})

# Left merge
left_merge = students.merge(grades, on='student_id', how='left')
print(left_merge)

# Inner merge
inner_merge = students.merge(grades, on='student_id', how='inner')
print(inner_merge)

print("Left merge rows:", len(left_merge))
print("Inner merge rows:", len(inner_merge))
# merge left shows the results
   student_id     name grade
0           1    Alice     A
1           2      Bob     B
2           3  Charlie     A
3           4    David     C
4           5     Emma   NaN

# inner merge results
   student_id     name grade
0           1    Alice     A
1           2      Bob     B
2           3  Charlie     A
3           4    David     C
Left merge rows: 5
Inner merge rows: 4

### 🤖 Explain It

In your own words: when you merge UFO sightings (state codes like `'tx'`) with populations (codes like `'TX'`), every state fails to match at first. Why, and what does that teach you about checking keys *before* you join?
`The merge fails because 'tx' and 'TX' are not identical strings. This teaches you to always validate and standardize your join keys before merging, otherwise matching records can be missed even when they represent the same thing.`
---

## 🧾 Submit Checklist

- [X] I created a `Series` and a `DataFrame` from Python containers (a dictionary or a list of dictionaries).
- [X] I loaded a local CSV into a DataFrame and inspected it with `.info()` and `.describe()`.
- [X] I used both `.loc[]` and `.iloc[]` at least once each.
- [X] I filtered a DataFrame using a compound condition (`&` or `|`).
- [X] I cleaned at least one column with `.fillna()`, `.dropna()`, or `pd.to_numeric()`.
- [X] I created a new column and sorted by it.
- [X] I removed duplicate rows or replaced a placeholder value with `NaN`.
- [X] I filtered with `.isin()`, `.between()`, or `.str.contains()`.
- [X] I used a whole-column (vectorized) calculation instead of a row-by-row loop.
- [X] I summarized groups with `groupby()` (and `.agg()`), and combined tables with `pd.concat()` or `.merge()`.
- [X] I completed the "Explain It" prompts in my own words.
