# 📝 Worksheet: 03b - Containers → Functions

Do this worksheet **on paper, without a computer**. The point is to practice being the computer. Each section ends with an **🤖 Explain It** prompt: write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧠 Section 1: Trace a Loop

Fill in the table for this code:

```python
temps = [31, 45, 28, 52]
total = 0
count = 0
for t in temps:
    total += t
    if t <= 32:
        count += 1
```

| pass | `t` | `total` | `count` |
|------|-----|---------|---------|
| start | — | 0 | 0 |
| 1 | 31| 31| 1|
| 2 | 45| 76| 1|
| 3 | 28| 104| 2|
| 4 | 52| 156| 2|

Which **two** patterns are mixed together in this loop?  
`Answer:` Accumulate and Filter

> 🤖 **Explain It:** Explain the difference between Accumulate, Count, and Filter as if you were talking to someone who has never programmed.

---
```Accumulate: Goes through the items and adds their values together to get a final result, such as a total or sum.
Count: Goes through the items and adds 1 each time something meets a condition, to find how many there are.
Filter: Goes through the items, checks a condition, and keeps only the items that meet the condition.```

## 🧠 Section 2: Pick Your Weapon

| Scenario | Container | Why? |
|----------|-----------|------|
| Daily step counts for a month | list|  list keeps the step counts in order |
| A playing card (rank, suit) | tuple|tuples are immutable |
| Username → password hash |dictionary |stores key → value pairs |
| Every distinct IP address in a log file | Set |set keeps only unique IP addresses |
| Your class schedule, in order |list |contains an ordered collection of items |

> 🤖 **Explain It:** Pick the scenario you were *least* sure about and argue for a different container than the one you chose.

---

## 🧠 Section 3: Take It Apart

```python
course = {
    "title": "CMPS 3603",
    "students": [
        {"name": "Ana", "scores": [88, 92]},
        {"name": "Ben", "scores": [75, 81]}
    ]
}
```

Write the value after **each** step:

1. `course["students"]` → [{"name": "Ana", "scores": [88, 92]}, {"name": "Ben", "scores": [75, 81]}]
2. `course["students"][1]` → {'name': 'Ben', 'scores': [75, 81]}
3. `course["students"][1]["scores"]` →[75, 81]
4. `course["students"][1]["scores"][0]` → 75

Write the expression that gets Ana's second score:  
`Answer:` `course["students"][0]["scores"][1]`

---

## 🧠 Section 4: Functions

1. What prints?

```python
def f(x):
    return x + 1

print(f(f(f(0))))
```

   `Answer:` 3

2. What prints? Explain why.

```python
def shout(word):
    print(word.upper())

x = shout("hi")
print(x)
```

   `Answer:`
HI
None #as the function converts words to upper case word so when the word is lower case it shows none. 

3. Circle the **parameters** and underline the **arguments**:

```python
def greet(name, greeting):
    return greeting + ", " + name

greet("Ada", "Hello")
```
parameters: (name, greeting) and arguments are "Ada", "Hello"

> 🤖 **Explain It:** In your own words, explain `print()` vs. `return`. Then explain why getting it wrong breaks a pipeline.

---print() displays a value on the screen, but return sends a value back to the program so it can be used later. Getting this wrong breaks a pipeline because the next function needs the returned value as its input. If we use print() instead of return, the next function may receive None instead of the data it needs.

## 🧠 Section 5: Contracts and Tests

Write a contract for a function `longest_word(words)`:

```text
IN: a list of words
OUT: the longest word (a string)
DOES: finds and returns the word with the greatest length
```


Write one test of each kind:

- Normal: check(longest_word(["cat", "elephant", "dorm"]), "elephant")
- Boundary: check(longest_word(["cat"]), "cat")
- Weird: check(longest_word([]), None)

---

## 🧠 Section 6: Draw the Pipeline

> "Given a list of prices, drop any that are `0` or less, add 8.25% tax to each, then find the total."

1. Name each function you'd need.
2. For each one, write what goes **in** and what comes **out** (shape, not just "data").
3. Draw the pipeline with arrows, labeling each arrow with the data's shape.

> 🤖 **Explain It:** Why is a pipeline of small functions easier to fix than one big block of code?
Functions needed
• remove_nonpositive() — removes prices that are 0 or less.
IN: list of numbers
Out: new list of numbers
Does: keeps only prices greater than 0
• add_tax() — adds 8.25% tax to each remaining price.
IN: list of numbers
Out: new list of numbers
Does: adds 8.25% tax to each price
• total() — adds all the prices together.
IN: list of numbers
Out: one number
Does: adds all prices together
```
Pipeline:
prices
(list of numbers)
      │
      ▼
remove_nonpositive()
      │
      ▼
(list of numbers)
      │
      ▼
add_tax()
      │
      ▼
(list of numbers)
      │
      ▼
total()
      │
      ▼
(one number)
```