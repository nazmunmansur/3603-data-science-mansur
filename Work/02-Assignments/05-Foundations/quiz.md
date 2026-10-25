# 📝 Quiz: 05 - Foundations

45 questions covering all 8 Foundations notebooks, in order: magic commands, Jupyter workflow, getting help, Markdown, files and paths, data I/O, plotting with NumPy, and timing. Mix of multiple choice, true/false, code-tracing, and short answer.

This is a conceptual self-check. For hands-on practice writing and running real code, see `Foundations_Quiz.ipynb` in this folder.

Try every question on your own first. The Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Magic Commands (01)

**1.** (Multiple Choice) Which magic command shows your current working directory?
A) `%pwd`  B) `%cd`  C) `%ls`  D) `%dir`
``` A) `%pwd```
**2.** (Short Answer) What's the difference between a line magic (`%pwd`), a cell magic (`%%writefile`), and a shell command (`!ls`)?
```%pwd is a line magic that affects one line, %%writefile is a cell magic that processes an entire cell, and !ls is a shell command that runs a command in the operating system.```
**3.** (Code Tracing) A folder contains only `a.csv` and `b.txt`. What kind of value is stored in `files`, and what does it contain?
```python
files = !ls
```
``` ['a.csv', 'b.txt']```
**4.** (True/False) `%cd ..  # go up one folder` moves you to the parent folder.
``` True```
**5.** (Short Answer) Inside a notebook, why should you install packages with `%pip install` instead of `!pip install`?
```Use %pip install because it installs packages into the notebook's current Python kernel environment. !pip install runs as a shell command and may install the package in a different environment, causing import problems. ```
**6.** (True/False) `%who` only shows variable *names*, while `%whos` also shows their types and a value summary.

---```True```

## Section B — Jupyter Workflow (02)

**7.** (Multiple Choice) In Command mode, which keyboard shortcut inserts a new cell *below* the current one?
A) `A`  B) `B`  C) `D D`  D) `M`
``` B) 'B' ```

**8.** (Short Answer) What's the practical difference between Command mode and Edit mode? You press `B` and the letter "b" appears in your code. What happened, and what should you press?
```Command mode is used for notebook actions and keyboard shortcuts (such as adding, deleting, or moving cells). Edit mode is used for typing and editing code or Markdown inside a cell. If you press B and the letter "b" appears in your code, you're in Edit mode. Press Esc to switch to Command mode, then press B to insert a new cell below.```
**9.** (Code Tracing) What does this cell display when it runs?
```python
x = 5
x * 2
x * 3
```
``` 15```
**10.** (Short Answer) A cell near the bottom of a notebook shows `[7]`, and the cell above it shows `[9]`. What does that tell you?
``` The cells were executed out of order. The numbers in brackets show execution order, not the cells' positions in the notebook.```
**11.** (True/False) If you delete the cell that created the variable `message`, `message` is removed from memory immediately.
``` False```
**12.** (Short Answer) Why should you **Restart & Run All** before submitting a notebook?
``` Restart & Run All clears everything from memory and then runs every cell from top to bottom. This helps verify that the notebook works correctly from a fresh start and doesn't rely on variables or outputs left over from earlier runs.``` 
---

## Section C — Getting Help (03)

**13.** (Short Answer) `?` shows a docstring. What does `??` sometimes show that `?` doesn't, and why doesn't it always work?
```? shows a function's docstring and basic information. ?? can also show the function's source code (when available). It doesn't always work because some functions are written in compiled languages (such as C) or their source code isn't available to IPython.```
**14.** (Multiple Choice) The signature is `sorted(iterable, /, *, key=None, reverse=False)`. Which call is valid?
A) `sorted(iterable=nums)`  B) `sorted(nums, None, True)`  C) `sorted(nums, reverse=True)`  D) `sorted()`
``` C) `sorted(nums, reverse=True)```
**15.** (Code Tracing) What error does this raise, and what does it mean?
```python
numbers = [1, 2, 3]
numbers.mean()
```
```This means that Python lists do not have a method called mean(). You are trying to use an attribute or method that doesn't exist for a list object. ```
**16.** (Short Answer) A long traceback fills the screen. Which line should you read first, and why?
```When a traceback appears, read the last line first. It usually shows the actual error type and message (for example, NameError, TypeError, or FileNotFoundError) and tells you what went wrong. Then look a few lines above it to find the line of your code where the error occurred.```
**17.** (Short Answer) What does `dir(obj)` give you that Tab completion doesn't?

---```dir(obj) shows the complete list of an object's attributes and methods. Tab completion helps you discover and complete names interactively, but it may not show everything as clearly or all at once.```

## Section D — Markdown (04)

**18.** (Short Answer) What's the Markdown syntax for a level-2 heading (like `## Section 2`)?
```A level-2 heading in Markdown uses two hash symbols (##) followed by a space and the heading text.```
**19.** (Short Answer) How do you write **inline** LaTeX math in a Markdown cell, versus a **block** equation on its own line(s)?
```Use $ ... $ for inline math and $$ ... $$ for a block equation on its own line.``` 
**20.** (Short Answer) The Markdown text `The item costs $5 and the tax is $2.` renders strangely. Why, and how do you fix it?
```It renders strangely because $ is used to mark LaTeX math. To show a literal dollar sign, escape it with \$, for example: The item costs \$5 and the tax is \$2.```
**21.** (Short Answer) You typed two lines directly under each other in a Markdown cell, but they render as **one** line. Name two ways to fix it.
```Add two trailing spaces at the end of the first line, or use <br> between the lines.```
**22.** (Short Answer) Why might you add narrative Markdown cells between code cells instead of just writing code comments?
---```Narrative Markdown cells explain the purpose, results, and reasoning behind the code. They make the notebook easier to understand and follow than code comments alone, especially for someone reading the notebook later.```

## Section E — Files and Paths (05)

**23.** (Code Tracing) What does this print?
```python
with open('x.txt', 'w', encoding='utf-8') as f:
    f.write('hi')

with open('x.txt', 'r', encoding='utf-8') as f:
    print(f.read())
```
``` hi```
**24.** (Multiple Choice) Which file mode adds to the end of an existing file **without** erasing it?
A) `'r'`  B) `'w'`  C) `'a'`  D) `'x'`
```C) `'a'```
**25.** (Code Tracing) What does this print?
```python
from pathlib import Path
p = Path('data') / 'sales_2026.csv'
print(p.name, p.stem, p.suffix)
```
```sales_2026.csv sales_2026 .csv```
**26.** (Short Answer) Why is it good practice to use a relative path (like `'data/file.csv'`) instead of an absolute path (like `'C:/Users/yourname/...'`) in a notebook you'll share or submit?
```Relative paths are better for shared or submitted notebooks because they work as long as the files are in the same project folder structure. Absolute paths often contain user-specific folders (such as C:/Users/...) that won't exist on another person's computer, causing the notebook to fail to find the files.``` 
**27.** (Code Tracing) `scores.csv` contains the two lines `Name,Score` and `Alice,90`. What does this print, and why might that cause a problem?
```python
import csv
with open('scores.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))
print(rows[1])
```
```It prints ['Alice', '90']. This can be a problem because if the file has no data rows, rows[1] won't exist and will raise an IndexError.```
**28.** (True/False) After saving `{'point': (3, 4)}` with `json.dump` and reading it back with `json.load`, you get back exactly the same dictionary.

---```False```

## Section F — Data Input and Output (06)

**29.** (Short Answer) What does `pd.read_csv('file.csv')` return?
```Returns a Pandas DataFrame containing its data.``` 
**30.** (Multiple Choice) Which DataFrame method shows summary statistics (mean, standard deviation, min/max, etc.)?
A) `.head()`  B) `.info()`  C) `.describe()`  D) `.columns()`
``` C) `.describe()```
**31.** (Short Answer) You save a DataFrame with `df.to_csv('out.csv')`, read it back, and find an extra `Unnamed: 0` column. What caused it, and how do you prevent it?
```The extra Unnamed: 0 column is the DataFrame index that was saved to the CSV. Prevent it by using index=False when calling to_csv().```
**32.** (Short Answer) What does JSON written with `orient='records'` look like, and why is it usually the layout you want?
```orient='records' creates a list of dictionaries, with one dictionary per row. It's usually preferred because it's easy to read, share, and use with APIs and other applications.```
**33.** (Short Answer) After `pd.read_csv`, the ZIP code `02108` shows up as `2108`. Why, and how do you fix it?
```The leading zero is lost because Pandas interprets the ZIP code as a number. Read the column as a string (dtype={'Zip': str}) to preserve leading zeros such as 02108.```
**34.** (Short Answer) What does `pd.read_excel('file.xlsx', sheet_name=None)` return?

---```pd.read_excel('file.xlsx', sheet_name=None) returns a dictionary of DataFrames, where the keys are the sheet names and the values are the DataFrames containing the data from each sheet.```

## Section G — Plotting with NumPy and Matplotlib (07)

**35.** (Code Tracing) What do these two lines print?
```python
print([1, 2] * 2)
print(np.array([1, 2]) * 2)
```
```
[1, 2, 1, 2]
[2 4]```
**36.** (Matching) Choose the best chart (line, bar, scatter, or histogram) for each question:
a) Which department sold the most? ```bar chart```
b) How did daily website visits change over a month?```line```
c) Is there a relationship between price and units sold?```scatter```
d) What is the distribution of customer order values?``` histogram```

**37.** (Short Answer) A histogram and a bar chart both draw rectangles. What's the difference in what they show?
```A histogram shows the distribution of a numeric variable by grouping values into intervals (bins), while a bar chart compares values for different categories. Histograms use continuous numeric data; bar charts use categorical data.``` 
**38.** (Short Answer) You call `plt.show()` and then `plt.savefig('chart.png')`, and the saved image is blank. Why?
```The usual reason is that plt.show() displays and may clear/close the current figure. If you call plt.savefig() after plt.show(), there may be no active plot left to save, resulting in a blank image.``` 
**39.** (Short Answer) On a box plot, what does the line **inside** the box represent, and what do the dots **beyond** the whiskers represent?

---```The line inside the box is the median, and the dots beyond the whiskers are outliers.```

## Section H — Timing and Performance (08)

**40.** (Short Answer) What's the difference between `%time` and `%timeit`, and why is `%timeit` more trustworthy for comparisons?
```%time measures one execution, while %timeit measures many executions and reports an average. %timeit is more trustworthy because it reduces the impact of random timing variations.```
**41.** (Short Answer) Why is a NumPy vectorized operation like `arr ** 2` usually much faster than a Python `for` loop doing the same calculation element by element?
``` A NumPy operation like arr ** 2 works on the whole array at once using fast, optimized code, while a Python for loop processes one element at a time and has more overhead. Therefore, vectorized operations are usually much faster.```
**42.** (True/False) A variable created inside a `%%timeit` cell is available in the cells after it.
```False```
**43.** (Short Answer) What's unfair about comparing `%timeit np.array(my_list) ** 2` against `%timeit arr ** 2` to decide whether squaring is fast?
```It's unfair because np.array(my_list) ** 2 includes two tasks: converting the list to a NumPy array and squaring the values, while arr ** 2 only measures the squaring operation on an array that already exists.```
**44.** (Short Answer) Why is `[s / max(scores) for s in scores]` slow for large lists? How would you fix it, and roughly what happens to its runtime when the list doubles in size?
```because max(scores) is recalculated during every iteration of the list comprehension. For a large list, that means scanning the entire list over and over again. Fix it by calculating the maximum once.```
**45.** (Multiple Choice) What does `%prun` show you?
A) Only the total time of the cell  B) How much time was spent in each function called  C) How much memory each variable uses  D) The source code of a function
```B) How much time was spent in each function called```
