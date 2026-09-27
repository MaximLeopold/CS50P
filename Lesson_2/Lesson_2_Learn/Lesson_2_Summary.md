# Lesson 2 Summary: Conditionals and Boolean Logic

Lesson 2 teaches programs how to make decisions. The main ideas are:

- Comparisons produce Boolean values: `True` or `False`.
- `if`, `elif`, and `else` select which code runs.
- `and`, `or`, and `not` combine or reverse conditions.
- The modulo operator `%` can test divisibility and determine whether a number is even.
- Functions can return Boolean values for use as conditions.
- Nested conditionals support decisions with more than one factor.
- `match` and `case` provide another way to handle fixed alternatives.

## 1. What is a conditional?

A conditional lets a program ask a question and choose what to do based on the answer.

```python
if condition:
    # Run this when the condition is True
```

The condition must evaluate to a Boolean value:

```python
True
False
```

For example:

```python
x = 5

if x > 0:
    print("x is positive")
```

The comparison `x > 0` evaluates to `True`, so the indented line runs.

## 2. Comparison operators

Comparison operators compare two values and produce `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `x == y` |
| `!=` | Not equal to | `x != y` |
| `<` | Less than | `x < y` |
| `>` | Greater than | `x > y` |
| `<=` | Less than or equal to | `x <= y` |
| `>=` | Greater than or equal to | `x >= y` |

Examples:

```python
5 > 3   # True
5 < 3   # False
5 == 5  # True
5 != 5  # False
```

Use `==` when comparing values. A single `=` performs assignment:

```python
x = 5      # Assign 5 to x
x == 5     # Ask whether x equals 5
```

## 3. `if`, `elif`, and `else`

Use an `if`/`elif`/`else` chain when only one branch should run:

```python
x = int(input("What is x? "))
y = int(input("What is y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y are equal")
```

Python checks the branches from top to bottom:

1. If `x < y` is true, Python runs that block and skips the remaining branches.
2. Otherwise, Python checks `x > y`.
3. If neither comparison is true, equality is the only possibility, so `else` runs.

### Why use `elif`?

`elif` means **else if**. Python checks it only when every earlier condition in the same chain was false.

```python
if condition_one:
    ...
elif condition_two:
    ...
else:
    ...
```

At most one branch in this chain runs.

### Separate `if` statements behave differently

With separate `if` statements, Python checks every condition independently:

```python
if score >= 90:
    print("A")

if score >= 80:
    print("At least a B")
```

A score of `95` makes both conditions true, so both messages are printed. Use `elif` when the outcomes should be mutually exclusive.

## 4. Logical operators

Logical operators combine or reverse Boolean expressions.

### `and`

Both conditions must be true:

```python
if score >= 90 and score <= 100:
    print("Grade A")
```

| Left side | Right side | Result with `and` |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

### `or`

At least one condition must be true:

```python
if x < y or x > y:
    print("x is not equal to y")
```

This can be expressed more directly as:

```python
if x != y:
    print("x is not equal to y")
```

### `not`

`not` reverses a Boolean value:

```python
if not x == y:
    print("x is not equal to y")
```

Again, the clearer version is:

```python
if x != y:
    print("x is not equal to y")
```

Use the simplest condition that clearly expresses the intended question.

## 5. Chained comparisons

Python can combine related numerical comparisons:

```python
if score >= 90 and score <= 100:
    print("Grade A")
```

This can be written more readably as:

```python
if 90 <= score <= 100:
    print("Grade A")
```

Python reads this like the mathematical statement:

```text
90 is less than or equal to score,
and score is less than or equal to 100.
```

A complete grading chain might be:

```python
if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 0 <= score < 70:
    print("Below C")
else:
    print("Invalid score")
```

The order matters. Python stops at the first true branch.

## 6. The modulo operator `%`

Modulo returns the remainder after division:

```python
5 % 3  # 2
8 % 2  # 0
```

If dividing by `2` leaves a remainder of `0`, the number is even:

```python
x = int(input("What is x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

For `x = 8`:

```text
8 % 2 -> 0
0 == 0 -> True
```

For `x = 7`:

```text
7 % 2 -> 1
1 == 0 -> False
```

## 7. Functions that return Boolean values

A function can answer a yes-or-no question by returning `True` or `False`:

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

This works, but the comparison already produces the Boolean value we need. The function can therefore be simplified:

```python
def is_even(n):
    return n % 2 == 0
```

Use it as a condition:

```python
def main():
    x = int(input("What is x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()
```

The data flow is:

```text
main() gets x
  -> main() passes x to is_even()
  -> is_even() evaluates n % 2 == 0
  -> is_even() returns True or False
  -> the if statement chooses a branch
```

Functions named like questions—such as `is_even()`—often return Boolean values.

## 8. Conditional expressions

Python can place a simple `if`/`else` decision on one line:

```python
return True if n % 2 == 0 else False
```

The structure is:

```python
value_if_true if condition else value_if_false
```

For this particular example, the one-line conditional is unnecessary because `n % 2 == 0` already produces `True` or `False`:

```python
return n % 2 == 0
```

Conditional expressions are most useful when the two possible results are different values:

```python
description = "even" if n % 2 == 0 else "odd"
```

## 9. Nested conditionals

A conditional can appear inside another conditional. This is called nesting:

```python
if difficulty == "difficult":
    if players == "multiplayer":
        recommend("poker")
    elif players == "single":
        recommend("Klondike")
elif difficulty == "casual":
    if players == "multiplayer":
        recommend("hearts")
    elif players == "single":
        recommend("clock")
else:
    print("Invalid difficulty")
```

The outer conditional first chooses a difficulty. The inner conditional then chooses based on the number of players.

Indentation shows which decision belongs inside which branch.

Nested conditionals are useful when the second question depends on the result of the first. They can become difficult to read when deeply nested, so keep each branch clear and validate all expected inputs.

## 10. Normalizing user input

String comparisons are case-sensitive:

```python
"Harry" == "harry"  # False
```

Normalize input before comparing it:

```python
name = input("What is your name? ").strip().lower()

if name == "harry":
    print("Gryffindor")
```

- `.strip()` removes whitespace at the beginning and end.
- `.lower()` converts letters to lowercase.

This lets inputs such as `"Harry"`, `"HARRY"`, and `" harry "` match the same condition.

## 11. `match` and `case`

`match` compares one value against several patterns:

```python
name = input("What is your name? ").strip().lower()

match name:
    case "harry":
        print("Gryffindor")
    case "ron":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Unknown student")
```

Python checks the cases from top to bottom and executes the first matching case.

### Combining cases with `|`

Use `|` when several patterns should have the same outcome:

```python
match name:
    case "harry" | "hermione" | "ron":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Unknown student")
```

The `|` means **or** between patterns.

### The wildcard case `_`

```python
case _:
```

The underscore is a wildcard that matches anything not handled by an earlier case. It plays a role similar to `else`.

`match` was introduced in Python 3.10. An `if`/`elif`/`else` chain remains appropriate when conditions involve ranges, inequalities, or different variables.

## 12. Choosing between conditional patterns

| Goal | Appropriate pattern |
|---|---|
| Run code only when one condition is true | `if` |
| Choose one of several mutually exclusive outcomes | `if` / `elif` / `else` |
| Require two conditions | `and` |
| Accept either condition | `or` |
| Reverse a condition | `not` |
| Test whether a number is divisible | `%` |
| Ask a reusable yes-or-no question | Function returning `bool` |
| Make a second decision inside a selected category | Nested conditional |
| Match one value against fixed alternatives | `match` / `case` |
| Handle every unmatched case | `else` or `case _` |

## 13. Corrections and cautions from the lesson files

1. The modulo example in `Lesson_2_Conditionals.py` is inaccurate. `5 % 3` has remainder `2`; `3 % 5` has remainder `3`.
2. After checking `x < y` and `x > y`, the remaining possibility is equality. The final equality branch can therefore be `else` instead of `elif x == y`.
3. In the grade file, the final `else` includes scores below `70` as well as invalid scores above `100` or below `0`; it does not necessarily mean the user passed.
4. The additional standalone `if 90 <= score <= 100` runs after the original grading chain, so an A score prints two messages. Treat the versions as alternatives rather than running both.
5. `Lesson_2_Conditionals_Grades.py` defines `main()` but never calls it. Add `main()` after the function definitions to run that section.
6. That file defines `is_even()` three times. Each new definition replaces the previous one; only the final definition remains active.
7. A function may call another function defined later in the file only if that later definition has executed before the call actually occurs. Defining `main()` first and calling it at the bottom satisfies this requirement.
8. The recommendation program collects `difficulty` and `players` as global variables. Gathering them inside `main()` or passing them as parameters would make the data flow clearer.
9. The recommendation branches treat some invalid player inputs as valid fallbacks—for example, any non-`"multiplayer"` casual input recommends `"clock"`. Explicitly validate both expected values.
10. `Lesson_2_Match.py` asks for a name three times because it contains three executable versions of the same example. Treat those sections as alternatives and run only one version at a time.
11. The match examples use inconsistent capitalization: `"Harry"`, `"hermione"`, and `"ron"`. Normalize the input and use one consistent case.
12. Parentheses around a single string, as in `("Draco")`, do not create a tuple and are unnecessary. A one-item tuple requires a comma: `("Draco",)`.

## Final mental model

```text
Comparisons ask questions and produce True or False.
Logical operators combine or reverse those questions.
Conditionals choose which branch runs.
Modulo helps test divisibility.
Boolean-returning functions package reusable questions.
Nested conditionals make decisions in stages.
Match/case handles fixed alternatives clearly.
```
