# 📝 Worksheet: 01 - Working with Data

Use this worksheet to review and reinforce your understanding of Python's core data containers. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧠 Section 1: Lists

1. What method adds an item to the end of a list?  
   `Answer:` .append()

2. How can you remove an item from a list by value? By position?  
   `Answer:` removing an item by vslue using the  .remove() method and remving by position usnig the .pop() method.

3. What's the result of this code?

```python
nums = [2, 4, 6]
nums.append(8)
print(nums)
```

   `Answer:` [2, 4, 6, 8]

4. What does `my_list[1:4]` return, given `my_list = [10, 20, 30, 40, 50]`?  
   `Answer:` [20, 30, 40]

4a. Given `a = [1, 2]` and `b = [3, 4]`, what is the result of `a + b`? Of `a.append(b)`? Of `a.extend(b)`?  
   `Answer:` 
- a + b → [1, 2, 3, 4]
- a.append(b) → [1, 2, [3, 4]]
- a.extend(b) → [1, 2, 3, 4] (and modifies a in place)

4b. Given `grid = [[1, 2], [3, 4]]`, how do you access the value `3`?  
   `Answer:` grid[1][0]

4c. List three different ways to remove an item from a list.  
   `Answer:` remove(), pop(), and del.

---

### ✏️ Task: List Practice

```python
# Create a list of your top 3 favorite foods.
# Add another food to the list.
# Remove one item and print the list.
```
foods = ["Biryani", "Pizza", "Sushi"]

# Add another food
foods.append("Pizza")

# Remove one item
foods.remove("Sushi")

# Print the list
print(foods)

# prints out: ['Biryani', 'Pizza', 'Pizza']
### ✏️ Task: Slicing and Sorting

```python
# Given: numbers = [42, 17, 8, 99, 23, 4]
# 1. Print the first three numbers using slicing.
# 2. Print the numbers sorted from smallest to largest.
# 3. Print the numbers sorted from largest to smallest.
```
numbers = [42, 17, 8, 99, 23, 4]

# 1. Print the first three numbers using slicing.
print(numbers[:3])

# 2. Print the numbers sorted from smallest to largest.
print(sorted(numbers))

# 3. Print the numbers sorted from largest to smallest.
print(sorted(numbers, reverse=True))
# Prints out:
[42, 17, 8]
[4, 8, 17, 23, 42, 99]
[99, 42, 23, 17, 8, 4]
### ✏️ Task: Filtering

```python
# Given: temps = [55, 72, 90, 43, 88, 67, 101]
# Build a new list called "hot" containing only temps over 85.
# Print "hot".
```
temps = [55, 72, 90, 43, 88, 67, 101]
hot = []

for temp in temps:
    if temp > 85:
        hot.append(temp)
print(hot)
```
# answer: [90, 88, 101]
### ✏️ Task: Combine Lists Three Ways

```python
# Given: morning = ['eggs', 'toast']
#        extras  = ['jam', 'coffee']
# 1. Use + to make a new list "breakfast" without changing "morning".
# 2. On a fresh copy of "morning", use .append(extras) and print the result.
#    Notice how many items the list has now, and why.
# 3. On another fresh copy, use .extend(extras) and print the result.
```
morning = ['eggs', 'toast']
extras = ['jam', 'coffee']

# 1. Use + to make a new list "breakfast" without changing "morning".
breakfast = morning + extras
print("breakfast:", breakfast)
print("morning:", morning)

# 2. On a fresh copy of "morning", use .append(extras)
copy1 = morning.copy()
copy1.append(extras)
print("append result:", copy1)

# 3. On another fresh copy, use .extend(extras)
copy2 = morning.copy()
copy2.extend(extras)
print("extend result:", copy2)
``` prints out:
breakfast: ['eggs', 'toast', 'jam', 'coffee']
morning: ['eggs', 'toast']
append result: ['eggs', 'toast', ['jam', 'coffee']]
extend result: ['eggs', 'toast', 'jam', 'coffee'] ```

### ✏️ Task: 2D List (grid)

```python
# board = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# 1. Print the value in row 2, column 0.
# 2. Change the center value to 0.
# 3. Loop over the board and print each row on its own line.
```
board = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
 ]
# 1. Print the value in row 2, column 0.
print(board[2][0])

# 2. Change the center value to 0.
board[1][1] = 0

# 3. Loop over the board and print each row on its own line.
for row in board:
    print(row)
``` prints out:
7
[1, 2, 3]
[4, 0, 6]
[7, 8, 9]
```

### ✏️ Task: Deleting Items

```python
# Given: queue = ['Ana', 'Ben', 'Cy', 'Dana', 'Eve']
# 1. Remove 'Cy' by value.
# 2. Use .pop() to remove and capture the last person into a variable "served".
# 3. Use del to remove the first person.
# 4. Print the remaining queue and "served".
```
queue = ['Ana', 'Ben', 'Cy', 'Dana', 'Eve']

# 1. Remove 'Cy' by value.
queue.remove('Cy')

# 2. Use .pop() to remove and capture the last person.
served = queue.pop()

# 3. Use del to remove the first person.
del queue[0]

# 4. Print the remaining queue and served.
print("Remaining queue:", queue)
print("Served:", served)
``` prints out:
Remaining queue: ['Ben', 'Dana']
Served: Eve```
### ✏️ Task: Iterate by Index

```python
# Given: prices = [10, 20, 30, 40]
# 1. Use "for i in range(len(prices)):" to print each item as "0: 10", "1: 20", ...
# 2. Using the index, add 5 to every price in place, then print the list.
# 3. Rewrite step 1 using enumerate() instead.
```
prices = [10, 20, 30, 40]

# 1. Print each item as "index: value"
for i in range(len(prices)):
    print(f"{i}: {prices[i]}")

# 2. Add 5 to every price in place
for i in range(len(prices)):
    prices[i] += 5

print("Updated prices:", prices)

# 3. Rewrite step 1 using enumerate()
for i, price in enumerate(prices):
    print(f"{i}: {price}")
``` prints out:
0: 10
1: 20
2: 30
3: 40
Updated prices: [15, 25, 35, 45]
0: 15
1: 25
2: 35
3: 45 ```
### 🤖 Explain It

In your own words: what's the difference between a list and a slice of a list? Is slicing a list the same as modifying it? And when you write `a.append(b)` versus `a.extend(b)`, what ends up in `a` each way?

---
A list contains all the items. A slice creates a new list containing only the selected items from the original list. 
No, slicing a list is not same as modifying it. Slicing creates a new list containing the chosen elements.
The quick note as below:
- List = the original collection of items.
- Slice = a new list containing selected items from original list.
- Slicing does not modify the original list.
- append(b) adds b as one item.
- extend(b) adds every item from b separately.

## 🔒 Section 2: Tuples

5. What is a key difference between a list and a tuple?  
   `Answer:` The key difference is that lists are mutable and tuples are immutable.

6. Can you change the contents of a tuple once it is created? Why or why not?  
   `Answer:` Tuples are immutable, meaning that once it's created  you cannot change or modify the tuples.

7. What does `first, *rest = (10, 20, 30, 40)` assign to `first` and `rest`?  
   `Answer:` first gets the first value: 10. `rest` collects all remaining values into a list: [20, 30, 40]. Python uses unpacking for that.

---

### ✏️ Task: Tuple Practice

```python
# Create a tuple with your favorite 3 numbers.
# Unpack it into three variables and print each.
```
favorite_numbers = (7, 14, 21)
# Unpack the tuple into three variables
first, second, third = favorite_numbers
# Print each variable
print(first)
print(second)
print(third)
# result: 
       7
       14
       21
### ✏️ Task: Unpacking with *rest

```python
# Given: race_times = (9.58, 9.63, 9.69, 9.71, 9.74)
# Unpack this into "winner" (the first time) and "others" (everything else).
# Print both.
```
race_times = (9.58, 9.63, 9.69, 9.71, 9.74)
Winner = race_times[0]
print("Winner: the first time", Winner)
others = race_times[1:5]
print("Others: everything else", others) 
# result:
Winner: the first time 9.58
Others: everything else (9.63, 9.69, 9.71, 9.74)
### ✏️ Task: Tuples as Dictionary Keys

```python
# Build a dictionary called "distances" where the keys are (city1, city2)
# tuples and the values are the distance in miles between them.
# Add at least two entries, then look up and print one of them.
```
distances = {
    ("Dallas", "Austin"): 195,
    ("Wichita Falls", "Dallas"): 142
}
# Look up and print one distance
print(distances[("Wichita Falls", "Dallas")])

# reult: 142
### 🤖 Explain It

In your own words: why does Python allow a tuple to be a dictionary key, but not a list? What property makes that possible?

---
Tuples are immutable and that property made a perfect choice to be a dictionary key. Lists are mutable meaning you can change or modify it.```

## 🔑 Section 3: Dictionaries

8. What does the `.get()` method do differently from accessing a key directly with `[]`?  
   `Answer:` dict[key] raises a KeyError when the key is missing, while dict.get(key) returns None (or a default value you specify) instead of raising an error.

9. How do you loop through both keys and values in a dictionary?  
   `Answer:` Use a for loop with .items() method

10. How would you remove a key from a dictionary and also capture the value it held?  
    `Answer:`dict.pop(key) to remove a key and capture the value it held.

11. In a list of dictionaries like `people = [{'name': 'Ana'}, {'name': 'Ben'}]`, how do you get Ben's name?  
    `Answer:` 
people = [{'name': 'Ana'}, {'name': 'Ben'}]

print(people[1]['name'])

12. If the same dictionary object is stored in both a list and another dictionary, and you change it through one, does the other see the change? Why?  
    `Answer:` Variables, lists, and dictionaries hold references to objects. If two references point to the same dictionary, changes made through one reference are visible through the other because they both refer to the same object in memory.

---

### ✏️ Task: Dictionary Practice

```python
# Create a dictionary with keys: 'name', 'age', and 'hobby'.
# Print each key and value in the format "key: value".
```
Person = {"name": "John", "age": 30, "hobby": "Reading"}
# Print each key and value
Person = {"name": "John", "age": 30, "hobby": "Reading"}
# Print each key and value
for key, value in Person.items():
    print(f"{key}: {value}")
```
# result:
name: John
age: 30
hobby: Reading
### ✏️ Task: Build from Two Lists

```python
# Given: products = ['pen', 'notebook', 'eraser']
#        prices = [1.50, 3.25, 0.75]
# Build a dictionary mapping each product to its price.
# Print the total cost of all products (hint: sum the .values()).
```

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
# result:
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
```
inventory = {
    'apples': {'count': 50, 'price': 0.50},
    'bananas': {'count': 30, 'price': 0.25},
}

# Loop through inventory and print each fruit's information
for fruit, details in inventory.items():
    print(f"{fruit}: {details['count']} units at ${details['price']:.2f}")
```
# results:
apples: 50 units at $0.50
bananas: 30 units at $0.25

### ✏️ Task: List of Dictionaries (table rows)

```python
# roster = [
#     {'name': 'Alex', 'major': 'CS'},
#     {'name': 'Ana',  'major': 'Math'},
#     {'name': 'Ben',  'major': 'History'},
# ]
# 1. Loop over roster and print "name - major" for each student.
# 2. Add a new student record to the list.
# 3. Build and print a list of just the names of everyone majoring in 'CS'.
```
roster = [
    {'name': 'Alex', 'major': 'CS'},
    {'name': 'Ana',  'major': 'Math'},
    {'name': 'Ben',  'major': 'History'},
]

# 1. Loop over roster and print "name - major" for each student.
for student in roster:
    print(f"{student['name']} - {student['major']}")

# 2. Add a new student record to the list.
roster.append({'name': 'Chris', 'major': 'CS'})

# 3. Build and print a list of just the names of everyone majoring in 'CS'.
cs_students = []

for student in roster:
    if student['major'] == 'CS':
        cs_students.append(student['name'])

print(cs_students)
# results:
Alex - CS
Ana - Math
Ben - History
['Alex', 'Chris']
### ✏️ Task: Update a Record by Row Number

```python
# Using the roster above:
# 1. Build a dict "by_row" mapping each row number to its record
#    (hint: {i: row for i, row in enumerate(roster)}).
# 2. Change the major of the student in row 2 to 'CS'.
# 3. Print roster[2] and explain why it changed too.
```
roster = [
    {'name': 'Alex', 'major': 'CS'},
    {'name': 'Ana',  'major': 'Math'},
    {'name': 'Ben',  'major': 'History'},
]

# 1. Build a dict mapping row numbers to records.
by_row = {i: row for i, row in enumerate(roster)}

# 2. Change the major of the student in row 2 to 'CS'.
by_row[2]['major'] = 'CS'

# 3. Print roster[2].
print(roster[2])
# print out:
{'name': 'Ben', 'major': 'CS'}
### 🤖 Explain It

In your own words: what's the difference between `student['gpa']` and `student.get('gpa')` when `'gpa'` isn't in the dictionary? Which would you use, and when? Also: why does changing `by_row[2]` also change `roster[2]`?

---
student[gpa] is looking for the key "gpa" and prints it value. It raises a KeyError if 'gpa' is missing. however, student.get('gpa') shows the gpa vlaue and if the key is missing thaen it gives a default value or "None".
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
text = "to be or not to be that is the question"

counts = {}

for word in text.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
```
# using collections.counter
from collections import Counter

text = "to be or not to be that is the question"

counts = Counter(text.split())
print(counts)
# prints out:
Counter({'to': 2, 'be': 2, 'or': 1, 'not': 1, 'that': 1, 'is': 1, 'the': 1, 'question': 1})
### ✏️ Task: Parse Some JSON

```python
import json
raw = '''
{
  "course": "Programming for Data Science",
  "online": true,
  "instructor": null,
  "students": [
    {"name": "Alex", "grade": 91},
    {"name": "Ana",  "grade": 88}
  ]
}
'''
# 1. Use json.loads(raw) to turn this into Python objects.
# 2. Print the course name and the second student's grade.
# 3. Print the Python type of the value that came from "online" and from "instructor".
```
import json

raw = '''
{
  "course": "Programming for Data Science",
  "online": true,
  "instructor": null,
  "students": [
    {"name": "Alex", "grade": 91},
    {"name": "Ana",  "grade": 88}
  ]
}
'''

# 1. Convert JSON to Python objects.
data = json.loads(raw)

# 2. Print the course name and the second student's grade.
print(data["course"])
print(data["students"][1]["grade"])

# 3. Print the Python types of "online" and "instructor".
print(type(data["online"]))
print(type(data["instructor"]))
# prints out:
Programming for Data Science
88
<class 'bool'>
<class 'NoneType'>
### ✏️ Task: Walk a GeoJSON FeatureCollection

```python
geo = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature",
         "geometry": {"type": "Point", "coordinates": [-98.529, 33.878]},
         "properties": {"name": "Bolin Hall"}},
        {"type": "Feature",
         "geometry": {"type": "Point", "coordinates": [-98.531, 33.876]},
         "properties": {"name": "Moffett Library"}},
    ],
}
# Loop over geo["features"] and print each building's name with its
# latitude and longitude. Remember: coordinates are [longitude, latitude].
```
geo = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature",
         "geometry": {"type": "Point", "coordinates": [-98.529, 33.878]},
         "properties": {"name": "Bolin Hall"}},
        {"type": "Feature",
         "geometry": {"type": "Point", "coordinates": [-98.531, 33.876]},
         "properties": {"name": "Moffett Library"}},
    ],
}

for feature in geo["features"]:
    name = feature["properties"]["name"]
    lon = feature["geometry"]["coordinates"][0]
    lat = feature["geometry"]["coordinates"][1]

    print(f"{name}: Latitude = {lat}, Longitude = {lon}")
# prints out:
Bolin Hall: Latitude = 33.878, Longitude = -98.529
Moffett Library: Latitude = 33.876, Longitude = -98.531
---

## 🧾 Submit Checklist

- [X] I practiced creating, slicing, sorting, and filtering lists.
- [X] I can explain the difference between `+`, `append()`, and `extend()`.
- [X] I built and traversed a nested (2D) list.
- [X] I removed list items with `remove()`, `pop()`, and `del`.
- [X] I looped by index with `range(len(...))` and with `enumerate()`.
- [X] I understand how tuples are different from lists, and why that makes them hashable.
- [X] I accessed, looped through, updated, and removed items from a dictionary.
- [X] I built a dictionary from two separate lists.
- [ X] I worked with at least one nested dictionary.
- [X] I processed a list of dictionaries as table rows and updated a record by row number.
- [X] I parsed JSON with `json.loads()` and walked a GeoJSON FeatureCollection.
- [X] I completed the "Explain It" prompts in my own words.
