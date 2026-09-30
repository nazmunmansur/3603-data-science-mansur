# 📝 Worksheet: 03 - Strings and Text

Use this worksheet to reinforce your understanding of strings — creating them, slicing them, cleaning them up, and formatting them. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧠 Section 1: String Basics

1. Why doesn't Python care whether you use `'...'` or `"..."`?  
   `Answer:` __Because both create exactly the same type of object: a string (str).

2. What's the output of this code?

```python
word = 'science'
print(word[0:3])
```

   `Answer:` _______sci________________

3. Rewrite this string so it could be written with single quotes on the outside instead of double:

```python
message = "She said \"don't stop\""
```

   `Answer:` ______message = """She said "don't stop" """_________________

---

### ✏️ Task: Slicing Practice

```python
# Given: course = "Programming for Data Science"
# Print just the word "Data" using slicing.
# Print the string reversed.
```
course = "Programming for Data Science"

# Print just the word "Data"
print(course[16:20])

# Print the string reversed
print(course[::-1])
result:
Data
ecneicS ataD rof gnimmargorP
### ✏️ Task: Multi-Line String

```python
# Write a triple-quoted string containing a 3-line "About Me" bio.
# Print it.
```
bio = """ My name is Nazmun. 
I am a data scientist. 
I love to work with data and solve problems using data. """
result:
 My name is Nazmun. 
I am a data scientist. 
I love to work with data and solve problems using data.

### 🤖 Explain It

In your own words: why are strings immutable, and what do you actually have to do if you want a "modified" version of a string?

---Strings are immutable. the modified version could be as below:
word = "hello"
new_word = "J" + word[1:]
print(new_word) and it will print Jello instead of hello.

## 🔁 Section 2: String Methods

4. What's the difference between `.strip()` and `.replace(' ', '')`?  
   `Answer:` ____.strip() emoes whitespace, .replace() removes very space charqacter.___________________

5. What will this print?

```python
name = "  ADA lovelace  "
print(name.strip().title())
```

   `Answer:` ____Ada Lovelace___________________

6. If `words = "red,green,blue".split(',')`, what is `words`, and what type is it?  
   `Answer:` _____['red', 'green', 'blue']
<class 'list'>__________________

---

### ✏️ Task: Clean and Validate

```python
# Given: raw_input = "  YES  "
# Clean it up (strip + lowercase) and check if it equals "yes".
# Print True or False.
```
raw_input = "  YES  "

print(raw_input.strip().lower() == "yes")
result: True
### ✏️ Task: Build a Sentence

```python
# Given: words = ['data', 'science', 'is', 'fun']
# Use .join() to turn this into the sentence "data science is fun".
# Then use .replace() to change "fun" to "powerful" in the result.
```
words = ['data', 'science', 'is', 'fun']

# Join the words into a sentence
sentence = " ".join(words)

# Replace "fun" with "powerful"
sentence = sentence.replace("fun", "powerful")

print(sentence)
it returns: data science is powerful
### 🤖 Explain It

In your own words: what's the difference between a method like `.upper()` that returns a new string, versus a list method like `.append()` that changes the list in place? Why do strings only work the first way?

---
Strings are immutable that's why it can use methods like .upper(), .lower(), and .replace() do not change the original string. Instead, they create and return a new string. however, list can be modified by using the .append(), .sort(), and .remove() that directly change the existing list.
## 🎯 Section 3: Formatted Strings

7. What does the format spec `:.2f` do?  
   `Answer:` ________format the number upto 2 deimal points._______________

8. What will this print?

```python
item = "eraser"
qty = 5
print(f"You bought {qty} {item}(s)")
```

   `Answer:` ____You bought 5 eraser(s)___________________

9. Why might you use an f-string instead of `+` to build a string out of variables?  
   `Answer:` ____f-string is often better than + because it's more readable, easier to write, and can include expressions directly.___________________

---

### ✏️ Task: Formatted Receipt

```python
# Given: item = "Backpack", price = 45.999, qty = 2
# Print a line like: "2x Backpack @ $46.00 = $92.00"
# (Notice price needs rounding — that's what :.2f is for.)
```
item = "Backpack"
price = 45.999
qty = 2

print(f"{qty}x {item} @ ${price:.2f} = ${price * qty:.2f}")
it prints: 2x Backpack @ $46.00 = $92.00
### ✏️ Task: Aligned Table

```python
# Given: names = ["Ana", "Bartholomew", "Cy"]
# Print each name right-aligned in a 15-character field, one per line,
# so they all line up on the right edge.
```
names = ["Ana", "Bartholomew", "Cy"]
for name in names:
    print(f"{name:>15}|")  # Right-align with a width of 15 characters

result:  
            Ana|
    Bartholomew|
             Cy|
### 🤖 Explain It

In your own words: what's the practical difference between `f'{price}'` and `f'{price:.2f}'` when `price = 19.999999`? When would the difference actually matter in real code?

---
the f'{price}' uses the default string representation of the float. However, f'{price:.2f}' rounds the number to 2 decimal places and always shows exactly two digits after the decimal point.
## 🚀 Section 4: Going Further (Optional)

These pair with the "🔥 Challenge" sections in the notebooks — skip if you haven't gotten there yet.

### ✏️ Task: Raw String

```python
# Write the Windows path C:\Users\you\Desktop\notes.txt as a raw string.
# Print it, and explain in a comment why the plain (non-raw) version would be risky.
```
path = r"C:\Users\Nazmun\projects\3603-data-science-mansur\Work\02"
path_1 = "C:\Users\Nazmun\projects\3603-data-science-mansur\Work\02"
print(path)
print(path_1) 
which shows the error: Cell In[29], line 2
    path_1 = "C:\Users\Nazmun\projects\3603-data-science-mansur\Work\02"
             ^
SyntaxError. withot r python cannot red the raw string. So Using a raw string is safer because backslashes are treated literally.
### ✏️ Task: Debug Format Spec

```python
# Given: width = 10, height = 4
# Use the f'{expr=}' debug spec to print both "width" and "width * height"
# with their values, without writing separate print() calls for each.
```
width = 10
height = 4

print(f"{width=}, {width * height=}")
---
it prints: width=10, width * height=40
## 🧾 Submit Checklist

- [X] I created strings with single quotes, double quotes, and triple quotes.
- [X] I indexed and sliced a string.
- [X] I used at least three different string methods (`.strip()`, `.split()`, `.join()`, `.replace()`, etc.).
- [X] I built an f-string with more than one embedded expression.
- [X] I used a format spec to control decimal places or alignment.
- [X] I completed the "Explain It" prompts in my own words.
