# Lesson 1 Summary: Variables, Types, Input, and Functions

Lesson 1 introduces the basic building blocks of Python programs. The main ideas are:

- Programs execute instructions in order, usually from top to bottom.
- Variables give names to values.
- `input()` collects text from the user.
- Strings represent text, integers represent whole numbers, and floats represent decimal numbers.
- Functions perform tasks and can receive arguments.
- String methods transform strings.
- Type-conversion functions such as `int()` and `float()` convert values.
- F-strings combine text, variables, expressions, and formatting.
- Custom functions organize reusable behavior.
- `return` sends a result back to the code that called a function.
- A `main()` function can organize the central flow of a program.

## 1. Programs, values, and variables

A variable is a name that refers to a value:

```python
name = "Mario"
age = 30
```

The assignment operator `=` stores the value on the right under the name on the left:

```text
name = "Mario"
  ^       ^
variable  value
```

Assignment is different from equality testing:

```python
name = "Mario"   # Assign a value
name == "Mario"  # Ask whether two values are equal
```

Python executes ordinary statements in order:

```python
x = 1
y = 2
z = x + y
print(z)
```

By the time Python evaluates `z = x + y`, both `x` and `y` already exist.

## 2. Built-in functions

Python provides ready-made functions. Lesson 1 uses several of them:

| Function | Purpose |
|---|---|
| `print()` | Display output |
| `input()` | Ask the user for text |
| `int()` | Convert a compatible value to an integer |
| `float()` | Convert a compatible value to a floating-point number |
| `round()` | Round a number |

A function call uses parentheses:

```python
print("Hello")
```

The value placed inside the parentheses is an argument passed to the function.

## 3. Getting user input

`input()` displays a prompt, waits for the user to type something, and returns the response:

```python
name = input("What is your name? ")
```

If the user types `Mario`, the returned value is stored in `name`:

```text
name -> "Mario"
```

An important rule is:

> `input()` always returns a string.

Even if the user enters `42`, Python initially receives it as:

```python
"42"
```

not:

```python
42
```

The quotation marks illustrate the difference between text and a numeric value.

## 4. Strings

A string is text surrounded by quotation marks:

```python
first_name = "Mario"
message = 'Hello'
```

Single and double quotation marks both create strings. Use one style consistently or alternate them when strings are nested.

### Joining strings with `+`

The `+` operator concatenates strings:

```python
name = "Mario"
print("Hello, " + name)
```

Output:

```text
Hello, Mario
```

Both sides of string concatenation must normally be strings:

```python
age = 30
print("Age: " + str(age))
```

Lesson 1 does not otherwise need `str()` because f-strings provide a clearer solution.

## 5. String methods

A method is a function associated with a particular kind of object. String methods are called using a dot:

```python
name.strip()
name.title()
```

### `.strip()`

`.strip()` removes whitespace from the beginning and end of a string:

```python
name = "   mario   "
name = name.strip()
```

The result is:

```python
"mario"
```

It does not remove meaningful spaces inside a string such as `"Mario Rossi"`.

### `.title()`

`.title()` capitalizes words in a string:

```python
name = "mario rossi"
name = name.title()
```

The result is:

```python
"Mario Rossi"
```

### Chaining methods

Methods can be chained:

```python
name = input("What is your name? ").strip().title()
```

The data flows through the chain:

```text
input(...)
  -> returns the user's string
  -> .strip() removes outside whitespace
  -> .title() capitalizes its words
  -> the final string is assigned to name
```

Each method operates on the value returned by the operation immediately before it.

## 6. F-strings

An f-string is a formatted string. Prefix the opening quotation mark with `f` and place expressions inside curly braces:

```python
name = "Mario"
print(f"Hello, {name}")
```

The `f` tells Python to evaluate what appears inside `{}` and insert the result into the string.

Output:

```text
Hello, Mario
```

F-strings can include several values:

```python
name = "Mario"
age = 30
print(f"{name} is {age} years old")
```

They can also evaluate expressions:

```python
x = 1
y = 2
print(f"The sum is {x + y}")
```

Unlike string concatenation, an f-string formats numeric values without requiring an explicit `str()` conversion.

## 7. Integers

An integer is a whole number:

```python
x = 1
y = 2
z = x + y
```

Common arithmetic operators include:

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `x + y` |
| `-` | Subtraction | `x - y` |
| `*` | Multiplication | `x * y` |
| `/` | Division | `x / y` |
| `**` | Exponentiation | `x ** 2` |

Because `input()` returns a string, numeric input must be converted before arithmetic:

```python
a = int(input("a is equal to? "))
b = int(input("b is equal to? "))
print(a + b)
```

Python evaluates the nested call from the inside outward:

```text
input(...)
  -> returns text such as "2"
  -> int(...) converts "2" to 2
  -> the integer 2 is assigned to a
```

Without conversion:

```python
a = input("a: ")  # User enters 1
b = input("b: ")  # User enters 2
print(a + b)
```

the output is string concatenation:

```text
12
```

With `int()`, the result is numeric addition:

```text
3
```

Entering text that cannot be converted to an integer raises a `ValueError`. Error handling is covered later in the course.

## 8. Floating-point numbers

A float is a number that can contain a decimal point:

```python
price = 12.50
temperature = 21.7
```

Convert user input with `float()` when decimal values should be accepted:

```python
a = float(input("a is equal to? "))
b = float(input("b is equal to? "))
print(a + b)
```

`int("2.5")` fails because `2.5` is not a whole-number string, while `float("2.5")` returns `2.5`.

Floating-point values are approximations in computers, so some decimal calculations can display tiny precision differences. Formatting or rounding controls how results are presented.

## 9. Rounding and number formatting

`round()` rounds a number:

```python
result = round(3.14159, 2)
```

The second argument specifies the number of decimal places:

```text
round(3.14159, 2) -> 3.14
round(3.14159, 1) -> 3.1
```

An f-string format specifier follows a colon inside `{}`:

```python
amount = 12345.6
print(f"{amount:,}")
```

Output:

```text
12,345.6
```

The comma requests a thousands separator. To show exactly one decimal place and a thousands separator:

```python
print(f"The sum is {a + b:,.1f}")
```

For example:

```text
12,345.6
```

Here:

- `:` begins the format specification.
- `,` adds thousands separators.
- `.1f` displays one digit after the decimal point.

## 10. Defining custom functions

Use `def` to create a function:

```python
def hello():
    print("Hello")
```

The function definition includes:

```text
def hello():
 ^    ^   ^^
 |    |   parentheses and colon
 |    function name
 define a function
```

The indented code belongs to the function. Defining it does not run it.

Call the function to execute its body:

```python
hello()
```

The parentheses in the call tell Python to execute the function.

## 11. Parameters and arguments

Parameters let a function receive information:

```python
def answer_question(name, question):
    print(f"Okay {name}, I will research: {question}")
```

Call it with arguments:

```python
answer_question("Mario", "What is Python?")
```

The relationship is:

```text
Function definition: name and question are parameters.
Function call: "Mario" and "What is Python?" are arguments.
```

On this call:

```text
name     -> "Mario"
question -> "What is Python?"
```

Parameters make functions reusable because callers can provide different values each time.

## 12. Scope

Scope describes where a variable is available.

A parameter or variable created inside a function is local to that function:

```python
def greet(person):
    message = f"Hello, {person}"
    print(message)
```

Here, `person` and `message` are local variables. Code outside `greet()` cannot directly use `message` after the function finishes.

Functions can read variables defined globally, but relying on globals makes a function less reusable and its dependencies less clear:

```python
name = "Mario"

def hello():
    print(name)
```

A clearer version passes the value explicitly:

```python
def hello(name):
    print(name)


hello("Mario")
```

Use parameters to make required information visible in the function definition.

## 13. `return` versus `print`

`print()` displays a value. `return` sends a value back to the calling code.

```python
def square(n):
    return n * n
```

Calling the function produces a value:

```python
result = square(4)
```

The returned value `16` is assigned to `result`.

The value can instead be printed directly:

```python
print(square(4))
```

The execution order is:

```text
square(4)
  -> n receives 4
  -> n * n produces 16
  -> return sends 16 back
  -> print displays 16
```

Compare these functions:

```python
def show_square(n):
    print(n * n)


def calculate_square(n):
    return n * n
```

`show_square()` only displays the result. `calculate_square()` gives the result back, allowing it to be stored, printed, or used in another calculation.

A function with no explicit `return` automatically returns `None`.

## 14. The `main()` function pattern

Python does not require a function named `main`, but it is a useful convention for organizing a program's central logic:

```python
def main():
    number = int(input("Give me a number: "))
    print("The number squared is", square(number))


def square(n):
    return n * n


main()
```

The program works as follows:

```text
main() is called
  -> input() obtains text
  -> int() converts it to a number
  -> square(number) calculates and returns the square
  -> print() displays the returned result
```

Python first processes both function definitions. The final `main()` call starts the program. This is why `main()` can call `square()` even though the `square` definition appears later in the file: `square` has been defined by the time `main()` is actually called.

## 15. Functions, methods, statements, and expressions

These terms describe different parts of Python:

| Term | Meaning | Example |
|---|---|---|
| Function | Reusable behavior called by name | `print("Hi")` |
| Method | Function associated with an object | `name.strip()` |
| Statement | An instruction Python executes | `return n * n` |
| Expression | Code that produces a value | `n * n` |

In:

```python
return n * n
```

- `return` is a statement.
- `n * n` is an expression that produces a value.
- The statement sends that value back to the caller.

Not every statement uses parentheses. Parentheses are primarily used for function and method calls, grouping, and some data structures.

## 16. Choosing the appropriate tool

| Goal | Typical Python |
|---|---|
| Ask the user for text | `input("Prompt: ")` |
| Display a value | `print(value)` |
| Clean outside whitespace | `text.strip()` |
| Capitalize words | `text.title()` |
| Insert values into text | `f"Hello, {name}"` |
| Convert input to a whole number | `int(input(...))` |
| Convert input to a decimal number | `float(input(...))` |
| Round a number | `round(number, places)` |
| Define reusable behavior | `def function_name(...):` |
| Supply information to a function | Parameters and arguments |
| Send a result back | `return value` |
| Organize the program's central flow | `main()` |

## 17. Corrections and cautions from the lesson files

1. `.strip()` removes leading and trailing whitespace; it does not remove all spaces inside a string.
2. `.title()` capitalizes words, not only the first letter of the entire string.
3. “Read right to left” is useful for simple nested calls, but method chains flow from left to right through returned values. In `int(input(...))`, the inner `input()` is evaluated before the outer `int()`.
4. The float lesson says it rounds to two decimal places, but `round(a + b, 1)` rounds to one decimal place.
5. The colon in an f-string begins a format specification; the comma after it specifically requests thousands separators.
6. A function can read a global variable, so the scope note saying it can access only local variables or parameters is too strict. Passing arguments is still clearer and safer.
7. The first `hello()` function depends on global `name` and `age`. A version such as `hello(name, age)` would make those dependencies explicit.
8. `main()` is a convention, not a special Python keyword. Defining it does nothing until it is called.
9. Statements are not defined by the absence of parentheses. Some statements contain function calls, and parentheses have several purposes.
10. All five lesson source files contain Python code but currently have no `.py` filename extensions. Python can still run them, but `.py` extensions improve editor and tooling recognition.

## Final mental model

```text
Values are pieces of data.
Variables give those values names.
Input collects strings from the user.
Type conversion turns strings into useful numeric types.
Methods transform objects such as strings.
F-strings combine values with readable output.
Functions organize reusable behavior.
Parameters carry information into functions.
Return values carry results out of functions.
main() organizes the program's overall flow.
```
