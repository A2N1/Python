# Python Cheat Sheet – COMPLETE LEARNING VERSION 📘 (Python 3.10+)

This cheat sheet covers **core Python concepts**, syntax, data structures, OOP, standard library, and modern Python features.  
Suitable for beginners and refreshers (Scripting / Backend / Data).

---

## Table of Contents

- [Python Cheat Sheet – COMPLETE LEARNING VERSION 📘 (Python 3.10+)](#python-cheat-sheet--complete-learning-version--python-310)
  - [Table of Contents](#table-of-contents)
  - [1. Basics](#1-basics)
  - [2. Variables \& Data Types](#2-variables--data-types)
  - [3. Operators](#3-operators)
  - [4. Control Structures](#4-control-structures)
  - [5. Functions](#5-functions)
  - [6. Lists](#6-lists)
  - [7. Tuples \& Sets](#7-tuples--sets)
  - [8. Dictionaries](#8-dictionaries)
  - [9. Loops](#9-loops)
  - [10. Strings](#10-strings)
  - [11. Modules \& Imports](#11-modules--imports)
  - [12. Object-Oriented Python](#12-object-oriented-python)
  - [13. Inheritance \& Polymorphism](#13-inheritance--polymorphism)
  - [14. Exceptions](#14-exceptions)
  - [15. File Handling](#15-file-handling)
  - [16. List Comprehensions](#16-list-comprehensions)
  - [17. Lambdas \& Functional Tools](#17-lambdas--functional-tools)
  - [18. Standard Library Highlights](#18-standard-library-highlights)
  - [19. Modern Python Features](#19-modern-python-features)
  - [20. Best Practices](#20-best-practices)
  - [End](#end)

---

## 1. Basics

~~~python
# Python code is interpreted and dynamically typed

print("Hello World")

# Comments
# single-line
"""
multi-line
"""
~~~

---

## 2. Variables & Data Types

~~~python
# Dynamic typing
name = "Max"
age = 30
price = 9.99
active = True
nothing = None

# Type checking
type(age)        # <class 'int'>
isinstance(age, int)
~~~

---

## 3. Operators

~~~python
# Arithmetic
5 + 3
5 - 3
5 * 3
5 / 2     # float division
5 // 2    # integer division
5 % 2

# Comparison
1 == 1
1 != 2
3 > 2

# Logical
True and False
True or False
not True

# Ternary
status = "adult" if age >= 18 else "minor"
~~~

---

## 4. Control Structures

~~~python
score = 85

if score > 90:
    grade = "A"
elif score > 80:
    grade = "B"
else:
    grade = "C"
~~~

---

## 5. Functions

~~~python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str = "Guest") -> str:
    return f"Hello {name}"

def sum_all(*numbers: int) -> int:
    return sum(numbers)
~~~

---

## 6. Lists

~~~python
numbers = [1, 2, 3]

numbers.append(4)
numbers.pop()

numbers[0]

# Copy
copy = numbers[:]
~~~

---

## 7. Tuples & Sets

~~~python
# Tuple (immutable)
coords = (10, 20)

# Set (unique values)
unique_numbers = {1, 2, 2, 3}
~~~

---

## 8. Dictionaries

~~~python
user = {
    "name": "Max",
    "age": 30
}

user["name"]
user.get("email", "not set")

# Keys & values
user.keys()
user.values()
~~~

---

## 9. Loops

~~~python
for i in range(3):
    print(i)

i = 0
while i < 3:
    print(i)
    i += 1

for key, value in user.items():
    print(key, value)
~~~

---

## 10. Strings

~~~python
text = "Hello"

len(text)
text.upper()
text.replace("H", "J")

name = "Max"
f"Hello {name}"
~~~

---

## 11. Modules & Imports

~~~python
import math
from math import sqrt

sqrt(16)

# Custom module
import my_module
~~~

---

## 12. Object-Oriented Python

~~~python
class Person:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello {self.name}"

p = Person("Max")
p.greet()
~~~

---

## 13. Inheritance & Polymorphism

~~~python
class Student(Person):
    def study(self) -> str:
        return "Studying"

s = Student("Anna")
s.greet()
~~~

---

## 14. Exceptions

~~~python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(e)
finally:
    print("Done")
~~~

---

## 15. File Handling

~~~python
# Write file
with open("file.txt", "w") as f:
    f.write("Hello")

# Read file
with open("file.txt", "r") as f:
    content = f.read()
~~~

---

## 16. List Comprehensions

~~~python
numbers = [1, 2, 3, 4]

squares = [n * n for n in numbers]
filtered = [n for n in numbers if n > 2]
~~~

---

## 17. Lambdas & Functional Tools

~~~python
double = lambda x: x * 2

list(map(double, [1, 2, 3]))
list(filter(lambda x: x > 1, [1, 2, 3]))
~~~

---

## 18. Standard Library Highlights

~~~python
import os
import sys
import json
import datetime

json.dumps({"a": 1})
datetime.datetime.now()
~~~

---

## 19. Modern Python Features

~~~python
# Match statement (Python 3.10+)
role = "admin"

match role:
    case "admin":
        result = "Admin"
    case _:
        result = "User"

# Dataclasses
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
~~~

---

## 20. Best Practices

- Follow PEP 8
- Use virtual environments
- Prefer readability over cleverness
- Use type hints
- Handle exceptions explicitly
- Write small, reusable functions
- Avoid global state

---

## End
