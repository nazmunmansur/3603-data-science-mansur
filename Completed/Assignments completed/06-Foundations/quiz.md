# 📝 Quiz: 06 - Foundations

22 questions covering magic commands, Markdown, files/data I/O, plotting, and Jupyter productivity, plus a couple of "going further" bonus questions. Mix of multiple choice, true/false, code-tracing, and short answer.

This is a conceptual self-check. For hands-on practice writing and running real code, see `Foundations_Quiz.ipynb` in this folder.

Try every question on your own first — the Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Magic Commands and Performance

**1.** (Multiple Choice) Which magic command shows your current working directory?
A) `%pwd`  B) `%cd`  C) `%ls`  D) `%dir`
` A) %pwd`
**2.** (Short Answer) What's the difference between `%time` and `%timeit`?
`Answer:` %timeit is used when you want to compare solutions and measure performance accurately. Use %time when you just want to know roughly how long a piece of code takes to run once.
**3.** (Short Answer) What does `%%writefile` do differently from running a normal code cell?
`Answer:`The %%writefile command is a Jupyter Notebook magic command that saves the contents of a cell directly to a file on your local hard drive or server rather than executing it as live Python code.
**4.** (Short Answer) Why is `%timeit` generally more trustworthy than a single `%time` measurement?
`Answer:` %timeit is generally more trustworthy because it performs repeated measurements and averages them, reducing the effect of random noise and producing a more accurate estimate of real performance.
**5.** (True/False) `%who` only shows variable *names*, while `%whos` also shows their types and a value summary.
True
**6.** (Short Answer) Why is a NumPy vectorized operation like `arr ** 2` usually faster than a Python `for` loop doing the same calculation element by element?

---
A Python loop is like manually processing each item in a stack one by one. while the NumPy vectorized operation is like putting the whole stack on an automated machine that processes everything in a single optimized pass.
## Section B — Markdown

**7.** (Short Answer) What's the Markdown syntax for a level-2 heading (like `## Section 2`)?
A level-2 heading uses ## followed by a space and the heading text, for example (`## Section 2`) is showing smaller size than `# Section 2`. Again increasing nnumber of # will smaller the size of the headings. 
**8.** (Short Answer) How do you write **inline** LaTeX math in a Markdown cell, versus a **block** equation on its own line(s)?
For "inline" Latex Math use $ the equation $ shows the equation within the line. **block**: $$ equation $$ will show the equation only. 
**9.** (Short Answer) Why might you add narrative Markdown cells between code cells instead of just writing code comments?

Narrative Markdown cells are useful because they can provide more detailed explanations and context than code comments, making a notebook easier to understand and follow

## Section C — Files, Paths, and Data I/O

**10.** (Short Answer) What's the difference between JSON and CSV as file formats — when would you reach for one over the other?
CSV (Comma-Separated Values) is a file format used to store tabular data. Each row represents a record, and each column contains information about a specific field. CSV files are commonly used for data analysis because they are simple and easy to work with.

JSON (JavaScript Object Notation) stores data as key-value pairs, similar to dictionaries in Python. It can handle more complex and nested data structures than CSV and is often used for APIs and data exchange between applications.
**11.** (Code Tracing) What does this print?
```python
with open('x.txt', 'w') as f:
    f.write('hi')

with open('x.txt', 'r') as f:
    print(f.read())
```
hi
**12.** (Short Answer) What does `pd.read_csv('file.csv')` return?
A DataFrame is a two-dimensional table with rows and columns, similar to an Excel worksheet.
**13.** (Multiple Choice) Which DataFrame method shows summary statistics (mean, standard deviation, min/max, etc.)?
A) `.head()`  B) `.info()`  C) `.describe()`  D) `.columns()`
C) `.describe()`
**14.** (Short Answer) Why is it good practice to use a relative path (like `'data/file.csv'`) instead of an absolute path (like `'C:\Users\yourname\...'`) in a notebook you'll share or submit?
A relative path (e.g., 'data/file.csv') refers to a file relative to the notebook's location, making the notebook portable and easier to share. An absolute path (e.g., 'C:\Users\yourname\data\file.csv') only works on a specific computer and directory structure, so others may not be able to run the notebook without changing the path. 
**15.** (Short Answer) What does `%ls *.csv` do differently from plain `%ls`?

---
%ls shows everything inside a directory whereas %ls *.csv shows only CSV files.
## Section D — Plotting and Productivity

**16.** (Short Answer) What does `%matplotlib inline` do?
%matplotlib inline tells Jupyter Notebook to display Matplotlib plots directly inside the notebook output cells instead of opening them in a separate window.
**17.** (Short Answer) Name the three basic plot types covered in this module.
Bar, scatter and line plot. 
**18.** (Multiple Choice) In Command mode, which keyboard shortcut inserts a new cell *below* the current one?
A) `A`  B) `B`  C) `D D`  D) `M`
B) `B` 
**19.** (Short Answer) What's the practical difference between Command mode and Edit mode in a Jupyter notebook?
Command mode is for notebook and cell operations (add, delete, move, change cell type). Edit mode is for typing and modifying the contents of a cell.
**20.** (Short Answer) `?` shows a docstring. What does `??` sometimes show that `?` doesn't — and why doesn't it always work?

? shows an object's docstring and basic information.

?? tries to show additional details, including the object's source code if Python can access it. However, ?? doesn't always work because some functions are implemented in compiled code (such as C extensions in Python or NumPy), so their Python source code isn't available for Jupyter to display.

## Section E — Going Further (Bonus)

**21.** (Short Answer) What does `pathlib`'s `Path` object give you that a plain string file path doesn't?
Path makes file handling easier, safer, and more portable across operating systems because it provides built-in methods for working with files and folders.
**22.** (Short Answer) What does `dir(obj)` show you that plain Tab-completion in a notebook might not make as obvious at a glance?

---dir(obj) gives you a full list of all attributes and methods of an object at once, making it easier to see everything that's available.

## ✅ Answer Key

1. **A** — `%pwd`.
2. `%time` runs an expression once and reports how long that single run took. `%timeit` runs it many times and reports an average (with variation), which is much less affected by whatever else your computer happens to be doing at that moment.
3. `%%writefile` saves the entire cell's contents to a file on disk instead of running it as Python code.
4. Because a single run can be thrown off by background noise (other processes, caching, etc.); averaging many runs smooths that out and gives a more reliable number.
5. **True**.
6. NumPy operations run as compiled, vectorized code under the hood instead of executing a Python-level loop instruction by instruction — the per-element overhead of the Python interpreter is avoided.
7. `## Section 2`
8. Inline: wrap it in single dollar signs, e.g. `$E = mc^2$`. Block: wrap it in double dollar signs on their own lines, e.g. `$$ ... $$`.
9. Narrative Markdown explains the *why* and tells a story around the results in a way that renders as readable formatted text — code comments are only visible when reading the raw code, not when someone (or you, later) is skimming a report-style notebook.
10. JSON stores structured, often nested, key-value data (good for configs, API responses, non-tabular structures). CSV stores flat, tabular, rows-and-columns data — better suited to spreadsheet-like datasets.
11. `hi`
12. A Pandas DataFrame.
13. **C** — `.describe()`.
14. An absolute path is specific to one person's computer and folder structure — it will break the moment anyone else (including you, on a different machine) tries to run the notebook. A relative path works whenever the notebook and its data stay in the same relative arrangement.
15. Plain `%ls` lists everything in the current directory; `%ls *.csv` filters that listing to only show files ending in `.csv`.
16. It tells Matplotlib to render plots directly inside the notebook output, instead of trying to open a separate window.
17. Line, scatter, and bar plots.
18. **B** — `B`.
19. In Edit mode, keystrokes type into the currently selected cell. In Command mode, keystrokes are shortcuts that act on the cell as a whole (or the notebook) — nothing gets typed into it.
20. `??` tries to show the actual Python **source code**, not just the docstring. It doesn't always work because some functions (many built-ins) are implemented in C, not Python, so there's no Python source available to display.
21. `Path` objects handle path separators correctly across operating systems (Windows uses `\`, Mac/Linux use `/`), support `/` for joining paths in code, and provide built-in checks like `.exists()` — a plain string just holds text and knows none of that.
22. `dir(obj)` lists *every* attribute and method at once, including "hidden" double-underscore (dunder) methods like `__init__` and `__len__` that Tab-completion in some editors may filter out of the suggestion list by default.
