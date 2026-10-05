# 📝 Worksheet: 02 - Scalar Types and Control Flow

Use this worksheet to reinforce your understanding of variables, arithmetic, comparisons, and decision logic. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧠 Section 1: Scalar Types and Casting

1. What is the output of the following code?

```python
x = 10
print(type(x))
```

   `Answer:` _____<class 'int'>__________________

2. What scalar type would best represent:
   - A person's name: __String_____
   - Their age: __Intiger_____
   - Whether they passed a test: _Bool______

3. Why does `int('21')` work, but `int('twenty-one')` raise an error?  
   `Answer:` __int('twenty-one') raises a ValueError because Python can only convert strings that are valid numeric representations. The text 'twenty-one' is a word, not a number written in digits._____________________

---

### ✏️ Task: Type Practice

```python
# Create a variable for each type and print its value and type.
# Example: an int, float, str, and bool.
```
age = 21              
gpa = 3.75            
name = "Ben"        
passed = True         

print(age, type(age))
print(gpa, type(gpa))
print(name, type(name))
print(passed, type(passed))
Result:
21 <class 'int'>
3.75 <class 'float'>
Ben <class 'str'>
True <class 'bool'>
### ✏️ Task: Arithmetic

```python
# Given: hours_worked = 37, hourly_rate = 15.50
# Print the total pay.
# Print the total pay rounded to 2 decimal places (hint: round()).
```
hours_worked = 37
hourly_rate = 15.50
total_pay = hours_worked * hourly_rate
print(round(total_pay, 2))
print(f"${total_pay:.2f}")
result:
573.5
$573.50
### ✏️ Task: Casting Round Trip

```python
# Given: user_input = "3.14159"
# Convert it to a float, then print it rounded to 2 decimal places.
```
user_input = "3.14159"
pi = float(user_input)
print(pi)
print(round(pi, 2))
resilt:
3.14159
3.14
### 🤖 Explain It

In your own words: why does `input()` always return a string, and why does that matter when you want to do math with what the user typed?

---`input()` always return a string thats's why user needds to define it as int or float when doing mathmetical calculations.

## 🔁 Section 2: Comparison Operators

4. What does the `!=` operator mean?

   `Answer:` _____The != operator means "not equal to."__________________

5. What will the following code print?

```python
a = 5
b = 3
print(a < b or b < 10)
```

   `Answer:` ______True_________________

6. What does `0 <= score <= 100` check, and how would you write the same thing *without* chaining?  
   `Answer:` _score = 85
print(0 <= score <= 100)
retuns the result True. 
without chaining: 0 <= score and score <= 100

---

### ✏️ Task: Comparison Practice

```python
# Given: temperature = 98.6
# Print True if it's within normal human body temperature range (97.0 to 99.0), else False.
# Try it both as a chained comparison and as two separate comparisons joined with "and".

temperature = 98.6
# Chained comparison
print(97.0 <= temperature <= 99.0)
# Two comparisons joined with "and"
print(temperature >= 97.0 and temperature <= 99.0)
```
### 🤖 Explain It

In your own words: what's the difference between `=` and `==` in Python? Why does mixing them up cause errors (or worse, silently wrong code)?

**If you've written C++:** explain why `0 <= score <= 100` is safe to write in Python but dangerous to write in C++. What does the C++ version actually evaluate to, and how would you fix it?

---Difference between the two operators as below:
'='is the assignment operator. It puts a value into a variable.
'==' is the comparison operator. It checks whether two values are equal.
In C++, the expression is evaluated left to right, meaning is if the condition is 0 <= score <= 100, for the score = 150 it will read as 0 <= 150 true, then true is converted to the integer 1: 1 <= 100 as true. So the entire expression incorrectly evaluates to true even though 150 is not between 0 and 100.
The fix is to using the && operator as 0 <= score && score <= 100

## 🔀 Section 3: Control Flow

7. Write a conditional that prints "Pass" if a grade is >= 70, and "Fail" otherwise.

```python
# Your code:
grade = 75

if grade >= 70:
    print("Pass")
else:
    print("Fail")
```
Pass
8. What does `elif` allow you to do that separate `if` statements don't?  
   `Answer:` ____elif allows you to check additional conditions in the same decision chain.___________________

9. What will this print?

```python
age = 16
has_ticket = False
print(age >= 13 and has_ticket)
```

   `Answer:` ____False___________________

---

### ✏️ Task: Multi-Branch Logic

```python
# Given: bmi = 22.5
# Print the BMI category:
# "Underweight" (< 18.5), "Normal" (18.5-24.9), "Overweight" (25-29.9), "Obese" (30+)
```
```
bmi = 22.5
if bmi < 18.5:
    print("Underweight")
elif bmi > 18.5 and bmi < 24.9:
    print("Normal")
elif bmi > 25 and bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
```
Result: Normal
### ✏️ Task: Multi-Line Branches

```python
# Given: cart_items = 3, member_since_days = 400
# In the if-branch (member_since_days >= 365): compute a "loyalty discount" of 15%,
#   print the discount amount, and print the final price.
# In the else-branch: print that there's no discount yet, and print the full price.
# Use item_price = 20.00 per item as the starting subtotal.
# Each branch should have at least 3 lines — this is the same shape as the
# "One Branch, Many Lines" example in the notebook.
```
cart_items = 3
member_since_days = 400
item_price = 20.00

subtotal = cart_items * item_price

if member_since_days >= 365:
    discount = subtotal * 0.15
    final_price = subtotal - discount
    print("Loyalty discount:", round(discount, 2))
    print("Final price:", round(final_price, 2))
    print("Thanks for being a loyal member!")
else:
    print("No discount yet.")
    print("Full price:", round(subtotal, 2))
    print("Become a member for 365+ days to earn a discount.")
result:
Loyalty discount: 9.0
Final price: 51.0
Thanks for being a loyal member!
### ✏️ Task: Your Turn

Write a program that asks for the weather and prints:
- "Bring sunscreen" if it's sunny
- "Take an umbrella" if it's raining
- "Check the forecast" otherwise
```
weather = "sunny"

if weather == "sunny":
    print("Bring sunscreen")
elif weather == "raining":
    print("Take an umbrella")
else:
    print("Check the forecast")
```
result: Bring sunscreen
### 🤖 Explain It

In your own words: what's the difference between using `and` versus writing nested `if` statements to check two conditions? Do they always produce the same result?

---
'and' is used to see all conditions are true. nested if statements is used to check conditions one at a time or perform different actions depending on which condition succeeds or fails.
## 🚀 Section 4: Going Further (Optional)

These pair with the "🔥 Challenge" sections in the notebooks — skip if you haven't gotten there yet.

### ✏️ Task: Conditional Expression

```python
# Rewrite this as a one-line conditional expression:
# if temperature > 90:
#     comfort = "too hot"
# else:
#     comfort = "fine"
```
comfort = "too hot" if temperature > 90 else "fine"
### ✏️ Task: Float Precision

```python
# Predict, then check: does 0.1 + 0.1 + 0.1 == 0.3 evaluate to True or False in Python?
# Write a "close enough" check instead of using == directly.
```
a = 0.1
b = 0.1
c = 0.1
def close_enough(a, b, c):
    # Your code here
    pass
    return abs(a - b) < 0.0001 and abs(b - c) < 0.0001
print(0.1 + 0.1 + 0.1)

print(close_enough(0.1 + 0.1 + 0.1, 0.3, 0.3))  # Should return True

reesult: 0.30000000000000004
True

### ✏️ Task: Match Statement

```python
# Given: grade_letter = 'B'
# Use match/case to print:
#   "Excellent" for 'A'
#   "Good" for 'B' or 'C'
#   "Needs improvement" for anything else (use the "_" wildcard case)
```
grade_letter = 'B'

match grade_letter:
    case 'A' :
        print('Excellent')
    case 'B' | 'C':
        print('Good')
    case _:
        print('Needs improvement')
```
result: 'Good'

### 🤖 Explain It

**If you've written C++:** how is Python's `match`/`case` similar to a C++ `switch`? What can `match` do (strings, multiple values per case with `|`) that a plain C++ `switch` can't?

---If you know C++'s `switch`, this is the same idea, but more flexible — Python's `match` can work on strings (not just integers/enums) and can match multiple values in one `case` using `|`. Python's match is generally much more powerful and flexible than a traditional C++ switch.

## 🧾 Submit Checklist

- [ X] I practiced creating and casting each scalar type.
- [X ] I used arithmetic operators, including `//` and `%`.
- [X ] I wrote conditionals using comparison and logical operators.
- [X ] I used a chained comparison at least once.
- [X ] I wrote at least one branch with multiple lines inside it.
- [X ] I completed the "Explain It" prompts in my own words.
