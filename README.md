# ![Python Templates](images/python-full-50.png)

<!--
TODO: Add function definitions to all functions:

def say_hello():

    """
    # Hello function

    this is a comment about the Hello function

    > Note: something of note

    ```python
    let i = Hello
    print(i)
    ```
    """

    print("Hello")
-->

<a href="https://www.python.org/">Python</a> is a general-purpose, user-friendly
programming language known for its great readability and versatility. It has a
vast ecosystem of libraries and frameworks, making it suitable for various
applications, from web development to scientific computing, and is compatible
across all operating systems.

<br>

## <img src="images/template-20.png" alt="template"> Templates

<br>

![Generic](images/generic-20.png)

- Template outlining Pythonic syntax and layout styling.

- Collection of useful classes and functions.

<br>

[![Flask](images/flask-full-30.png)](https://github.com/ilya0x/flask-templates)

Flask is a flexible minimalistic Python web framework.

<br>

[![Django](images/django-full-30.png)](https://github.com/ilya0x/django-templates)

Django is a high-level web framework for Python that simplifies web application
development.

<br>
<!--
[![PyTorch](images/pytorch-full-30.png)](https://github.com/ilya0x/pytorch-templates)

PyTorch is a fully featured Python framework for building deep learning models
for Machine Learning.

<br>

[![TorchAudio](images/torchaudio-full-20.png)](https://github.com/ilya0x/torchaudio-templates)

TorchAudio is a PyTorch library to work with audio.

<br>
-->

## <img src="./images/vscode-20.png" alt="Flask"> Visual Studio Code Extensions

<br>

## 📝Notes

> These notes are updated on regular basis

<!--TODO: Table of Contents -->

<br>

### Variables

- Names of variables can have letters, numbers, and underscores, but cannot
  start with numbers (it can start with underscores). Python will give you a
  SyntaxError if you use anything else that is not allowed.

- Variables are like containers that can store data, and the data they store
  must have a specific data type. variables can be associated with various data
  types. When you create a variable, you give it a name and assign a value to
  it, and that value has a particular data type.

<br>

### Data Types

<h4>Numeric Types:</h4>

`int`: Represents integer numbers (e.g., 5, -10, 1000).

`float`: Represents floating-point numbers with decimal places (e.g., 3.14,
-0.5, 2.0).

<h4>Boolean Type:</h4>

`bool`: Represents boolean values True and False. Used for logical operations
and conditions.

<h4>Text Type:</h4>

`str`: Represents strings of characters, enclosed in single (') or double (")
quotes (e.g., `"Hello, World!"`).

<h4>Sequence Types:</h4>

`list`: Represents ordered collections of items that can be of different data
types and are mutable (modifiable).

`tuple`: Represents ordered collections of
items like lists, but they are immutable (cannot be changed after creation).
range: Represents a sequence of numbers often used for iteration (e.g., `range(0,
5)`).

<h4>Mapping Type:</h4>

`dict`: Represents key-value pairs (e.g., `{"name": "John", "age": 30}`).

<h4>Set Types:</h4>

`set`: Represents an unordered collection of unique elements. Sets are mutable.

`frozenset`: Similar to sets, but they are immutable.

<h4>Sequence Types (Binary):</h4>

`bytes`: Represents a sequence of bytes (immutable).

`bytearray`: Represents a mutable sequence of bytes.

`memoryview`: Represents a memory view object, which allows viewing the memory of
other objects in a buffer-like fashion.

<h4>None Type:</h4>

`NoneType` or `None`: Represents the absence of a value or a null value. Used
when a variable or function does not return anything.

<h4>Custom Classes:</h4>

You can create your own custom data types by defining custom classes.

<br>

### Expressions vs Statements

- Expressions produce a value and are often found inside statements

- Statements perform actions and are executed sequentially. They control the
  flow of the program, define functions and classes, perform assignments, etc.

<br>

### Operators

Symbols used to perform operations on values and variables that hold those values:

<h4>Assignment operator:</h4>

`=`: Assigns the value on the right to the variable on the left

<h4>Arithmetic operators:</h4>

`+`: Addition of numbers. Can be used to concatenate two strings.

`-`: Subtraction of numbers.

`*`: Multiplication of numbers.

`/`: Division of numbers.

`//`: Floor division rounds down the result of the division.

`%`: Remainder of division.

`**`: Raises first number to the power of following number.

<h4>Comparison operators:</h4>

`==`: Compares if the value on the left equals to the value on the right.

`!=`: Compares if the value on the left does not equal to the value on the right.

`>`: Compares if the value on the left is greater then the value on the right.

`<`: Compares if the value on the left is less then the value on the right.

`>=`: Compares if the value on the left is greater then or equal to the value on
the right.

`<=`: Compares if the value on the left is less then or equal to the value on
the right.

<h4>Boolean operators:</h4>

`not`: Returns the opposite of the value.

`and`: Checks if both values are `True`. Looks at two values and stops at
`False`, or returns `True` if both values are `True`.

`or`: Checks if one or the other value is `True`. Will only look at the second
value if the first value is `False`.

<h4>Ternary Operator:</h4>

> The Pythonic Way!

``` python
print("True") if x > y else print("False")
```

<h4>More Operators to come. . .</h4>

<br>

### Value Assignment

<h4>Literal Assignment:</h4>

<h4>Constructor Function:</h4>
