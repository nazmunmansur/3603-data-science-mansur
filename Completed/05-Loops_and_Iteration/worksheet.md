# 📝 Worksheet: 05 - Loops and Iteration

Use this worksheet to reinforce your understanding of `for` loops, `while` loops, and reading files. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🔁 Section 1: For Loops

1. What does `range(5)` produce?  
   `Answer:` _____[0, 1, 2, 3, 4]_______________

2. Write a `for` loop that prints numbers 1 to 10, but skips 5.

```python
# Your code:
```for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```
prits out: 
1
2
3
4
6
7
8
9
10

3. What's the difference between using `range(len(my_list))` and just using `enumerate(my_list)` when you need the index?  
   `Answer:` range(len(my_list)) gives the indices and requires manual indexing to get values, while enumerate(my_list) gives both the index and the value directly, making the code cleaner and easier to read.

---

### ✏️ Task: Numbered Report with enumerate()

```python
# Given: tasks = ["Write report", "Review code", "Attend meeting"]
# Print each task numbered starting at 1, like:
# "1. Write report"
```
```
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
    ```
prints out:
1. Write report
2. Review code
3. Attend meeting
### ✏️ Task: Two Lists with zip()

```python
# Given: cities = ["Austin", "Dallas", "Houston"]
#        populations = [978000, 1300000, 2300000]
# Print a line per city like "Austin: 978,000" (use a format spec for the comma).
```
for city, population in zip(cities, populations):
    print(f"{city}: {population:,}")
result:
Austin: 978,000
Dallas: 1,300,000
Houston: 2,300,000
### 🤖 Explain It

In your own words: if you've written C++, compare Python's `for x in list:` to a C++ index-based `for` loop. What has to be managed by hand in C++ that Python handles for you?

---answer: In C++, I have to manage the counter, the stopping condition, and accessing each element by index. In Python, for x in list: iterates directly over the items, so Python handles the indexing and loop control automatically, making the code shorter and less error-prone.

## 🔁 Section 2: While Loops

4. What's the difference between a `for` loop and a `while` loop?  
   `Answer:` A for loop is used when you want to iterate over a sequence of items, while a while loop is used when you want to keep looping as long as a condition remains True.

5. What happens if a `while` loop's condition never becomes `False`?  
   `Answer:` ____Then it starts to do infinite looping. If a while loop's condition never becomes False, the loop will run forever. This is called an infinite loop.
---

### ✏️ Task: Countdown with While

```python
# Use a while loop to count down from 5 to 1.
```
while True:
    for i in range(5, 0, -1):
        print(i)
    break
Print out:
5
4
3
2
1
### ✏️ Task: Sentinel Loop

```python
# Use a while True loop with input() to collect names from the user
# until they type "stop". Print the final list of names collected.
```
names = []

while True:
    name = input("Enter a name (or 'stop' to finish): ")

    if name.lower() == "stop":
        break

    names.append(name)

print("Names collected:")
print(names)
#prints out:
Names collected:
['Ben']
### 🤖 Explain It

In your own words: why does a sentinel loop use `while True:` with a `break` inside, instead of putting the stop condition directly in the `while` line? Is there a situation where you *could* put it directly in the `while` line instead?

---
answer: The loop condition can't check name yet because name doesn't exist until after input() runs. Using while True lets the code to get the value first and decide afterward whether to continue. 
while True + break is common when the value needed for the decision is only available after some action (such as input() or reading a file).
Using while name != "stop": often requires getting the first value before the loop.
The walrus operator (:=) can satisfy both get the value and test it in the loop condition.
## 📁 Section 3: File Reading and `with`

6. What does the `with` statement do when opening a file?  
   `Answer:` The with statement automatically manages the file for you. It opens the file at the start of the block and guarantees that the file is closed when you leave the block, even if an error occurs.

7. How do you loop over each line in a file?  
   `Answer:` We can loop over each line in a file by iterating over the file object directly by the following method using line.strip() and loopoing it over the file as:
   with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
It is memory-efficient because Python reads the file one line at a time instead of loading the entire file into memory at once.
8. What error do you get if you try to open a file that doesn't exist, and how would you handle it without crashing the program?  
   `Answer:` Python raises a FileNotFoundError. To avoid this we can use try/except method aa below:
   try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found.")

 to keep the program running and not crashing the code.

---

### ✏️ Task: File Filter

```python
# Using the sample.txt file from the notebook (or create your own),
# write code that prints only the lines containing the word "error".
```
with open('sample.txt', 'r') as file:
    for line in file:
        if "error" in line:
            print(line.strip())

### ✏️ Task: Word Count

```python
# Loop over sample.txt and print the total number of words across
# the entire file (hint: len(line.split()) per line, added up).
```
line_count = 0
word_count = 0

with open("sample.txt", "r") as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())

print("Total lines:", line_count)
print("Total words:", word_count)
`prints out:` 
Total lines: 7
Total words: 27
### 🤖 Explain It

In your own words: what specifically goes wrong if you open a file *without* using `with` (or without manually calling `.close()`) and your code crashes partway through reading it?

---
answer: with open(...) is considered best practice: it guarantees the file is closed even if an exception, return, or other unexpected exit happens inside the block.

## 🚀 Section 4: Going Further (Optional)

This pairs with the "🔥 Challenge" section in the While Loops notebook — skip if you haven't gotten there yet.

### ✏️ Task: Walrus Operator

```python
# Rewrite this using the walrus operator (:=) so it's a single while line
# instead of a while True + break:
# while True:
#     n = int(input("Enter a number (0 to stop): "))
#     if n == 0:
#         break
#     print(n * n)
```
while (n := int(input("Enter a number (0 to stop): "))) != 0:
    print(n * n)
`prits out:` 100
---

## 🧾 Submit Checklist

- [X ] I wrote a `for` loop using `range()`.
- [X] I used `enumerate()` at least once.
- [X] I used `zip()` to loop over two sequences together.
- [X] I wrote a `while` loop, including at least one with `break` or `continue`.
- [X] I read a file with `with open(...)` and looped over its lines.
- [X] I completed the "Explain It" prompts in my own words.
