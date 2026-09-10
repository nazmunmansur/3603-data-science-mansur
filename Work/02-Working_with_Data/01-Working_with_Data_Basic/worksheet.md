# 📝 Worksheet: 01 - Working with Data

Use this worksheet to review and reinforce your understanding of Python's core data containers. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧠 Section 1: Lists

1. What method adds an item to the end of a list?  
   `Answer:` ________.append()____________________

2. How can you remove an item from a list by value? By position?  
   `Answer:` ____removing an item by vslue using .remove() and remving by position  usnig _____.pop()___________________

3. What's the result of this code?

```python
nums = [2, 4, 6]
nums.append(8)
print(nums)
```

   `Answer:` ___[2, 4, 6, 8]________________________

4. What does `my_list[1:4]` return, given `my_list = [10, 20, 30, 40, 50]`?  
   `Answer:` _______[20, 30, 40]_____________________

---

### ✏️ Task: List Practice

```python
# Create a list of your top 3 favorite foods.
# Add another food to the list.
# Remove one item and print the list.
```

### ✏️ Task: Slicing and Sorting

```python
# Given: numbers = [42, 17, 8, 99, 23, 4]
# 1. Print the first three numbers using slicing.
# 2. Print the numbers sorted from smallest to largest.
# 3. Print the numbers sorted from largest to smallest.
```Python
# Create a list of top 3 favorite foods
foods = ["Pizza", "Macroons", "Biryani"]

# Add another food to the list
foods.append("Pasta")

# Remove one item from the list
foods.remove("Pizza")

# Print the final list
print(foods)
```
### ✏️ Task: Filtering

```python
# Given: temps = [55, 72, 90, 43, 88, 67, 101]
# Build a new list called "hot" containing only temps over 85.
# Print "hot".
temps = [55, 72, 90, 43, 88, 67, 101]
hot = []

for temp in temps:
    if temp > 85:
        hot.append(temp)
print(hot)
```
answer: [90, 88, 101]

### 🤖 Explain It

In your own words: what's the difference between a list and a slice of a list? Is slicing a list the same as modifying it?
A list contains all the items.
A slice creates a new list containing only the selected items from the original list. 
No slicing a list is not same as modifying it. Slicing creates a new list containing the chosen elements.
---

## 🔒 Section 2: Tuples

5. What is a key difference between a list and a tuple?  
   `Answer:` _The key difference is that lists are mutable and tuples are immutable.__________________

6. Can you change the contents of a tuple once it is created? Why or why not?  
   `Answer:` ____Tuples are immutable, meaning that once it's created  you cannot change or modify the tuples________________________

7. What does `first, *rest = (10, 20, 30, 40)` assign to `first` and `rest`?  
   `Answer:` first gets the first value: 10
*rest collects all remaining values into a list: [20, 30, 40]. Python uses unpacking for that.

---

### ✏️ Task: Tuple Practice

```python
# Create a tuple with your favorite 3 numbers.
# Unpack it into three variables and print each.
# Create a tuple with 3 favorite numbers
favorite_numbers = (7, 14, 21)
# Unpack the tuple into three variables
first, second, third = favorite_numbers
# Print each variable
print(first)
print(second)
print(third)
```
result: 7
       14
       21
### ✏️ Task: Unpacking with *rest

```python
# Given: race_times = (9.58, 9.63, 9.69, 9.71, 9.74)
# Unpack this into "winner" (the first time) and "others" (everything else).
# Print both.
race_times = (9.58, 9.63, 9.69, 9.71, 9.74)
Winner = race_times[0]
print("Winner:", Winner)
others = race_times[1:5]
print("Others:", others) 
```
result:
Winner: 9.58
Others: (9.63, 9.69, 9.71, 9.74)
### ✏️ Task: Tuples as Dictionary Keys

```python
# Build a dictionary called "distances" where the keys are (city1, city2)
# tuples and the values are the distance in miles between them.
# Add at least two entries, then look up and print one of them.
# Create a dictionary with tuple keys
distances = {
    ("Dallas", "Austin"): 195,
    ("Wichita Falls", "Dallas"): 142
}
# Look up and print one distance
print(distances[("Wichita Falls", "Dallas")])
```
reult: 142
### 🤖 Explain It

In your own words: why does Python allow a tuple to be a dictionary key, but not a list? What property makes that possible?

---Tuples are immutable and that property made a perfect choice to be a dictionary key. Lists are mutable meaning you can change or modify it. 

## 🔑 Section 3: Dictionaries

8. What does the `.get()` method do differently from accessing a key directly with `[]`?  
   `Answer:` dict[key] raises a KeyError when the key is missing, while dict.get(key) returns None (or a default value you specify) instead of raising an error.
9. How do you loop through both keys and values in a dictionary?  
   `Answer:` __Use a for loop with .items() method__________________________

10. How would you remove a key from a dictionary and also capture the value it held?  
    `Answer:` dict.pop(key) to remove a key and capture the value it held.
---

### ✏️ Task: Dictionary Practice

```python
# Create a dictionary with keys: 'name', 'age', and 'hobby'.
# Print each key and value in the format "key: value".

Person = {"name": "John", "age": 30, "hobby": "Reading"}
# Print each key and value
Person = {"name": "John", "age": 30, "hobby": "Reading"}
# Print each key and value
for key, value in Person.items():
    print(f"{key}: {value}")
```
result:
name: John
age: 30
hobby: Reading

### ✏️ Task: Build from Two Lists

```python
# Given: products = ['pen', 'notebook', 'eraser']
#        prices = [1.50, 3.25, 0.75]
# Build a dictionary mapping each product to its price.
# Print the total cost of all products (hint: sum the .values()).

products = ['pen', 'notebook', 'eraser']
prices = [1.50, 3.25, 0.75]

# Build a dictionary mapping products to prices
product_prices = dict(zip(products, prices))

# Print the dictionary
print(product_prices)

# Print the total cost of all products
total_cost = sum(product_prices.values())
print(f"Total cost: ${total_cost:.2f}")
```
result:
{'pen': 1.5, 'notebook': 3.25, 'eraser': 0.75}
Total cost: $5.50
### ✏️ Task: Nested Dictionaries

```python
# Given:
# inventory = {
#     'apples': {'count': 50, 'price': 0.50},
#     'bananas': {'count': 30, 'price': 0.25},
# }
# Loop through inventory and print a line for each fruit like:
# "apples: 50 units at $0.50"
inventory = {
    'apples': {'count': 50, 'price': 0.50},
    'bananas': {'count': 30, 'price': 0.25},
}

# Loop through inventory and print each fruit's information
for fruit, details in inventory.items():
    print(f"{fruit}: {details['count']} units at ${details['price']:.2f}")
```
results:
apples: 50 units at $0.50
bananas: 30 units at $0.25
### 🤖 Explain It

In your own words: what's the difference between `student['gpa']` and `student.get('gpa')` when `'gpa'` isn't in the dictionary? Which would you use, and when?
student[gpa] is looking for the key "gpa" and prints it value. It raises a KeyError if 'gpa' is missing. however, student.get('gpa') shows the gpa vlaue and if the key is missing thaen it gives a default value or "None".  
---

## 🚀 Section 4: Going Further (Optional)

These pair with the "🔥 Challenge" sections in the notebooks — skip if you haven't gotten there yet.

### ✏️ Task: List Comprehension

```python
# Rewrite this loop as a one-line list comprehension:
# cubes = []
# for n in range(6):
#     cubes.append(n ** 3)
```
cubes = [n ** 3 for n in range(6)]
results: [0, 1, 8, 27, 64, 125]

### ✏️ Task: namedtuple

```python
# Create a namedtuple called "Book" with fields "title" and "author".
# Make one instance and print both fields by name.
```
from collections import namedtuple
# Create a namedtuple called Book
Book = namedtuple("Book", ["title", "author"])
# Create an instance
my_book = Book("The Hobbit", "J.R.R. Tolkien")
# Print fields by name
print(my_book.title)
print(my_book.author)
The Hobbit
J.R.R. Tolkien
### ✏️ Task: Word Counter

```python
# text = "to be or not to be that is the question"
# Build a dictionary counting how many times each word appears.
# (Try it by hand first, then check yourself with collections.Counter.)
```

---

## 🧾 Submit Checklist

- [X ] I practiced creating, slicing, sorting, and filtering lists.
- [X ] I understand how tuples are different from lists, and why that makes them hashable.
- [X] I accessed, looped through, updated, and removed items from a dictionary.
- [X ] I built a dictionary from two separate lists.
- [X ] I worked with at least one nested dictionary.
- [X ] I completed the "Explain It" prompts in my own words.
