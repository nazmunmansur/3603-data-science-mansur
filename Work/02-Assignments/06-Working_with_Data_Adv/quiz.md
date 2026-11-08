# 📝 Quiz: 06 - Working with Data (Advanced)

47 questions covering Pandas Series/DataFrames, loading/exploring data, indexing/selection, cleaning, column operations, sorting/filtering/searching, grouping and combining tables, and a "going further" bonus. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first — the Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Series and DataFrames

**1.** (Short Answer) What's the difference between a Pandas `Series` and a `DataFrame`?
` A Series is a one-dimensional collection of data (like a single column), while a DataFrame is a two-dimensional table with rows and columns.`
**2.** (Code Tracing) What prints?
```python
s = pd.Series({'a': 1, 'b': 2})
print(s['a'])
```
` 1 `
**3.** (Short Answer) What does `df.shape` return?
` The dimensions of the dataframe. df.shape returns a tuple containing the number of rows and columns in the DataFrame, in the format (rows, columns).`
**4.** (Short Answer) If you add two `Series` together and one has a label the other doesn't, what happens at that label?
` When you add two Series, Pandas aligns them by their index labels. If one Series has a label that the other does not, the result for that label will be NaN.`
**5.** (Short Answer) You have a list of dictionaries, one per student (the way you stored records in Module 03b). What does `pd.DataFrame(that_list)` turn each dictionary into?
` # pd.DataFrame(list_of_dicts) turns each dictionary into a row, with the dictionary keys becoming column names.`
**6.** (Code Tracing) What prints?
```python
scores = pd.Series([70, 95, 88])
print(scores[scores > 80].tolist())
```
`[95, 88]`
---

## Section B — Loading and Exploring Data

**7.** (Multiple Choice) Which method shows summary statistics (mean, std, min/max) for numeric columns?
A) `.head()`  B) `.columns`  C) `.describe()`  D) `.shape`

`Answer: C) `.describe()``
**8.** (Short Answer) What's the difference between what `.head()` and `.info()` each tell you about a DataFrame?
`.head() shows the first few rows of a DataFrame (by default, the first 5), while .info() provides summary information about the DataFrame, including the number of rows and columns, column names, data types, and non-null counts.`
**9.** (Short Answer) How do you count how many missing values are in *each column* of a DataFrame?
` Use df.isna().sum() to count the number of missing values in each column.`
**10.** (Short Answer) What do `df.duplicated().sum()` and `df['col'].value_counts(dropna=False)` each tell you?
` df.duplicated().sum() returns the number of duplicate rows in the DataFrame.It does not count duplicate values within a column.
df['col'].value_counts(dropna=False) returns the frequency of each value in the column, including missing values (NaN) because of dropna=False.It shows how many times each value appears, not just duplicates.`
**11.** (Short Answer) Titanic's `Age` column holds whole numbers, but its dtype is `float64`. Why?
`The main reason is that Age contains missing values (NaN). In pandas, a regular integer column cannot store NaN, so when a column has both whole numbers and missing values, pandas automatically uses the float64 dtype because floating-point columns can represent NaN.`
---

## Section C — Indexing and Selection

**12.** (Short Answer) What's the difference between `.loc[]` and `.iloc[]`?
`.loc[] selects rows and columns by their labels (names) and .iloc[] selects rows and columns by their integer positions.`
**13.** (Short Answer) Is `df.loc[0:4]` inclusive or exclusive of row `4`? What about `df.iloc[0:4]` and position `4`?
`df.loc[0:4] includes row label 4 as .loc[] uses labels and includes both endpoints when slicing. df.iloc[0:4] excludes position 4 and returns positions 0, 1, 2, and 3. As .iloc[] uses integer positions and follows normal Python slicing rules, where the stop value is excluded.`
**14.** (Short Answer) What symbols does Pandas require for combining conditions when filtering a DataFrame (instead of the `and`/`or` keywords)?
` Use & for AND and | for OR when combining conditions in Pandas. `
**15.** (Short Answer) What does `df[df['Age'] < 10]` return?
` df[df['Age'] < 10] does not return just the Age column. It returns a filtered DataFrame containing all columns for the rows where Age < 10.`
**16.** (Short Answer) Rewrite `df[(df['Embarked'] == 'C') | (df['Embarked'] == 'Q')]` using `.isin()`. Does `df['Age'].between(13, 19)` include ages 13 and 19?
` df[df['Embarked'].isin(['C', 'Q'])]`
**17.** (Multiple Choice) Which one returns a `DataFrame` rather than a `Series`?
A) `df['Age']`  B) `df[['Age']]`  C) `df.Age`  D) `df.loc[0]`
`B) `df[['Age']]``
**18.** (Short Answer) After `by_id = df.set_index('PassengerId')`, what does `by_id.loc[2]` select, and how is that different from `df.loc[2]`?
`After set_index('PassengerId'), by_id.loc[2] selects the row whose PassengerId is 2. In contrast, df.loc[2] selects the row with index label 2 in the original DataFrame, which is usually the third row if the default index is being used. It is not looking up PassengerId = 2 unless the DataFrame's index already happens to be PassengerId.`
**19.** (Code Tracing) After `by_id = titanic.set_index('PassengerId')`, do `by_id.loc[3]` and `by_id.iloc[3]` select the same passenger? Why or why not?
`by_id.loc[3] selects the row whose PassengerId is 3 (because .loc[] uses index labels) and by_id.iloc[3] selects the 4th row by position (because .iloc[] uses integer positions starting at 0).`
**20.** (Short Answer) Write a filter for passengers who did **not** board at Southampton (`'S'`), using `~` and `.isin()`.
`titanic[~titanic['Embarked'].isin(['S'])]`
**21.** (Short Answer) What's wrong with `df[df['Age'] < 10]['child'] = True`, and what should you write instead?
`df[df['Age'] < 10]['child'] = True uses chained indexing and may not update the original DataFrame. Use: df.loc[df['Age'] < 10, 'child'] = True`
---

## Section D — Cleaning

**22.** (Short Answer) What's the difference between `.dropna()` and `.fillna()`?
`.dropna() removes rows (or columns) that contain missing values and .fillna() replaces missing values with a specified value.`
**23.** (Short Answer) What does `pd.to_numeric(col, errors='coerce')` do to a value like `'ninety'` in that column?
`pd.to_numeric(..., errors='coerce') converts invalid numeric values like 'ninety' to NaN.`
**24.** (True/False) `NaN` and an empty string `""` are always treated identically by `.isnull()`.
` False`
**25.** (Short Answer) Two rows have the same `order_id` but different `amount`s. Does `df.drop_duplicates()` remove one of them? What would you write to keep only the last row for each `order_id`?
`No. df.drop_duplicates() will not remove one of the rows because the amounts are different, so the rows are not identical. To keep only the last row for each order_id:
df.drop_duplicates(subset='order_id', keep='last')`
**26.** (Short Answer) A survey stores missing ages as `-1`. Why is that a problem for `df['age'].mean()`, and how do you fix it?
`-1 is not a valid age, but .mean() will treat it as a real number, making the average age too low. Replace -1 with NaN (or pd.NA) before calculating the mean.`
**27.** (Short Answer) A date column holds `'2022-01-01'`, `'2022/03/01'`, and `'April 5, 2022'`. Why can `pd.to_datetime(col, errors='coerce')` turn two perfectly valid dates into `NaT`, and how do you fix it?
`Valid dates can become NaT when their format doesn't match what pd.to_datetime() expects. Fix this by cleaning the values and/or letting Pandas infer the date format with pd.to_datetime(col, errors='coerce').`
**28.** (Short Answer) Why does `.astype('int64')` fail on a column with missing values, while `.astype('Int64')` works?
`.astype('int64') fails because regular int64 cannot store missing values and .astype('Int64') works because it is Pandas' nullable integer type and can represent missing values as <NA>.`
**29.** (Short Answer) Before deleting rows with a repeated `order_id`, why would you look at `df[df.duplicated(subset=['order_id'], keep=False)]` first?
`Before deleting duplicates, you should inspect them to make sure the repeated order_id rows are actually duplicates and not records with different information. This helps you decide whether it's safe to remove them and which row (first or last) should be kept.`
---

## Section E — Column Operations, Sorting, Filtering, and Searching

**30.** (Short Answer) How do you create a new column that's the sum of two existing numeric columns?
`Create a new column by adding the two columns together.
df['total'] = df['math'] + df['science']`
**31.** (Short Answer) What does `.apply()` do that you could also do with a `for` loop over rows — and why is `.apply()` usually preferred?
`.apply() applies a function to each value in a Series (or row/column in a DataFrame), similar to looping through the data with a for loop. It is usually preferred because the code is shorter, cleaner, and easier to read.`
**32.** (Short Answer) What does `ascending=False` do inside `df.sort_values(by='score', ascending=False)`?
`ascending=False sorts the values from largest to smallest (descending order).`
**33.** (Short Answer) What's the main advantage of `.query()` over bracket-based boolean filtering (`df[df['col'] > 5]`)?
`.query() provides a cleaner, more readable way to filter DataFrames, especially when using multiple conditions across columns.`
**34.** (Code Tracing) `bonus` is a brand-new column. What value do the rows with `score >= 80` get in it?
```python
df.loc[df['score'] < 80, 'bonus'] = 5
```
`Rows with score >= 80 get NaN in the bonus column.`
**35.** (Short Answer) To compute `price * qty` for every row, why should you write `df['price'] * df['qty']` instead of looping with `.iterrows()`? When *is* a loop (preferably `.itertuples()`) the right tool?
`df['price'] * df['qty'] performs the calculation on the entire columns at once (vectorization), making the code shorter, easier to read, and much faster than looping with .iterrows(). A loop (preferably .itertuples()) is appropriate when the logic cannot be easily expressed with vectorized operations, such as complex row-by-row processing that depends on multiple columns or external functions.`
**36.** (Short Answer) What do `case=False` and `na=False` each do in `df['name'].str.contains('an', case=False, na=False)`?
`case=False makes the search case-insensitive, so it matches 'an', 'An', 'AN', etc and na=False treats missing values (NaN) as False instead of returning NaN, so rows with missing names are not included in the match.`
**37.** (Code Tracing) A student has `math = 95` and `average = 91`. What is their `award` after these three lines, and what would it be if the last two lines were swapped?
```python
df['award'] = 'None'
df.loc[df['average'] >= 85, 'award'] = 'Honor Roll'
df.loc[df['math'] >= 90, 'award'] = 'Math Star'
```
`The student's award is 'Math Star' in the original code. If the last two lines are swapped, it becomes 'Honor Roll' because the later assignment overwrites the earlier one.`
**38.** (Short Answer) What does `pd.cut(df['score'], bins=[0, 70, 90, 101], labels=['Low', 'Mid', 'High'], right=False)` do, and why is it usually better than `.apply()` with an `if`/`elif` function for the same job?
`pd.cut() groups numeric values into ranges (bins) and assigns labels to each range. In this example, scores from 0-69 become 'Low', 70-89 become 'Mid', and 90-100 become 'High' (because right=False makes the right endpoint excluded). It's usually better than .apply() with an if/elif function because it is vectorized, faster, shorter, and easier to maintain for binning large datasets.`
**39.** (Short Answer) What's the difference between `df.query('math_score >= minimum')` and `df.query('math_score >= @minimum')`?
`In .query(), minimum is treated as the name of a column in the DataFrame, while @minimum refers to the Python variable named minimum outside the DataFrame.`
**40.** (Code Tracing) What does each line return, and why are they different?
```python
books = pd.Series(['C++ Primer', 'C Programming'])
books.str.contains('C++').tolist()
books.str.contains('C++', regex=False).tolist()
```
str.contains('C++') treats 'C++' as a regular expression, while str.contains('C++', regex=False) treats it as a literal string. Therefore, the first may match more strings than expected, while the second matches only strings that actually contain "C++".
---

## Section F — Grouping and Combining

**41.** (Code Tracing) What does this return?
```python
df = pd.DataFrame({'team': ['A', 'B', 'A', 'B'], 'points': [10, 4, 20, 6]})
df.groupby('team')['points'].mean()
```
team
A    15.0
B     5.0
Name: points, dtype: float64
**42.** (Short Answer) Write a `groupby` with `.agg()` that gives, for each `team`, the number of rows and the total `points`, as columns named `games` and `total`.
df.groupby('team').agg(
    games=('team', 'size'),
    total=('points', 'sum')
)
**43.** (Short Answer) When would you use `pd.concat()` instead of `.merge()`? What does `ignore_index=True` do?
`Use pd.concat() when you want to stack DataFrames together (add rows or columns), such as combining monthly sales files that have the same structure. Use .merge() when you want to join related DataFrames based on a common key, similar to a SQL join.`
**44.** (Short Answer) In `orders.merge(prices, on='product_id', how='left')`, what happens to an order whose `product_id` isn't in `prices`? What would `how='inner'` do instead? And why does a merge on state codes fail when one table uses `'tx'` and the other uses `'TX'`?
`With how='left', all rows from orders are kept. If an order's product_id is not found in prices, the columns coming from prices will contain NaN for that order. With how='inner', only rows with matching product_id values in both DataFrames are kept. Therefore, those rows do not match during the merge. In a left join, the unmatched row gets NaN values from the other table; in an inner join, the row is dropped.`
**45.** (Short Answer) In Titanic, `groupby('Pclass').size()` gives 216 for 1st class, but `groupby('Pclass')['Age'].count()` gives 186. Why are they different?
`groupby('Pclass').size() counts all rows in each passenger class, while groupby('Pclass')['Age'].count() counts only non-missing Age values.`
**46.** (Short Answer) `purchases` has 6 rows. After `purchases.merge(buyers, on='buyer_id', how='left')`, it has 8. What probably happened, and how can `validate=` protect you?
`The merge probably duplicated rows because a buyer_id appeared more than once in buyers. Using validate='many_to_one' (or another appropriate validation) helps catch unexpected duplicate keys before they corrupt your analysis.`
---

## Section G — Going Further (Bonus)

**47.** (Short Answer) What do the `usecols` and `nrows` arguments to `pd.read_csv()` do, and when would you reach for them?
`usecols tells pd.read_csv() to load only specific columns, while nrows limits how many rows are read. They are useful when working with large datasets because they reduce memory usage, speed up loading, and let you focus only on the data needed for analysis.`
