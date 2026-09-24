# 📝 Worksheet: 04 - Functions

Use this worksheet to reinforce your understanding of defining and calling functions, flexible arguments, and type-based behavior. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧠 Section 1: Function Basics

1. What's the difference between a parameter and an argument?  
   `Answer:` __A parameter is the variable listed in a function's definition. And an argument is the actual value used in the function when you call it._____________________

2. What does this function return if called as `mystery(5)`?

```python
def mystery(x):
    y = x * 2
    print(y)
```

   `Answer:` ____________10___________ (careful — this is a trick question)

3. Rewrite this so it actually returns a usable value instead of just printing it:

```python
def area(length, width):
    print(length * width)
```

   `Answer:` ___def area(length, width):
                     return length * width
               area(5, 10)____________________
result: '50'
---

### ✏️ Task: Default Values

```python
# Write a function `power(base, exponent=2)` that returns base raised to exponent.
# Call it once with just a base (should square it), and once with both arguments.
```
def power(base, exponent=2):
    return base ** exponent

print(power(5))        # 25
print(power(5, 3))     # 125
### ✏️ Task: Scope

```python
# Predict, then check: what does this print?
count = 0
def increment():
    count = count + 1
    return count
print(increment())
print(count)
# (Hint: this is the local-vs-global lesson biting you. You do NOT need to fix it yet.)
```
It returns an error: cannot access local variable 'count' where it is not associated with a value.
### 🤖 Explain It

In your own words: why did the "Task: Scope" code above not update the outer `count`? What would you have to do differently if you actually wanted to change a global variable from inside a function?

---count = 0
def increment(count=count): # "defining count inside the funtion so it will work as local variable."
    count = count + 1
    return count
print(increment())
print(count) 
Prints hte result: 1
0

## 🔁 Section 2: Flexible Arguments

4. What does `*args` collect its extra arguments into?  
   `Answer:` _____Tuple__________________

5. What does `**kwargs` collect its extra arguments into?  
   `Answer:` _________dictionary (dict)______________

6. What will this print?

```python
def describe(**info):
    print(info)

describe(name='Ada', role='Mathematician')
```

   `Answer:` ______{'name': 'Ada', 'role': 'Mathematician'}_________________

---

### ✏️ Task: Variable-Length Averaging

```python
# Write a function `average(*nums)` that returns the average of any amount of numbers.
# Test it with 2 numbers, then with 6.
```
def average(*nums):
    return sum(nums) / len(nums) if nums else 0

print(average(1, 2))        # 1.5
print(average(1, 2, 3, 4, 5, 6))     # 3.5
### ✏️ Task: Flexible Profile Builder

```python
# Write a function `build_profile(name, **details)` that returns a dictionary
# with 'name' plus whatever other keyword arguments were passed in.
# Call it with name plus at least 3 other details (e.g. major='CS', year=2).
```
def build_profile(name, **details):
    profile = {'name': name}
    profile.update(details)
    return profile

print(build_profile("Alice", major="CS", year=2)) 
result:
{'name': 'Alice', 'major': 'CS', 'year': 2}
### 🤖 Explain It

In your own words: why does Python require regular parameters first, then `*args`, then `**kwargs` — what would go wrong if you could put them in any order?

---
Answer: Python would have difficulty to determine the required parameter and collect extra positional arguments(*args) into a tuple and extra keyword arguments (*kwargs) into a dictionary. which will make the language muuch more complicated and error-prone.
## 🎭 Section 3: Type-Based Behavior

7. Why can't you define two functions both named `calculate_area`, one for circles and one for rectangles, the way you could in C++?  
   `Answer:` In Python, a function name refers to one function object at a time, so a later def calculate_area(...) simply replaces the earlier one.

8. What will this print?

```python
def classify(x):
    if isinstance(x, bool):
        return 'boolean'
    elif isinstance(x, int):
        return 'integer'
    else:
        return 'something else'

print(classify(True))
```

   `Answer:` ____boolean___________________ (careful — `bool` is technically a subclass of `int` in Python, which is why the `bool` check has to come first)

9. What's one advantage of `isinstance(x, (int, float))` over just `isinstance(x, int)` when checking "is this a number"?  
   `Answer:` __Making it a simple way to accept multiple numeric types with one test._____________________

---

### ✏️ Task: Type-Branching Function

```python
# Write a function `describe_input(x)` that:
#   - if x is a list, prints how many items it has
#   - if x is a string, prints how many characters it has
#   - if x is a number, prints whether it's positive, negative, or zero
# Test it on a list, a string, and a number.
```
```
def describe_input(x):
    if isinstance(x, list):
        print(f'This is a list with {len(x)} items.')
    elif isinstance(x, str):
        print(f'This is a string with {len(x)} characters.')
    elif isinstance(x, (int, float)):
        if x > 0:
            print('This is a positive number.')
        elif x < 0:
            print('This is a negative number.')
        else:
            print('This is zero.')
    else:
        print('Unknown type.')

describe_input([1, 2, 3])  # This is a list with 3 items.  
describe_input('hello data scientist')  # This is a string with 21 characters.  
describe_input(-42)  # This is a negative number.
describe_input('oops')  # This is a string with 4 characters.
```
### ✏️ Task: Compare to dict.get()

```python
# Given: settings = {'theme': 'dark'}
# 1. Use settings.get('font_size', 12) to get a font size with a fallback.
# 2. Write a function get_display_name(value) that returns str(value) if value
#    is a number, or value itself if it's already a string.
# In a comment, explain how these two are "the same kind of decision."
```
settings = {'theme': 'dark'}
font_size = settings.get('font_size', 12)
def get_display_name(value):
    if isinstance(value, (int, float)):
            return str(value)
    elif isinstance(value, str):
            return value
print(font_size)  # 12
print(get_display_name('Dark'))  # 'Dark'

# Both patterns are trying to avoid failure by choosing an alternative when the ideal case is not available.
### 🤖 Explain It

In your own words: what is duck typing, and can you think of a real-world (non-code) example of judging something by how it behaves rather than by its label?

---
Duck typing is determining whether an object can perform the required action rather than checking its type. It is based on the idea, "If it walks like a duck and quacks like a duck, it's probably a duck." Instead of asking what an object is, duck typing asks what the object can do.

## 🚀 Section 4: Going Further (Optional)

These pair with the "🔥 Challenge" sections in the notebooks — skip if you haven't gotten there yet.

### ✏️ Task: Mutable Default Gotcha

```python
# Given this buggy function:
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags

# Call add_tag('python') twice in a row and print the result each time.
# Then rewrite the function using tags=None so each call starts fresh.
```
    
# Call add_tag('python') twice in a row and print the result each time.
print(add_tag('python'))
print(add_tag('python'))
# result:
['python']
['python', 'python']

# Then rewrite the function using tags=None so each call starts fresh.
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags
print(add_tag('python'))
print(add_tag('python'))
# result:
['python']
['python']
### ✏️ Task: Unpacking Into a Call

```python
# Given: def volume(length, width, height): return length * width * height
# Given: dimensions = [3, 4, 5]
# Call volume() by unpacking "dimensions" with *, instead of writing out
# volume(dimensions[0], dimensions[1], dimensions[2]).
```
def volume(length, width, height): return length * width * height
dimensions = [3, 4, 5]
# Call volume() by unpacking "dimensions" with *, instead of writing out
print(volume(*dimensions))  # Output: 60
---

## 🧾 Submit Checklist

- [X] I wrote a function that returns a value (not just prints one).
- [X] I wrote a function with a default parameter value.
- [X] I wrote a function using `*args` and one using `**kwargs`.
- [X] I wrote a function that branches its behavior based on `isinstance()`.
- [X] I completed the "Explain It" prompts in my own words.
