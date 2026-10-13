# 📝 Worksheet: 04 - More Functions & Loops

Do this worksheet **on paper, without a computer**. Each section ends with an **🤖 Explain It** prompt: write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧠 Section 1: Defaults and Keywords

```python
def price(amount, tax=0.0825, discount=0):
    return round(amount * (1 + tax) - discount, 2)
```

What does each call return?

1. `price(100)` → ________108.25____________________
2. `price(100, discount=10)` → __98.25__________________________
3. `price(100, 0)` → ___100_________________________
4. `price(discount=5, amount=20)` → ___16.65_________________________

> 🤖 **Explain It:** Why are keyword arguments easier to read than positional ones in a call like `price(100, 0, 10)`?

--- 
```Keyword arguments are easier to read because they label each value with its parameter name, making the call more self-explanatory. ```

## 🧠 Section 2: Scope

What prints? Explain why.

```python
count = 0

def add_one(count):
    count = count + 1
    return count

result = add_one(count)
print(count, result)
```

`Answer:` 0 1

> 🤖 **Explain It:** Describe the "room with two doors" model of a function in your own words.

---
```A function is like a room with an input door and an output door. Data goes into the function through its parameters, the function does some work inside the room, and the result comes out through the return statement.```

## 🧠 Section 3: Trace a While Loop

```python
balance = 100
years = 0
while balance < 150:
    balance = balance + 20
    years += 1
```

| pass | `balance` at the start | `balance < 150`? | `balance` after | `years` after |
|------|------------------------|------------------|-----------------|---------------|
| 1 | 100 | True| 120| 1|
| 2 | 120| True| 140| 2|
| 3 | 140| True| 160| 3|
| 4 | 160| False| Stop| none|

Final `years`: ___3_________  Final `balance`: ____160________

What single change would make this an **infinite** loop?  
`Answer:` while balance != 150:

---

## 🧠 Section 4: `for` or `while`?

| Task | `for` or `while`? | Why? |
|------|-------------------|------|
| Print each line of a file | for| iterating each line of a file|
| Keep asking for a password until it's correct | while| condition is correct password to stop the loop|
| Find the average of a list of prices | for | itersting over the list of prices no condiotion added |
| Double a number until it's over one million | while| there is a codition to stop the loop|

---

## 🧠 Section 5: Files

Given the file `pets.txt`:

```text
name,species
Rex,dog

# rescued in May
Tom,cat
```

1. How many times does `for line in f:` run? ______4______
2. Which lines should your code skip, and how would you detect each one?  
   `Answer:` ____Skip the header (name,species) and any line starting with #_______________________
3. Write the list of dictionaries a `read_pets` function should return:  
   `Answer:` __[
    {"name": "Rex", "species": "dog"},
    {"name": "Tom", "species": "cat"}
]
```_```_____________________

> 🤖 **Explain It:** When is `try` / `except` a good idea, and when does it just hide bugs?
try/except is a good idea when you expect an error that could reasonably happen, such as a user entering invalid input or a file not existing. It prevents the program from crashing and lets you handle the problem gracefully.  
