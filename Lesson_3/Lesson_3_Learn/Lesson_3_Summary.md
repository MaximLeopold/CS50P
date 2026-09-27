# Lesson 3 Summary: Loops, Lists, Dictionaries, and Tuples

This lesson introduces ways to repeat code and work with collections of data. The main ideas are:

- `while` loops repeat while a condition remains true.
- `for` loops process the items in an iterable, such as a list, string, dictionary, or `range`.
- Lists store ordered collections of values.
- Dictionaries store relationships between keys and values.
- Tuples store ordered groups of values that should not change.
- `break`, `continue`, and `return` control what happens during repetition.
- Functions can separate input, validation, and output into clear responsibilities.

## 1. What is a loop?

A loop repeatedly executes an indented block of code. One execution of that block is called an **iteration**.

Python has two main loop statements:

```python
while condition:
    # Repeat while the condition is true
```

```python
for item in iterable:
    # Repeat once for each item
```

A useful rule of thumb is:

- Use `while` when repetition depends on a condition and the number of repetitions may be unknown.
- Use `for` when processing a collection or repeating a known number of times.

## 2. `while` loops

A `while` loop checks its condition before every iteration. It stops when the condition becomes `False`.

```python
i = 3

while i != 0:
    print("Meow")
    i = i - 1
```

The execution is:

| Check | Result | Action |
|---|---|---|
| `3 != 0` | `True` | Print `Meow`; change `i` to `2` |
| `2 != 0` | `True` | Print `Meow`; change `i` to `1` |
| `1 != 0` | `True` | Print `Meow`; change `i` to `0` |
| `0 != 0` | `False` | Stop |

The shorter form of the update is:

```python
i -= 1
```

This means the same basic thing as:

```python
i = i - 1
```

The counter can also increase:

```python
i = 0

while i < 3:
    print("Woof")
    i += 1
```

It is important that something eventually makes the condition false. Otherwise, the loop will continue indefinitely.

## 3. Infinite loops and input validation

`True` is always true, so this creates a deliberate infinite loop:

```python
while True:
    n = int(input("How often does the dog bark? "))

    if n > 0:
        break
```

This pattern is useful for validation:

1. Ask the user for input.
2. Test whether it is valid.
3. Leave the loop if it is valid.
4. Otherwise, return to the top and ask again.

If the user enters `0` or a negative integer, `n > 0` is false. Python reaches the bottom of the loop and begins another iteration.

Entering non-numeric text still causes `int()` to raise a `ValueError`. Handling that requires `try` and `except`, which is covered later in the course.

### Repeating while external state changes

A `while` loop can repeatedly check a changing measurement:

```python
moisture = sample()
print(f"Moisture is {moisture}%")

while moisture > 20:
    moisture = sample()
    print(f"Moisture is {moisture}%")

print("Time to water")
```

This pattern works as follows:

1. Take an initial sample before the loop so that `moisture` exists when the condition is first checked.
2. Continue looping while `moisture > 20` is true.
3. Take a new sample inside the loop so the condition has a chance to change.
4. When the reading becomes `20` or lower, the condition is false and execution continues after the loop.

Updating `moisture` inside the loop is essential. Without a new sample, the condition would never change and the loop could run forever. The lesson's `from soil import sample` line is conceptual and requires an actual `soil` module before the example can run.

## 4. `for` loops

A `for` loop automatically takes the next value from an iterable on each iteration:

```python
for i in [0, 1, 2]:
    print("Meow")
```

Here, `i` receives `0`, then `1`, then `2`. The value of `i` is not used by `print()`, but the list contains three items, so the loop runs three times.

### Using `range()`

`range()` produces a sequence of integers suitable for looping:

```python
for i in range(3):
    print("Woof")
```

`range(3)` represents:

```text
0, 1, 2
```

The stopping value is not included. The loop therefore runs three times.

`range()` returns a special range object, not a list, although it supplies its numbers one at a time like a sequence.

Common forms are:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Examples:

```python
range(3)        # 0, 1, 2
range(1, 4)     # 1, 2, 3
range(0, 10, 2) # 0, 2, 4, 6, 8
```

### The underscore variable

Use `_` by convention when the loop variable is required syntactically but its value is not needed:

```python
for _ in range(3):
    print("Woof")
```

`_` is still a valid variable name. It communicates that the program intentionally ignores the current value.

## 5. Loop-control statements

| Statement | Effect |
|---|---|
| `break` | Immediately exits the nearest loop |
| `continue` | Skips the rest of the current iteration and starts the next one |
| `return` | Immediately exits the entire function and optionally sends a value to its caller |

Example using `continue`:

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

Output:

```text
0
1
3
4
```

`return` is different from `break`: `break` exits only the loop, whereas `return` exits the function containing the loop.

## 6. Organizing a loop-based program with functions

The dog-barking program separates its responsibilities into functions:

```python
def main():
    number = get_number()
    woof(number)


def get_number():
    while True:
        n = int(input("How often does the dog bark? "))
        if n > 0:
            return n


def woof(n):
    for _ in range(n):
        print("Woof")


main()
```

The data flow is:

```text
main()
  -> get_number() asks for and validates input
  -> get_number() returns a positive integer
  -> main() stores it in number
  -> woof(number) receives it as n
  -> the for loop prints Woof n times
```

Important details:

- `return n` sends the valid number to `main()` and exits `get_number()`.
- `number` in `main()` and `n` in the helper functions are local variables.
- `woof(number)` passes the value stored in `number` as an argument.
- `main()` must be called after the function definitions for the program to run.

## 7. Repeating a string without a loop

Python can multiply a string:

```python
print("Woof\n" * 3, end="")
```

`"Woof\n" * 3` creates:

```text
Woof
Woof
Woof
```

The newline escape sequence is `\n`, with a backslash. `end=""` prevents `print()` from adding another newline after the string.

This works for simple repetition, but a loop is more flexible when each iteration needs additional logic.

## 8. Lists

A list is an ordered, changeable collection. Square brackets create a list:

```python
students = ["Peter", "Paul", "Mary", "John"]
```

Lists can contain strings, numbers, Boolean values, other lists, dictionaries, or mixtures of values.

### Accessing list items by index

Indexes begin at `0`:

```python
students[0]  # "Peter"
students[1]  # "Paul"
students[2]  # "Mary"
students[3]  # "John"
```

Negative indexes count backward from the end:

```python
students[-1]  # "John"
students[-2]  # "Mary"
```

Trying to use an index outside the list produces an `IndexError`.

### Iterating directly over a list

If only the values are needed, loop directly over the list:

```python
for student in students:
    print(student)
```

During each iteration, `student` receives the next value from `students`.

### Using `len()` and list indexes

`len()` returns the number of items in a collection:

```python
len(students)  # 4
```

To generate all valid indexes dynamically:

```python
for index in range(len(students)):
    print(index, students[index])
```

For a four-item list:

```text
len(students)         -> 4
range(len(students))  -> 0, 1, 2, 3
```

The output is:

```text
0 Peter
1 Paul
2 Mary
3 John
```

The final valid index is always one less than the length because indexing starts at zero.

Use direct iteration when only the values matter. Use indexes when the position is also needed:

```python
# Values only
for student in students:
    print(student)

# Index and value
for index in range(len(students)):
    print(index, students[index])
```

### Modifying lists with methods

Lists are mutable, which means their contents can be changed after creation.

```python
guests = ["Mario", "Luigi"]

guests.append("Daisy")              # Add one item at the end
guests.extend(["Yoshi", "Toad"])   # Add all items from another iterable
guests.insert(0, "Peach")           # Insert at index 0
guests.remove("Luigi")              # Remove the first matching value
last_guest = guests.pop()            # Remove and return the last item
guests.reverse()                     # Reverse the list in place
guests.clear()                       # Remove every item
```

Important differences:

| Method | Main purpose | Returned value |
|---|---|---|
| `.append(value)` | Add one value to the end | `None` |
| `.extend(iterable)` | Add several values | `None` |
| `.insert(index, value)` | Add a value at a chosen index | `None` |
| `.remove(value)` | Remove the first matching value | `None` |
| `.pop()` | Remove and return the final item | Removed item |
| `.pop(index)` | Remove and return the item at an index | Removed item |
| `.reverse()` | Reverse the existing list | `None` |
| `.clear()` | Remove all items | `None` |

Because `.pop()` returns the removed item, an undo system can save it:

```python
history = []

while True:
    action = input("Action: ")

    if action == "Undo":
        if history:
            undone = history.pop()
            print(f"Undone: {undone}")
        else:
            print("There is nothing to undo")
    elif action == "Restart":
        history.clear()
    elif action == "Quit":
        break
    else:
        history.append(action)

    print(history)
```

The test `if history:` is true when the list contains at least one item. It prevents `.pop()` from raising an `IndexError` on an empty list.

## 9. Dictionaries

A dictionary stores key-value relationships:

```python
students = {
    "Herman": "Gryffindor",
    "Peter": "Gryffindor",
    "Paul": "Ravenclaw",
    "Mary": "Ravenclaw"
}
```

Dictionary syntax uses:

- Curly braces `{}` around the collection
- A colon `:` between each key and value
- A comma `,` between key-value pairs

The relationship is:

```text
student name -> house
```

Keys must be unique and hashable. Strings, numbers, and tuples can commonly be keys; mutable objects such as lists and dictionaries cannot be keys. Values can be of any type and do not need to be unique.

### Accessing a dictionary value

Use a key inside square brackets:

```python
print(students["Herman"])
```

Output:

```text
Gryffindor
```

This is a lookup by key, not positional indexing. Dictionary keys are case-sensitive, so `"Herman"` and `"herman"` are different strings. Looking up a missing key with square brackets raises a `KeyError`.

### Iterating over a dictionary

Direct dictionary iteration produces its keys:

```python
for student in students:
    print(student)
```

To print each key and its associated value:

```python
for student in students:
    print(student, students[student])
```

On the first iteration:

```text
student                  -> "Herman"
students[student]        -> students["Herman"]
students["Herman"]      -> "Gryffindor"
```

An alternative is the `.items()` method:

```python
for student, house in students.items():
    print(student, house)
```

### Adding and updating dictionary data

Assigning to a new key adds a key-value pair:

```python
spacecraft = {
    "name": "Voyager 1",
    "distance": 163
}

spacecraft["speed"] = 0.01
```

After the assignment, the dictionary also contains the key `"speed"` with the value `0.01`.

The `.update()` method can add or replace several pairs at once:

```python
spacecraft.update({
    "orbit": "Sun",
    "crew": "5 people"
})
```

If a supplied key already exists, `.update()` replaces its old value. If it does not exist, `.update()` adds it.

A reporting function can look up values and return one formatted string:

```python
def create_report(spacecraft):
    return (
        f"Name: {spacecraft['name']}\n"
        f"Distance: {spacecraft['distance']}\n"
        f"Speed: {spacecraft['speed']}"
    )
```

The `f` creates a formatted string, `{...}` evaluates each dictionary lookup, and `return` sends the completed string back to the caller. The caller can then decide whether to print, store, or otherwise use the report.

### Dictionary methods

The extended lessons introduce these methods:

| Method | Purpose |
|---|---|
| `.keys()` | Return a view of all keys |
| `.items()` | Return key-value pairs for iteration |
| `.update({...})` | Add new pairs or replace existing values |
| `.pop(key)` | Remove a key-value pair and return its value |
| `.clear()` | Remove every key-value pair |

Looping directly over a dictionary already produces its keys, so these are equivalent:

```python
for name in distances:
    print(name)

for name in distances.keys():
    print(name)
```

Membership testing also checks keys by default:

```python
if guess in words:
    points = words.pop(guess)
```

Writing `if guess in words.keys():` works, but `.keys()` is unnecessary in this situation.

### Dictionary state in a loop

A spelling-bee program can keep looping while its dictionary still contains words:

```python
def main():
    words = {"pair": 4, "hair": 4, "chair": 5}

    print("Welcome to Spelling Bee")

    while len(words) > 0:
        print(f"{len(words)} words left!")
        guess = input("Guess a word: ").lower()

        if guess in words:
            points = words.pop(guess)
            print(f"Good job! You scored {points} points")
        else:
            print("That word is not available")

    print("You found every word!")


main()
```

The dictionary itself is the changing state:

- `len(words)` reports how many entries remain.
- `guess in words` checks whether the guess is a key.
- `words.pop(guess)` removes the guessed word and returns its points.
- Every successful guess makes the dictionary smaller.
- When the dictionary is empty, `len(words) > 0` becomes false and the loop ends.

## 10. Lists of dictionaries

When every student needs several associated properties, use a list containing dictionaries:

```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Lion"},
    {"name": "Peter", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Paul", "house": "Ravenclaw", "patronus": "Eagle"},
    {"name": "Mary", "house": "Ravenclaw", "patronus": "none"}
]
```

The outer square brackets create one list. Each pair of curly braces creates one dictionary representing one student.

Loop over the list to receive one student dictionary at a time:

```python
for student in students:
    print(student["name"])
```

Access several values from each dictionary:

```python
for student in students:
    print(student["name"], student["house"], student["patronus"])
```

In this loop, `student` is not a name string. It is an entire dictionary such as:

```python
{"name": "Hermione", "house": "Gryffindor", "patronus": "Lion"}
```

Therefore, `student["name"]` retrieves the name value from that dictionary.

## 11. Tuples

A tuple is an ordered collection whose items cannot be replaced, added, or removed after creation. This is called **immutability**.

```python
coordinates = (42.376, -71.115)
```

The tuple holds two related values as one value:

```text
index 0 -> latitude
index 1 -> longitude
```

Tuple items can be accessed by index just like list items:

```python
print(coordinates[0])  # 42.376
print(coordinates[1])  # -71.115
```

### Tuple unpacking

Tuple unpacking assigns the tuple's items to separate variables:

```python
latitude, longitude = coordinates

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
```

This is equivalent to retrieving index `0` and index `1`, but the variable names express what the values mean.

The number of variables must match the number of tuple items. This fails because a two-item tuple cannot be unpacked into three variables:

```python
latitude, longitude, altitude = coordinates
```

Technically, the comma creates a tuple; parentheses usually make it clearer:

```python
coordinates = 42.376, -71.115    # Tuple
coordinates = (42.376, -71.115)  # Same tuple, clearer
```

A one-item tuple requires a trailing comma:

```python
one_value = (42,)
```

Without the comma, `(42)` is simply the integer `42` surrounded by grouping parentheses.

Use a list when the collection should change. Use a tuple when the position and number of values are fixed and the collection should remain unchanged.

## 12. Bracket recap

| Symbols | Common uses in this lesson |
|---|---|
| `()` | Call functions and methods; group expressions; make tuple syntax clear |
| `[]` | Create lists; access list indexes; access dictionary keys |
| `{}` | Create dictionaries and sets |

On a standard German Mac keyboard:

- `[` is `Option + 5`
- `]` is `Option + 6`
- `{` is `Option + 8`
- `}` is `Option + 9`

## 13. Choosing the appropriate pattern

| Goal | Typical pattern |
|---|---|
| Repeat while a condition remains true | `while condition:` |
| Keep asking until input is valid | `while True` with `break` or `return` |
| Repeat a known number of times | `for _ in range(n):` |
| Process every value in a list | `for value in values:` |
| Process list positions and values | `for index in range(len(values)):` |
| Process dictionary keys | `for key in dictionary:` |
| Process dictionary keys and values | `for key, value in dictionary.items():` |
| Store a fixed, ordered group of values | `values = (first, second)` |

## 14. Corrections and cautions from the lesson files

1. `range(3)` is a range object representing `0, 1, 2`; it is not literally a list.
2. The stop value passed to `range()` is excluded.
3. The newline escape sequence is `\n`, not `/n`.
4. On a German Mac keyboard, the square-bracket shortcuts are `Option + 5` and `Option + 6`.
5. `return` exits the entire function, not only the loop inside it.
6. Dictionary access is more accurately called a key lookup rather than positional indexing.
7. Dictionary keys cannot be absolutely any data type; they must be hashable. Lists and dictionaries cannot be keys.
8. In `Lesson_3_Loops#2`, the introductory version and function-based version are both executable. Running the complete file asks the barking question twice. They are best treated as two alternative examples, with one version commented out while running the other.
9. In the list-method notes, `.remove("XY")` removes the string `"XY"`. Writing `.remove(["XY"])` would instead search for a nested list containing that string.
10. In the history example, `history.pop()` must be assigned with `undone = history.pop()` before `undone` can be printed. The list should also be checked before popping.
11. In `Lesson_3_Dictionaries#5`, adjacent f-strings need separators such as `\n`; otherwise, the report fields run together. Using different quote styles in `spacecraft['name']` also makes the nested strings easier to read.
12. That file defines `main()` twice. The first version is called before the second definition, while the spelling-bee version is never called. In a normal program, give the examples distinct function names or keep only one `main()` and call it at the bottom.
13. Store distance values consistently. A value such as `"100 AU"` should not be followed by another hard-coded `"AU"`, or the output becomes `100 AU AU`. Numeric values are preferable when calculations may be required.
14. `Lesson_3_Loops#6` imports `sample` from a `soil` module that is not present, so that example cannot run until the module is supplied. It also defines a second `main()` without calling it.
15. All seven lesson source files contain Python code but currently have no `.py` filename extensions. Python can still run them, but adding `.py` would improve editor and tooling recognition.

## Final mental model

```text
Variables store individual values.
Lists store ordered collections.
Dictionaries store key-value relationships.
Tuples store fixed, ordered collections.
Conditionals choose which code runs.
While loops repeat according to a condition.
For loops process the items in an iterable.
Functions organize these operations into reusable responsibilities.
```
