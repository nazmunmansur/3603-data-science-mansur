# 📝 Quiz: 05 - Loops and Iteration

20 questions covering for loops, while loops, file loops with `with`, and the "going further" topics from the Challenge sections. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first — the Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — For Loops

**1.** (Code Tracing) What prints?
```python
for i in range(3, 6):
    print(i)
```
Answer:
3
4
5
**2.** (Multiple Choice) Which function gives you both the index and the value in a `for` loop?
A) `zip()`  B) `enumerate()`  C) `range()`  D) `index()`
answer: B
**3.** (Code Tracing) What prints (both lines)?
```python
for i, f in enumerate(['a', 'b']):
    print(i, f)
```
answer:
0 a
1 b
**4.** (Code Tracing) What prints (both lines)?
```python
for name, score in zip(['Ana', 'Ben'], [90, 85]):
    print(name, score)
```
answer: zip() prints both line:
Ana 90
Ben 85
**5.** (Short Answer) What's the main difference between Python's `for` loop and C++'s classic three-part `for` loop?
answer: Python's for loop iterates directly over items in an iterable, while C++'s classic for loop requires explicit initialization, condition checking, and updating of a loop variable.
**6.** (True/False) `range(5)` includes the number `5`.
answer: False
**7.** (Code Tracing) List all the pairs this prints, in order:
```python
for i in range(2):
    for j in range(2):
        print(i, j)
```
answer:
0 0
0 1
1 0
1 1
---

## Section B — While Loops

**8.** (Code Tracing) What prints?
```python
n = 0
while n < 3:
    print(n)
    n += 1
```
answer:
0
1
2
**9.** (Short Answer) What causes an infinite loop?
answer: An infinite loop happens when a loop's stopping condition never becomes False, so the loop keeps running forever.
**10.** (Short Answer) In VS Code, what's the practical fix if you accidentally create one?
answer: Stop the debugger with the red Stop button (running in debug mode).
**11.** (Code Tracing) What prints, in order?
```python
n = 0
while n < 5:
    n += 1
    if n == 2:
        continue
    if n == 4:
        break
    print(n)
```
answe:
1
3
**12.** (Multiple Choice) Which loop construct does C++ have that Python has no dedicated version of?
A) `for`  B) `while`  C) `do`/`while`  D) `foreach`
answer: C
**13.** (Short Answer) What is a "sentinel value" in the context of a loop?

---
answer: A sentinel value is a special value used to signal that a loop should stop.
## Section C — File Loops

**14.** (Short Answer) What does the `with` statement guarantee when you use it to open a file?
answer: The with statement guarantees that the file is properly closed when you're done with it, even if an error occurs while the file is being processed.
**15.** (Short Answer) When looping over lines in a file, why does `print(line.strip())` usually look better than `print(line)`?
answer: .strip() removes the newline character at the end of each line, preventing unwanted blank lines and making the output look cleaner.
**16.** (Short Answer) Why should code that opens a file often be wrapped in `try`/`except`?
answer: You should wrap file-opening code in a try/except block because file operations can fail, and try/except lets your program handle those errors gracefully instead of crashing.
**17.** (Multiple Choice) What exception is raised when you try to open a file that doesn't exist?
A) `ValueError`  B) `FileNotFoundError`  C) `IOError`  D) `NameError`
answer: B
**18.** (Short Answer) What does `line.strip().split(',')` do to a line of text?

---
answer: line.strip().split(',') removes the newline and surrounding whitespace, then splits the line into a list of values separated by commas.
## Section D — Going Further (Bonus)

**19.** (Short Answer) What does the walrus operator `:=` do differently from a regular `=`?
answer: The walrus operator (:=) lets you assign a value and use it in an expression at the same time.
**20.** (Code Tracing) What prints, in order?
```python
count = 0
while (count := count + 1) <= 3:
    print(count)
```
answer:
1
2
3
---

## ✅ Answer Key

1. `3`, `4`, `5`
2. **B** — `enumerate()`.
3. `0 a` then `1 b`.
4. `Ana 90` then `Ben 85`.
5. Python's `for` loop is a for-each loop — it hands you each item directly with no index to manage. C++'s classic `for` requires you to declare, check, and increment an index yourself.
6. **False** — `range(5)` is stop-exclusive, so it produces `0, 1, 2, 3, 4`.
7. `0 0`, `0 1`, `1 0`, `1 1`.
8. `0`, `1`, `2`.
9. The loop's condition never becomes `False` — usually because whatever variable the condition depends on is never updated (or updated in a way that never satisfies the exit condition).
10. Click the Interrupt/Stop button next to the running cell (or Kernel → Interrupt) to stop execution.
11. `1`, `3` — `2` is skipped by `continue`, and the loop stops before printing `4` because of `break`.
12. **C** — `do`/`while`.
13. A special value (like `'quit'`) that a loop watches for to know when to stop, typically checked inside a `while True:` loop with `break`.
14. It guarantees the file gets closed automatically once the block ends — even if an error happens inside it — without you having to call `.close()` yourself.
15. Each line from a file includes the trailing newline character; `.strip()` removes it, so `print()` doesn't add an extra blank line on top of it.
16. The file might not exist, might be in the wrong location, or might not be readable — `try`/`except` lets the program handle that gracefully instead of crashing.
17. **B** — `FileNotFoundError`.
18. It first removes leading/trailing whitespace (including the newline), then splits what's left into a list wherever a comma appears.
19. `:=` assigns a value **and** evaluates to that value in the same expression, so you can assign and check a condition in one line instead of two.
20. `1`, `2`, `3` — each pass increments `count` and checks the new value in the same expression; the loop stops once `count` reaches `4`.
