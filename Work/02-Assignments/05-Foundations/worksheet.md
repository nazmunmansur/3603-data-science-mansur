# 📝 Worksheet: 06 - Foundations

Use this worksheet to reinforce the Jupyter/IPython tooling skills from this module. There's one section per notebook, in order. Each section ends with an **🤖 Explain It** prompt. Write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧙 Section 1: Magic Commands (01)

1. What magic command lists every variable currently in memory, along with its type?  
   `Answer:` %whos

2. What's the difference between a line magic (`%pwd`), a cell magic (`%%writefile`), and a shell command (`!ls`)?  
   `Answer:` %pwd is a line magic that affects one line, %%writefile is a cell magic that processes an entire cell, and !ls is a shell command that runs a command in the operating system.

3. Why does `%cd ..  # go up` fail, and how do you fix it?  
   `Answer:` %cd .. fails when there is no accessible parent directory (or the path is invalid). Fix it by changing to a valid existing directory or ensuring you're not already at the root directory.

---

### ✏️ Task: Write, Run, and Reload

```python
# Use %%writefile to create tools.py containing a function shout(text)
```python
%%writefile tools.py

def shout(text):
    return text.upper() + "!"
    ```
# that returns text in uppercase with "!" on the end.
# Turn on %load_ext autoreload and %autoreload 2, then import tools and call shout().
```python
%load_ext autoreload
%autoreload 2```
# Rewrite tools.py so shout() adds "!!!" instead, and call it again WITHOUT restarting.
```
```python
%%writefile tools.py

def shout(text):
    return text.upper() + "!!!"
    ```
tools.shout("hello")
```
### 🤖 Explain It

In your own words: why can `!pip install` "succeed" while `import` still fails with `ModuleNotFoundError`? Why does `%pip` avoid the problem?

---```!pip install runs a shell command. Sometimes it installs the package into a different Python environment than the one the notebook kernel is using. As a result, the installation appears to succeed, but import fails with ModuleNotFoundError because the notebook's Python can't find the package.

%pip install installs the package into the same Python environment that the current Jupyter kernel is using, so the package is available for import immediately and avoids environment mismatches.```

## ⚡ Section 2: Jupyter Workflow (02)

4. What are the two Jupyter cell modes, and what key switches to each?  
   `Answer:` The two Jupyter cell modes are Command Mode and Edit Mode.
- Press Enter to switch from Command Mode to Edit Mode (so you can edit a cell).
- Press Esc to switch from Edit Mode to Command Mode (so you can run notebook shortcuts like A, B, DD, etc.).

5. What do the numbers in `[3]`, `[4]`, `[12]` next to code cells tell you, and what *don't* they tell you?  
   `Answer:` ```The numbers in [3], [4], [12] are the execution counts. They show the order in which cells were run by the kernel.
They do tell you:
Which cell was executed first, second, etc.
Whether cells were run out of order (for example, [12] above [4]).

They do not tell you:
The order of cells in the notebook.
Whether the notebook was run from top to bottom.
How long a cell took to run.
Whether the code is correct.```
6. A cell's code ends with three expressions on three lines. How many of their values are displayed?  
   `Answer:` 3 values.

---

### ✏️ Task: Shortcut Drill

```
Using only the keyboard (no mouse):
- Insert 2 new cells below this one.
- Turn one into a Markdown cell and the other into a Code cell.
- Move the Code cell above the Markdown cell.
- Delete the Markdown cell, then undo the deletion.
- Run the Code cell.
```
Press B twice to insert 2 new cells below.
Select one cell and press M to make it a Markdown cell.
Select the other cell and press Y to make it a Code cell.
Select the Code cell and press Ctrl+Shift+Up (or use X then V above the Markdown cell, depending on your Jupyter version) to move it above the Markdown cell.
Select the Markdown cell and press D D to delete it.
Press Z to undo the deletion and restore the Markdown cell.
Select the Code cell and press Shift+Enter (or Ctrl+Enter) to run it.
### ✏️ Task: Break It, Then Fix It

```python
# In three separate cells, IN THIS ORDER, type:
#   print(area)
#   width, height = 4, 5
#   area = width * height
# Get it to work by running cells out of order. Then Restart & Run All,

it shows a "NameError: name 'area' is not defined'" as the variable area is not defined previously.
```python
area = width * height
width, height = 4, 5
print(area)
# watch it fail, and fix the ORDER so it runs top to bottom.
```
Now it is showing the answer 20.
A notebook should run correctly from top to bottom after a kernel restart, without relying on variables left in memory from earlier executions.
### 🤖 Explain It

In your own words, using the "recipe and kitchen" idea: why can a notebook look correct on your screen and still fail for your grader?

---The notebook may work on my computer because variables are already stored in memory from earlier cell executions. The grader starts with a fresh kernel, so if the cells are not in the correct order, the notebook fails even though it looked correct on my screen.

## 📚 Section 3: Getting Help (03)

7. What's the difference between `help(len)` and `len?`? Which one also works in a plain `.py` script?  
   `Answer:` help(len) and len? both show documentation for len, but len? is an IPython/Jupyter shortcut. help(len) also works in a normal .py script.

8. In the signature `round(number, ndigits=None)`, which argument is required and which is optional? What's the optional one's default?  
   `Answer:` round(number, ndigits=None): number is the required argument because it has no default value. ndigits is the optional argument because it has a default value.
The default value of ndigits is None.

9. Name the error type for each: `'5' + 5`, `int('hello')`, `[1, 2][5]`, `{'a': 1}['b']`.  
   `Answer:` _______________________
'5' + 5      #TypeError
int('hello') # ValueError
[1, 2][5]    # IndexError
{'a': 1}['b'] # KeyError
---

### ✏️ Task: Investigate Without Searching

```python
# Using only ?, Tab/IntelliSense, dir(), and help() (no web searching):
# 1. Find a string method that checks whether a string contains only digits.
dir(str)
"12345".isdigit()
```True```
"123cv".isdigit()
```False```
# 2. Use a wildcard search (np.*sum*?) to list NumPy functions with "sum" in the name.
np.*sum*?
```#list of functions
np.cumsum
np.cumulative_sum
np.einsum
np.einsum_path
np.nancumsum
np.nansum
np.sum```
# 3. Find out whether np.random.randint's upper limit is included. Prove it with code.
```
```
import numpy as np

nums = np.random.randint(1, 5, size=10000)

print(nums.min())
print(nums.max())
print(5 in nums)```
```prints out: 1
4
False```
### 🤖 Explain It

In your own words: when would you reach for `?` versus `??` versus `help()` versus `dir()` versus the official docs? Is there a natural order you'd try them in?

---
```
dir() → discover what's available.
? → quick documentation and function signature.
?? → deeper details or source code (when available).
help() → more complete built-in documentation.
Official docs → full explanations, examples, and advanced usage.```
## 📝 Section 4: Markdown (04)

10. What's the difference between `*italic*` and `**bold**` in Markdown?  
    `Answer:` *italic* makes text italic, while **bold** makes text bold. The difference is the number of asterisks used.

11. Write the Markdown for a 2-item bulleted list where the second item has its own sub-bullet.  
    `Answer:` 
```
- Python
- Jupyter Notebook
   * Select Kernel```

12. How do you show a literal price like `$5` in Markdown without it turning into math?  
    `Answer:`escape it with a backslash_

---

### ✏️ Task: Mini Report

```markdown
# Write a Markdown cell with:
# - a level-2 heading
# - a short paragraph with a line break in the middle
# - a 3-item list
# - one inline LaTeX expression (try the mean, \bar{x})
# - a small table with a right-aligned number column
```
## Meann of Numbers
mean of numbers can be calcu;lated by the sum of the numbers divided by the length of the numbers. It is very useful Statistical tool.Mean is also called average.  <br> An example will be getting the average score of three students. <br> Nancy = 98, Ben = 88, Alice = 95. <br>
$\bar{x}$  = Sum of Scores / Len of scores
<br>

|Name | Score|
|-----|------:|
|Nancy | 98|
|Ben | 88|
|Alice | 95|
### 🤖 Explain It

In your own words: what's lost if you write an entire notebook as code + comments only, with no Markdown cells at all? When would *generating* Markdown from code (`display(Markdown(...))`) be better than typing it?

---If a notebook contains only code and comments, it loses the story and explanation of the work. Markdown cells help explain the purpose of the analysis, describe the steps, interpret the results, and make the notebook easier for other people (and your future self) to understand. Without Markdown, the notebook can be harder to read and follow.

Generating Markdown with display(Markdown(...)) is better when the text needs to change automatically based on the code's output. For example, you might create a report that inserts the current date, dataset statistics, model results, or conclusions computed by the notebook. Typed Markdown is better for static explanations that don't change.

## 📂 Section 5: Files and Paths (05)

13. What does the `with` keyword do when you open a file, and why is it preferred over a plain `open()`/`.close()` pair?  
`Answer:` The with keyword creates a context manager that automatically handles opening and closing a file. When the code inside the with block finishes, Python closes the file for you, even if an error occurs.

It is preferred over a plain open()/close() pair because you don't have to remember to call .close(), which helps prevent resource leaks and files being left open.

14. What's the difference between modes `'w'`, `'a'`, and `'x'`?  
    `Answer:`'w' (write mode): Creates a new file or overwrites an existing file.
'a' (append mode): Adds new content to the end of an existing file without erasing its current contents.
'x' (exclusive create mode): Creates a new file only. If the file already exists, Python raises a FileExistsError.

15. For `Path('reports') / 'final.pdf'`, what are the `.name`, `.stem`, `.suffix`, and `.parent`?  
    `Answer:` .name → 'final.pdf'
.stem → 'final'
.suffix → '.pdf'
.parent → Path('reports') (the reports folder)

---

### ✏️ Task: Build, Save, Reload

```python
# Create a dictionary describing yourself (name, major, hobbies as a list).
# Save it to a JSON file with indent=2 (use pathlib to build the path).
# Read it back into a NEW variable and confirm it matches the original with ==.
# Then add a tuple to the dictionary and repeat. Does it still match? Why not?
```
# Create a dictionary describing yourself
from pathlib import Path
import json

my_info = {
    "name": "Nancy",
    "major": "Data Analytics",
    "hobbies": ["reading", "coding", "traveling"]
}

# Build path with pathlib
path = Path("my_info.json")

# Save to JSON with indent=2
with open(path, "w") as file:
    json.dump(my_info, file, indent=2)

# Read into a new variable
with open(path, "r") as file:
    loaded_info = json.load(file)

# Confirm match
print(my_info == loaded_info)  # True

# Add a tuple
my_info["location"] = (33.9, -98.5)

# Save again
with open(path, "w") as file:
    json.dump(my_info, file, indent=2)

# Read again
with open(path, "r") as file:
    loaded_info_2 = json.load(file)

# Compare
print(my_info == loaded_info_2)  # False
```
Shows True after running the code. 
```
True
False
```
### ✏️ Task: Find Files

```python
# Write three small .txt files into a folder using a loop.
# Use glob('*.txt') to find them WITHOUT typing their names, and print each
# file's name and size in bytes.
```
from pathlib import Path

# Create a folder
folder = Path("text_files")
folder.mkdir(exist_ok=True)

# Write three text files using a loop
for i in range(1, 4):
    file_path = folder / f"file{i}.txt"
    with open(file_path, "w") as f:
        f.write(f"This is file {i}")

# Find all .txt files and print name and size
for file_path in folder.glob("*.txt"):
    print(file_path.name, "-", file_path.stat().st_size, "bytes")
```prints out:
file1.txt - 14 bytes
file2.txt - 14 bytes
file3.txt - 14 bytes```
### 🤖 Explain It

In your own words: why does `csv.reader` give you `'90'` instead of `90`, and why does splitting a CSV line on `','` break on a value like `"Smith, John"`?

---csv.reader returns values like '90' as strings because CSV files store data as text. The CSV format doesn't know whether 90 is supposed to be a number, a ZIP code, an ID, or plain text, so Python reads everything as strings by default.

Splitting a CSV line with ',' is unreliable because commas can appear inside quoted fields.

## 📊 Section 6: Data Input and Output (06)

16. Name three things `.info()` tells you about a DataFrame that `.head()` doesn't.  
`Answer:` .info() tells you several things that .head() does not, including:

Column names and the number of non-null values in each column.
Data types (dtype) of each column (e.g., int64, float64, object).
Memory usage of the DataFrame.

17. What does `index=False` do in `df.to_csv(...)`, and what happens if you forget it?  
    `Answer:` index=False tells pandas not to write the DataFrame's index column to the CSV file.

18. When would you use `pd.json_normalize()` instead of `pd.read_json()`?  
    `Answer:` Use pd.read_json() when the JSON data is already in a tabular format that can be loaded directly into a DataFrame.

Use pd.json_normalize() when the JSON contains nested dictionaries or lists and you want to flatten that nested structure into columns.
---

### ✏️ Task: CSV Round Trip

```python
# Create a small DataFrame from a dictionary of lists (use pd.DataFrame(your_dict)).
# Save it to a CSV, then read that CSV back into a new DataFrame.
# Use .equals() to confirm the reloaded DataFrame matches the original.
```
import pandas as pd

# Create a DataFrame from a dictionary of lists
data = {
    "Name": ["Nancy", "Alice", "John"],
    "Age": [25, 22, 27],
    "City": ["Wichita Falls", "Dallas", "Austin"]
}
df_original = pd.DataFrame(data)
# Save the DataFrame to a CSV file
df_original.to_csv("customers.csv", index=False)
# Read the CSV back into a new DataFrame
df_reloaded = pd.read_csv("customers.csv")
# Check whether the two DataFrames are identical
print(df_original.equals(df_reloaded))
```
shows True after running the code.
### ✏️ Task: Convert Between Formats

```python
# Take the same DataFrame and save it as JSON (orient='records') and as Excel.
# Read the Excel file back and convert it to a CSV.
# Print the raw text of the JSON and CSV files and compare them.
```
# Save to Excel
df_original.to_excel("customers.xlsx", index=False)

# Read Excel back
df_excel = pd.read_excel("customers.xlsx")

# Convert Excel data to CSV
df_excel.to_csv("customers_from_excel.csv", index=False)

# Print raw JSON text
print("----- JSON FILE -----")
with open("customers.json", "r") as file:
    print(file.read())

# Print raw CSV text
print("\n----- CSV FILE -----")
with open("customers_from_excel.csv", "r") as file:
    print(file.read())

# Compare DataFrames
print("\nOriginal equals CSV Reloaded:",
      df_original.equals(df_reloaded))

print("Original equals Excel Reloaded:",
      df_original.equals(df_excel))
### 🤖 Explain It

In your own words: what information can get lost or changed when converting Excel → CSV, or CSV → DataFrame? Give two examples.

---When converting Excel → CSV or CSV → DataFrame, some information can be lost or changed because CSV only stores plain text values.

Example 1: Data types may change. A date, currency, or ZIP code in Excel might be read as a string or number in a DataFrame.

Example 2: Excel formatting is lost. Things like cell colors, bold text, formulas, multiple sheets, and charts are not saved in a CSV file.

## 📈 Section 7: Plotting with NumPy (07)

19. What's the difference between `[1, 2, 3] * 2` and `np.array([1, 2, 3]) * 2`?  
`Answer:` [1, 2, 3] * 2 duplicates the list and produces [1, 2, 3, 1, 2, 3], while np.array([1, 2, 3]) * 2 multiplies each element by 2 and produces array([2, 4, 6]). Lists repeat; NumPy arrays perform mathematical operations element-wise.

20. What does `plt.legend()` require in order to show meaningful labels (hint: think about the `plot()` calls before it)?  
`Answer:` plt.legend() needs the plotted lines to have labels. These labels are usually provided in the plot() calls using the label= argument.

21. Which chart would you use for: comparing categories, change over time, a relationship between two numbers, and the distribution of one number?  
`Answer:`
Comparing categories → Bar chart
Change over time → Line chart
Relationship between two numbers → Scatter plot
Distribution of one number → Histogram

---

### ✏️ Task: Compare Three Categories

```python
# Given: subjects = ["Math", "Science", "History"]
#        hours_studied = [5, 8, 3]
# Build a bar plot with a title and axis labels (with units).
# Save it to a PNG file, then display it.
```
import matplotlib.pyplot as plt

subjects = ["Math", "Science", "History"]
hours_studied = [5, 8, 3]

plt.bar(subjects, hours_studied)

plt.title('Hours Studied by Subject')
plt.xlabel('Subject')
plt.ylabel('Hours Studied (hours)')  # includes units

plt.legend(['Hours Studied'])

plt.savefig('subjects_studied.png')  # saving it first
plt.show()  # then dispaying thr plot
### ✏️ Task: Distribution

```python
# Generate 200 test scores with np.random.normal(75, 10, size=200).
# Plot a histogram and mark the mean with a vertical dashed line and a legend.
# Then show the same data as a box plot side by side, using subplots.
```
import numpy as np
import matplotlib.pyplot as plt

scores = np.random.normal(75, 10, size=200)
plt.boxplot([scores], tick_labels=['scores'])
plt.title('Exam Scores by Section')
plt.ylabel('Score')
plt.show()

### 🤖 Explain It

In your own words: why does a line plot make sense for `sin(x)` or monthly revenue but not for the categories `"Math"`, `"Science"`, `"History"`? What's different about the two kinds of data?

---A line chart is best for data that changes over a continuous scale or over time, such as sin(x) or monthly revenue. Connecting the points shows the trend between values. For categories like "Math", "Science", and "History", there is no continuous relationship between the categories, so connecting them with lines can be misleading. A bar chart is better because it compares the values of separate categories.

## ⏱️ Section 8: Timing and Performance (08)

22. What's the difference between `%time`, `%timeit`, `%%time`, and `%%timeit`?  
`Answer:` %time: Times a single line of code once and reports wall time (and CPU time when available).
%timeit: Runs a single line many times and reports the average/best execution time. This is more reliable for performance comparisons.
%%time: Times an entire cell once.
%%timeit: Runs an entire cell many times and reports the average/best execution time.

23. Name two things that make a timing comparison **unfair**.  
    `Answer:` Two things that make a timing comparison unfair are (1) including extra work in one version that the other version doesn't do, and (2) performing setup tasks such as sorting or data preparation inside the timed code instead of doing them beforehand. This means you're not measuring the same work in both tests.

24. What does `%prun` tell you that `%timeit` doesn't?  
    `Answer:` %prun provides profiling information, showing which functions or lines of code consume the most execution time and how many times they were called. %timeit only tells you the overall execution time of the code after running it multiple times. It does not show where the time was spent.
---

### ✏️ Task: Timing Comparison

```python
# Build a list of the first 500,000 integers, and a NumPy array of the same.
# Use %timeit -o to compare squaring the list with a comprehension
# vs. squaring the array (numbers ** 2).
# Confirm both give the same values, then print how many times faster NumPy is.
```
```
import numpy as np

numbers_list = list(range(500_000))
numbers_array = np.arange(500_000)

def square_with_loop(values):
    result = []
    for value in values:
        result.append(value ** 2)
    return result

def square_with_numpy(values):
    return values ** 2

# Verify results match
loop_result = square_with_loop(numbers_list)
numpy_result = square_with_numpy(numbers_array)

print(loop_result == numpy_result.tolist())

# Benchmark
t_loop = %timeit -o square_with_loop(numbers_list)
t_numpy = %timeit -o square_with_numpy(numbers_array)

print(f"NumPy is about {t_loop.average / t_numpy.average:.0f}x faster")
results:
True
32.4 ms ± 1.08 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
286 μs ± 14.4 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
NumPy is about 113x faster```

### ✏️ Task: Find the Repeated Work

```python
# This function is slow. Time it, find the repeated work, fix it, and time it again:
def above_average(values):
    return [v for v in values if v > sum(values) / len(values)]
```
def above_average(values):
    return [v for v in values if v > sum(values) / len(values)]
def above_average_fast(values):
    avg = sum(values) / len(values)
    return [v for v in values if v > avg]
values = list(range(100_000))
#t_slow = %timeit -o above_average(values)
t_fast = %timeit -o above_average_fast(values)

print(f"Speedup: {t_slow.average / t_fast.average:.1f}x")
### 🤖 Explain It

In your own words: why does `%timeit` run your code many times instead of just once like `%time`? And why should you "measure first" instead of rewriting code that just *looks* slow?

---
%timeit runs the code many times and reports an average execution time, which makes the result more reliable. A single run measured by %time can be affected by random factors such as other processes running on the computer or temporary system activity. %timeit reduces this noise by repeating the test many times and averaging the results.

You should "measure first" because code that looks slow is not always the actual bottleneck. Profiling and timing tools can identify where the program is really spending its time. Otherwise, you may spend time optimizing parts of the code that have little impact on overall performance.
## 🧾 Submit Checklist

- [X] I used at least 3 different magic commands, including one cell magic and one `!` shell command.
- [X] I fixed a notebook that only worked when run out of order, and I can explain why it failed.
- [X] I ran **Restart & Run All** on my notebooks before submitting.
- [X] I used `?`, `help()`, or `dir()` to look something up instead of guessing.
- [X] I wrote a Markdown cell with a heading, a list, a table, and LaTeX math.
- [X] I wrote and read back a text file, a JSON file, and a CSV file using `pathlib` paths.
- [X] I loaded data with Pandas and converted it between at least two formats.
- [X] I built at least one plot with a title, axis labels, and (if applicable) a legend, and saved it to a file.
- [X] I timed two approaches fairly with `%timeit`.
- [X] I uploaded each notebook's `NN-OutputFiles` folder along with the notebook.
- [X] I completed the "Explain It" prompts in my own words.
